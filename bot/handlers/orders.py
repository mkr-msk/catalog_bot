from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from utils.api_client import api
from config import ADMIN_TELEGRAM_ID

router = Router()


class OrderForm(StatesGroup):
    waiting_for_name = State()
    waiting_for_phone = State()
    waiting_for_comment = State()


@router.callback_query(F.data.startswith("order_"))
async def start_order(callback: CallbackQuery, state: FSMContext):
    """Начало оформления заявки"""
    product_id = int(callback.data.split("_")[1])
    
    await state.update_data(product_id=product_id)
    await state.set_state(OrderForm.waiting_for_name)
    
    await callback.message.answer(
        "📝 Оформление заявки\n\n"
        "Введите ваше имя:"
    )
    await callback.answer()


@router.message(OrderForm.waiting_for_name)
async def process_name(message: Message, state: FSMContext):
    """Получение имени"""
    await state.update_data(name=message.text)
    await state.set_state(OrderForm.waiting_for_phone)
    
    await message.answer("📱 Введите ваш номер телефона:")


@router.message(OrderForm.waiting_for_phone)
async def process_phone(message: Message, state: FSMContext):
    """Получение телефона"""
    await state.update_data(phone=message.text)
    await state.set_state(OrderForm.waiting_for_comment)
    
    await message.answer(
        "💬 Напишите комментарий к заявке\n"
        "(или отправьте /skip чтобы пропустить):"
    )


@router.message(OrderForm.waiting_for_comment, F.text == "/skip")
@router.message(OrderForm.waiting_for_comment)
async def process_comment(message: Message, state: FSMContext):
    """Получение комментария и создание заявки"""
    comment = "" if message.text == "/skip" else message.text
    data = await state.get_data()
    
    order_data = {
        "customer_name": data['name'],
        "customer_phone": data['phone'],
        "customer_telegram_id": message.from_user.id,
        "customer_username": message.from_user.username or "",
        "product": data['product_id'],
        "comment": comment
    }
    
    try:
        order = await api.create_order(order_data)
        
        await message.answer(
            "✅ Заявка успешно отправлена!\n\n"
            "Мы свяжемся с вами в ближайшее время."
        )
        
        # Уведомление админу
        product = await api.get_product(data['product_id'])
        admin_text = (
            f"🔔 Новая заявка #{order['id']}\n\n"
            f"👤 Клиент: {data['name']}\n"
            f"📱 Телефон: {data['phone']}\n"
            f"📦 Товар: {product['name']}\n"
            f"💰 Цена: {product['price']} ₽\n"
        )
        if comment:
            admin_text += f"💬 Комментарий: {comment}\n"
        
        if message.from_user.username:
            admin_text += f"\n👉 @{message.from_user.username}"
        
        await message.bot.send_message(ADMIN_TELEGRAM_ID, admin_text)
        
    except Exception as e:
        await message.answer(
            "❌ Ошибка при отправке заявки. Попробуйте позже."
        )
    
    await state.clear()