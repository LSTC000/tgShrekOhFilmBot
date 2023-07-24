from aiogram.dispatcher.filters.state import StatesGroup, State


class PaymentStatesGroup(StatesGroup):
    payment_menu = State()
    enter_yoomoney_payment_amount = State()
