__all__ = ['register_users_payments']


from .payment_menu import payment_menu
from .yoomoney_payment_msg import yoomoney_payment_msg
from .yoomoney_payment_clb import yoomoney_payment_clb

from aiogram import Dispatcher


def register_users_payments(dp: Dispatcher):
    dp.register_callback_query_handler(payment_menu)
    dp.register_message_handler(yoomoney_payment_msg)
    dp.register_callback_query_handler(yoomoney_payment_clb)
