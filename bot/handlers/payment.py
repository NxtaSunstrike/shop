from aiogram import types,F,Router,Bot
from aiogram.filters import Command

router = Router()

@router.message(Command(commands=['buy']))
async def buy(call: types.CallbackQuery):
    await call.bot.send_invoice(
        chat_id=call.from_user.id,
        title='Товар',
        description='Описание товара',
        provider_token='381764678:TEST:81032',
        payload='new',
        prices=[
            types.LabeledPrice(label='Товар', amount=90000)
            ],
        start_parameter='new-invoice',

        need_name=True,
        need_phone_number=True,
        need_shipping_address=True,
        currency='rub',
        request_timeout=100
        )

@router.pre_checkout_query(lambda query:True)
async def process_payment(pre_checkout: types.PreCheckoutQuery,bot:Bot):
    await bot.answer_pre_checkout_query(pre_checkout.id, ok=True)


