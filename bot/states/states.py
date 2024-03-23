from aiogram.fsm.state import State,StatesGroup

class ShopFSM(StatesGroup):
    start = State()
    admin_choise = State()
    info = State()
    admin = State()
    add_cloth = State()

    