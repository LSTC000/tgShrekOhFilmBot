from data.config import ROW_WIDTH

from data.callbacks import (
    CHANGE_USER_ALERT_CALLBACK_DATA,
    PAYMENT_CALLBACK_DATA,
    SOCIAL_CALLBACK_DATA,
    USER_REVIEW_CALLBACK_DATA
)

from data.messages import (
    USER_ALERT_ON_IKB_MESSAGE,
    USER_ALERT_OFF_IKB_MESSAGE,
    SOCIAL_IKB_MESSAGE,
    USER_REVIEW_IKB_MESSAGE,
    PAYMENT_IKB_MESSAGE
)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def main_menu_ikb(alert: bool) -> InlineKeyboardMarkup:
    """
    :param alert: True if the user has enabled alerts, else False.
    :return: Main menu inline keyboard.
    """

    ikb = InlineKeyboardMarkup(row_width=ROW_WIDTH)

    ikb.row(
        InlineKeyboardButton(
            text=USER_ALERT_OFF_IKB_MESSAGE if alert else USER_ALERT_ON_IKB_MESSAGE,
            callback_data=CHANGE_USER_ALERT_CALLBACK_DATA
        )
    )
    ikb.row(InlineKeyboardButton(text=SOCIAL_IKB_MESSAGE, callback_data=SOCIAL_CALLBACK_DATA))
    ikb.row(InlineKeyboardButton(text=USER_REVIEW_IKB_MESSAGE, callback_data=USER_REVIEW_CALLBACK_DATA))
    ikb.row(InlineKeyboardButton(text=PAYMENT_IKB_MESSAGE, callback_data=PAYMENT_CALLBACK_DATA))

    return ikb
