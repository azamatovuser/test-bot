from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from database import get_users, get_all_products, delete_product, update_product
from states import DeleteProduct, UpdateProduct


button_handlers_router = Router()


@button_handlers_router.message(F.text ==
                                'Hamma userlarni ko\'rish 👤')
async def get_all_users(message: Message):
    users = get_users()
    for user in users:
        await message.answer(f"ID: {user[0]}\nIsm familya: "
                             f"{user[1]}")


@button_handlers_router.message(F.text == "Mahsulotlarni ko'rish")
async def all_products(message: Message):
    products = get_all_products()
    for product in products:
        await message.answer_photo(photo=product[2],
                                   caption=f"Ismi - {product[0]}\n"
                                           f"Narxi - {product[1]}")


@button_handlers_router.message(F.text == "Mahsulotni o'chirib tashlash")
async def delete_function(message: Message, state: FSMContext):
    await state.set_state(DeleteProduct.name)
    await message.answer('Qaysi mahsulotni olib tashlamoqchisiz?')


@button_handlers_router.message(DeleteProduct.name)
async def name_product_function(message: Message, state: FSMContext):
    product_name = message.text
    delete_product(product_name)
    await message.answer("Mahsulot o'chirildi")
    await state.clear()


@button_handlers_router.message(F.text == "Malumonti o'zgartirish")
async def update_function(message: Message, state: FSMContext):
    await message.answer("Qaysi mahsulotni o'zgartirmoqchisiz?")
    await state.set_state(UpdateProduct.name)


@button_handlers_router.message(UpdateProduct.name)
async def name_function(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Endi narxni kiriting")
    await state.set_state(UpdateProduct.price)


@button_handlers_router.message(UpdateProduct.price)
async def price_func(message: Message, state: FSMContext):
    await state.set_state(UpdateProduct.image)
    await state.update_data(price=message.text)
    await message.answer("Endi rasmni jo'nating")


@button_handlers_router.message(UpdateProduct.image)
async def image_func(message: Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    await message.answer("Mahsulot o'zgardi")
    data = await state.get_data()
    update_product(name=data['name'], price=data['price'], image=data['image'])
    await state.clear()
