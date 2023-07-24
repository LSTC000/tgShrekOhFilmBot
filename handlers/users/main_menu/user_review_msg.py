from loader import dp, bot

from data.messages import ERROR_ENTER_USER_REVIEW_MESSAGE, SUCCESSFUL_ENTER_USER_REVIEW_MESSAGE

from database import add_user_review

from functions import call_main_menu_ikb

from states import MainMenuStatesGroup

from utils import Validator

from aiogram import types
from aiogram.dispatcher.storage import FSMContext


@dp.message_handler(state=MainMenuStatesGroup.enter_user_review)
async def user_review_msg(message: types.Message, state: FSMContext) -> None:
    user_id = message.from_user.id
    text = message.text

    # Check review on valid
    if Validator().user_review_validation(text):
        # Add user review in database.
        await add_user_review(user_id=user_id, review=text)
        # Inform the user about a successful entering the review.
        await bot.send_message(chat_id=user_id, text=SUCCESSFUL_ENTER_USER_REVIEW_MESSAGE)
    else:
        # Inform the user about an error when entering the review.
        await bot.send_message(chat_id=user_id, text=ERROR_ENTER_USER_REVIEW_MESSAGE)

    # Call payment inline menu.
    await call_main_menu_ikb(user_id=user_id, state=state)
    # Set main_menu state.
    await MainMenuStatesGroup.main_menu.set()
