from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from utils.api_client import api
from keyboards.inline import (
    get_categories_keyboard,
    get_products_keyboard,
    get_product_detail_keyboard
)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    """Обработка команды /start"""
    categories = await api.get_categories()
    
    if not categories:
        await message.answer("Каталог пока пуст. Попробуйте позже.")
        return
    
    await message.answer(
        "👋 Добро пожаловать!\n\n"
        "Выберите категорию:",
        reply_markup=get_categories_keyboard(categories)
    )


@router.callback_query(F.data == "back_to_categories")
async def back_to_categories(callback: CallbackQuery):
    """Возврат к списку категорий"""
    categories = await api.get_categories()
    
    await callback.message.edit_text(
        "Выберите категорию:",
        reply_markup=get_categories_keyboard(categories)
    )
    await callback.answer()


@router.callback_query(F.data.startswith("category_"))
async def show_category_products(callback: CallbackQuery):
    """Показ товаров категории"""
    category_id = int(callback.data.split("_")[1])
    products = await api.get_products_by_category(category_id)
    
    if not products:
        await callback.answer("В этой категории пока нет товаров", show_alert=True)
        return
    
    category_name = products[0]['category_name']
    
    await callback.message.edit_text(
        f"📂 {category_name}\n\nВыберите товар:",
        reply_markup=get_products_keyboard(products)
    )
    await callback.answer()


@router.callback_query(F.data.startswith("product_"))
async def show_product_detail(callback: CallbackQuery):
    """Показ карточки товара"""
    product_id = int(callback.data.split("_")[1])
    product = await api.get_product(product_id)
    
    text = (
        f"📦 {product['name']}\n\n"
        f"{product['description']}\n\n"
        f"💰 Цена: {product['price']} ₽"
    )
    
    category_id = product['category_id']
    
    if product.get('telegram_file_id'):
        await callback.message.delete()
        await callback.message.answer_photo(
            photo=product['telegram_file_id'],
            caption=text,
            reply_markup=get_product_detail_keyboard(product_id, category_id)
        )
    else:
        await callback.message.edit_text(
            text,
            reply_markup=get_product_detail_keyboard(product_id, category_id)
        )
    
    await callback.answer()