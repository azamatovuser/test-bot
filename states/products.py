from aiogram.fsm.state import State, StatesGroup

class Products(StatesGroup):
    name = State()
    image = State()
    price = State()


class DeleteProduct(StatesGroup):
    name = State()


class UpdateProduct(StatesGroup):
    name = State()
    image = State()
    price = State()