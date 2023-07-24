from loader import dp

from data.callbacks import PAYMENT_CALLBACK_DATA

from functions import clear_last_ikb, call_payment_ikb

from states import MainMenuStatesGroup, PaymentStatesGroup

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.callback_query_handler(lambda c: c.data == PAYMENT_CALLBACK_DATA, state=MainMenuStatesGroup.main_menu)
async def payment_menu(callback: types.CallbackQuery, state: FSMContext) -> None:
    user_id = callback.from_user.id

    # Clear last inline keyboard.
    await clear_last_ikb(user_id=user_id, state=state)
    # Call payment inline menu.
    await call_payment_ikb(user_id=user_id, state=state)
    # Set payment_menu state.
    await PaymentStatesGroup.payment_menu.set()
