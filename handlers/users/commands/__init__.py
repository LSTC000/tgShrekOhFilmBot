__all__ = ['register_users_commands', 'set_default_commands']


from .start_msg import start_msg
from .start_clb import start_clb
from .setting_commands import set_default_commands

from aiogram import Dispatcher


def register_users_commands(dp: Dispatcher):
    dp.register_message_handler(start_msg)
    dp.register_callback_query_handler(start_clb)
