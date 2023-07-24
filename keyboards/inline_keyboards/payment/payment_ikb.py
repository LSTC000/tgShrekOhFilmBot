from data.config import ROW_WIDTH

from data.callbacks import CANCEL_TO_MAIN_MENU_CALLBACK_DATA, YOOMONEY_PAYMENT_CALLBACK_DATA

from data.messages import (
    YOOMONEY_PAYMENT_IKB_MESSAGE,
    DONATION_ALERTS_PAYMENT_URL_IKB_MESSAGE,
    CANCEL_TO_MAIN_MENU_IKB_MESSAGE
)

from data.urls import DONATION_ALERTS_URL

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def payment_ikb() -> InlineKeyboardMarkup:
    """
    :return: Payment inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(InlineKeyboardButton(text=DONATION_ALERTS_PAYMENT_URL_IKB_MESSAGE, url=DONATION_ALERTS_URL))
    ikb.row(InlineKeyboardButton(text=YOOMONEY_PAYMENT_IKB_MESSAGE, callback_data=YOOMONEY_PAYMENT_CALLBACK_DATA))
    ikb.row(InlineKeyboardButton(text=CANCEL_TO_MAIN_MENU_IKB_MESSAGE, callback_data=CANCEL_TO_MAIN_MENU_CALLBACK_DATA))

    return ikb
