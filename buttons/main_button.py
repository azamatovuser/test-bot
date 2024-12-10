from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Hamma userlarni ko\'rish 👤'),
     KeyboardButton(text='Mahsulot qo\'shish 📦'),],
    [KeyboardButton(text="Mahsulotlarni ko'rish")],
    [KeyboardButton(text="Malumonti o'zgartirish")],
    [KeyboardButton(text="Mahsulotni o'chirib tashlash")]
], resize_keyboard=True)