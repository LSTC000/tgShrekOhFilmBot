from data.config import ROW_WIDTH

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA

from data.messages import (
    CANCEL_TO_MAIN_MENU_IKB_MESSAGE,
    SOCIAL_TIK_TOK_CHANNEL_URL_IKB_MESSAGE,
    SOCIAL_OFFICIAL_TG_GROUP_IKB_MESSAGE
)

from data.urls import TIK_TOK_CHANNEL_URL, OFFICIAL_GROUP_URL

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def social_ikb() -> InlineKeyboardMarkup:
    """
    :return: Social inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(text=SOCIAL_TIK_TOK_CHANNEL_URL_IKB_MESSAGE, url=TIK_TOK_CHANNEL_URL))
    ikb.row(InlineKeyboardButton(text=SOCIAL_OFFICIAL_TG_GROUP_IKB_MESSAGE, url=OFFICIAL_GROUP_URL))
    ikb.row(InlineKeyboardButton(text=CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA))

    return ikb
