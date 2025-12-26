from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_categories_keyboard(categories: list) -> InlineKeyboardMarkup:
    """Клавиатура с категориями"""
    buttons = []
    for category in categories:
        buttons.append([
            InlineKeyboardButton(
                text=f"{category['name']} ({category['products_count']})",
                callback_data=f"category_{category['id']}"
            )
        ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_products_keyboard(products: list) -> InlineKeyboardMarkup:
    """Клавиатура с товарами категории"""
    buttons = []
    for product in products:
        buttons.append([
            InlineKeyboardButton(
                text=f"{product['name']} - {product['price']} ₽",
                callback_data=f"product_{product['id']}"
            )
        ])
    buttons.append([
        InlineKeyboardButton(text="◀️ Назад", callback_data="back_to_categories")
    ])
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def get_product_detail_keyboard(product_id: int, category_id: int) -> InlineKeyboardMarkup:
    """Клавиатура для карточки товара"""
    buttons = [
        [InlineKeyboardButton(text="📝 Оставить заявку", callback_data=f"order_{product_id}")],
        [InlineKeyboardButton(text="◀️ К товарам", callback_data=f"category_{category_id}")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)