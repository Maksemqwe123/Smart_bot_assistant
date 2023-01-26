from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

drinks_name = ['кола', 'пепси', 'фанта']
drinks_size = ['большая', 'средняя', 'маленькая']


class DrinksStates(StatesGroup):
    drinks_name = State()
    drinks_size = State()


async def drinks_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in drinks_name:
        keyboard.add(name.title())

    await message.answer('Выберите Напиток', reply_markup=keyboard)
    await state.set_state(DrinksStates.drinks_name.state)


async def drinks_chose(message: types.Message, state: FSMContext):
    if message.text.lower() not in drinks_name:
        await message.answer('Пожалуйста, выберите напиток, используя клавиатуру ниже')
        return

    """
    {chosen_food: 'пицца'}
    """

    await state.update_data(chosen_food=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in drinks_size:
        keyboard.add(size)

    await message.answer('Выберите размер напитка', reply_markup=keyboard)
    await state.set_state(DrinksStates.drinks_size.state)


async def drinks_size_chose(message: types.Message, state: FSMContext):
    if message.text.lower() not in drinks_size:
        await message.answer('Пожалуйста, выберите размер напитка, используя клавиатуру ниже')
        return

    user_data = await state.get_data()
    drinks = user_data.get('chosen_food')
    drinks_size_1 = message.text

    await message.answer(f'Вы заказали {drinks}. Порция размером {drinks_size_1}', reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_drinks(dp: Dispatcher):
    dp.register_message_handler(drinks_start, commands='drinks', state='*')
    dp.register_message_handler(drinks_chose, state=DrinksStates.drinks_name)
    dp.register_message_handler(drinks_size_chose, state=DrinksStates.drinks_size)
