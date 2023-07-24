from loader import dp, bot

from data.callbacks import YOOMONEY_PAYMENT_CALLBACK_DATA

from data.messages import ENTER_YOOMONEY_PAYMENT_AMOUNT_MESSAGE

from functions import clear_last_ikb

from states import PaymentStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == YOOMONEY_PAYMENT_CALLBACK_DATA, state=PaymentStatesGroup.payment_menu)
async def yoomoney_payment_clb(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Withdrawal of the request for the introduction of the amount.
    await bot.send_message(chat_id=user_id, text=ENTER_YOOMONEY_PAYMENT_AMOUNT_MESSAGE)
    # Set enter_yoomoney_payment_amount state.
    await PaymentStatesGroup.enter_yoomoney_payment_amount.set()
