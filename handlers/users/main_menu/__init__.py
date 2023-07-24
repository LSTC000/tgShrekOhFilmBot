__all__ = ['register_users_main_menu']


from .change_user_alert import change_user_alert
from .user_review_clb import user_review_clb
from .user_review_msg import user_review_msg

from aiogram import Dispatcher


def register_users_main_menu(dp: Dispatcher):
    dp.register_callback_query_handler(change_user_alert)
    dp.register_callback_query_handler(user_review_clb)
    dp.register_message_handler(user_review_msg)
