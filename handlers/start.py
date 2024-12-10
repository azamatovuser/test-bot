from aiogram import Router, types, filters, F
from aiogram.fsm.context import FSMContext
from buttons import main_button
from database import create_table_users, add_user, create_table_product, add_product_data
from states.products import Products


start_router = Router()


@start_router.message(filters.Command('start'))
async def start_function(message: types.Message):
    create_table_product()
    create_table_users()
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    add_user(user_id, user_full_name)
    await message.answer("Yaxshimisiz?", reply_markup=main_button)


@start_router.message(F.text == "Mahsulot qo\'shish 📦")
async def add_product(message: types.Message, state: FSMContext):
    await message.answer("Mahsulotni ismini kiriting")
    await state.set_state(Products.name)


@start_router.message(Products.name)
async def name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Endi narxini kiriting")
    await state.set_state(Products.price)


@start_router.message(Products.price)
async def price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer("Endi rasmini kiriting")
    await state.set_state(Products.image)


@start_router.message(Products.image)
async def image(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    await message.answer("Ma'lumotlar keldi")
    data = await state.get_data()
    name = data['name']
    price = data['price']
    image = data['image']
    add_product_data(name, price, image)
    await state.clear()