from aiogram.dispatcher.filters.state import StatesGroup, State


class MainMenuStatesGroup(StatesGroup):
    main_menu = State()
    user_review = State()
