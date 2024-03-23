import emoji

from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.keyboards.reply import start_keyboard
from bot.states.states import ShopFSM

router = Router()

@router.message(CommandStart())
async def start(message:Message,state:FSMContext)->None:
    await state.set_state(ShopFSM.start)
    await message.answer_sticker(
        'CAACAgIAAxkBAAI4BmX--zJU1Wur2r3qSfJuMrwl5yGXAAJ5EAACL384SehalBaaw7JlNAQ',
        reply_markup= start_keyboard(user_id=message.from_user.id)
        )
@router.message(F.sticker,ShopFSM.start)
async def start(message:Message,state:FSMContext)->None:
    await message.answer(message.sticker.file_id)


