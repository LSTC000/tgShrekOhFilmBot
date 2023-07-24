from data.redis import LAST_IKB_REDIS_KEY

from data.messages import SOCIAL_MENU_MESSAGE

from keyboards import social_ikb

from loader import bot

from aiogram.dispatcher.storage import FSMContext


async def call_social_ikb(user_id: int, state: FSMContext) -> None:
    """
    :param user_id: Telegram user id.
    :param state: FSMContext.
    :return: None.
    """

    async with state.proxy() as data:
        # Call social inline menu.
        msg = await bot.send_message(
            chat_id=user_id,
            text=SOCIAL_MENU_MESSAGE,
            reply_markup=social_ikb()
        )
        # Remember id of the last inline keyboard.
        data[LAST_IKB_REDIS_KEY] = msg.message_id
