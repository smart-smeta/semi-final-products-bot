from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🍔 Меню")],
        [KeyboardButton(text="📦 Мои заказы"), KeyboardButton(text="ℹ️ О нас")],
    ],
    resize_keyboard=True,
    input_field_placeholder="Выберите действие...",
)
