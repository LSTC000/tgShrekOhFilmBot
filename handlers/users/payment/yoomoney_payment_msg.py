from loader import dp, bot

from data.messages import ERROR_YOOMONEY_ENTER_PAYMENT_AMOUNT_MESSAGE

from data.config import RECEIVER, QUICKPAY_FORM, TARGETS, PAYMENT_TYPE

from functions import call_yoomoney_payment_ikb, call_payment_ikb

from states import PaymentStatesGroup

from utils import Validator

from aiogram import types
from aiogram.dispatcher.storage import FSMContext

from yoomoney import Quickpay


@dp.message_handler(state=PaymentStatesGroup.enter_yoomoney_payment_amount)
async def yoomoney_payment_msg(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    amount = message.text

    # Check amount on valid
    if Validator().payment_validation(amount):
        quickpay = Quickpay(
            receiver=RECEIVER,
            quickpay_form=QUICKPAY_FORM,
            targets=TARGETS,
            paymentType=PAYMENT_TYPE,
            sum=int(amount)
        )
        # Call yoomoney payment inline menu.
        await call_yoomoney_payment_ikb(
            user_id=user_id,
            redirected_url=quickpay.redirected_url,
            amount=amount,
            state=state
        )
    else:
        # Inform the user about an error when entering the amount.
        await bot.send_message(chat_id=user_id, text=ERROR_YOOMONEY_ENTER_PAYMENT_AMOUNT_MESSAGE)
        # Call payment inline menu.
        await call_payment_ikb(user_id=user_id, state=state)
        # Set payment_menu state.
        await PaymentStatesGroup.payment_menu.set()
