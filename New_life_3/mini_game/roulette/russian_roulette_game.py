# -*- coding: utf-8 -*-

import random

from aiogram import types
from New_life_3.mini_game.buttons import *

from aiogram.dispatcher.filters.state import StatesGroup, State

from aiogram.dispatcher import FSMContext


revolver_drum = [1, 1, 1, 1, 1, 1]
count_shoot = 0


class RussianRoulette(StatesGroup):
    drum_roulette = State()
    shoot = State()


async def play_game(message: types.Message):
    await message.answer('Хочешь сыграть в русскую рулетку с надоедливым Джони⁉️')

    await message.answer('В барабане 6 пуль, сколько хочешь оставить❓😈☠️', reply_markup=number_bullets)

    await RussianRoulette.drum_roulette.set()


async def drum_number(message: types.Message):

    if int(message.text) == 1:
        revolver_drum.clear()
        revolver_drum.extend([0, 1, 0, 0, 0, 0])

    elif int(message.text) == 2:
        revolver_drum.clear()
        revolver_drum.extend([0, 1, 0, 1, 0, 0])

    elif int(message.text) == 3:
        revolver_drum.clear()
        revolver_drum.extend([0, 1, 0, 1, 0, 1])

    elif int(message.text) == 4:
        revolver_drum.clear()
        revolver_drum.extend([0, 1, 0, 1, 1, 1])

    elif int(message.text) == 5:
        revolver_drum.clear()
        revolver_drum.extend([0, 1, 1, 1, 1, 1])

    await message.answer('В барабане %d пули, ещё не поздно уйти😖 или хочешь продолжить❓☠️\n' % int(message.text), reply_markup=russian_game)
    # if message.text == 'продолжить':


async def random_shoot(message: types.Message, state: FSMContext):
    global count_shoot
    random_index = random.randrange(len(revolver_drum))
    user_shoot = revolver_drum[random_index]
    bot_player = revolver_drum[random_index]
    if count_shoot != 0:
        revolver_drum.append(message.text)
        if revolver_drum[6] == 'крутить🔫':
            if user_shoot == 1:
                await message.answer(f'Ты умер☠️ {count_shoot + 1} выстрел стал для тебя последним😵‍💫😬', reply_markup=user_game)
                count_shoot -= count_shoot
                await state.finish()

            elif user_shoot == 0 and bot_player == 0:
                await message.answer('Вам повезло, в этот раз выстрел был холостым😮‍💨 \nНо сможешь ли ты ещё раз нажать на курок❓🫣😵')
                await message.answer('Крутить барабан или сделать выстрел❓🧐\n', reply_markup=shoot_twist)

                count_shoot += 1

            elif bot_player == 1:
                await message.answer(f'Ты победил😎, для Джони {count_shoot + 1} выстрел оказался последним🤕', reply_markup=user_game)
                count_shoot -= count_shoot

                await state.finish()

        elif revolver_drum[6] == 'выстрелить😈':
            if random_index != 5:
                user_shoot = revolver_drum[random_index + 1]
                if user_shoot == 1:
                    await message.answer(f'Ты умер☠️ {count_shoot + 1} выстрел стал для тебя последним😵‍💫😬', reply_markup=user_game)
                    await message.answer('В этот раз нужно было прокрутить барабан🤕')
                    count_shoot -= count_shoot

                    await state.finish()

                elif user_shoot == 0 and bot_player == 0:
                    await message.answer(
                        'Вам повезло, в этот раз выстрел был холостым😮‍💨 \nНо сможешь ли ты ещё раз нажать на курок❓🫣😵')
                    await message.answer('Крутить барабан или сделать выстрел❓🧐\n', reply_markup=shoot_twist)

                    count_shoot += 1

                elif bot_player == 1:
                    await message.answer(f'Ты победил😎, для Джони {count_shoot + 1} выстрел оказался последним😵‍💫😬', reply_markup=user_game)
                    count_shoot -= count_shoot

                    await state.finish()

            elif random_index == 5:
                user_shoot = revolver_drum[1]
                if user_shoot == 1:
                    await message.answer(f'Ты умер☠️ {count_shoot + 1} выстрел стал для тебя последним😵‍💫😬',
                                         reply_markup=user_game)
                    await message.answer('В этот раз нужно было прокрутить барабан🤕')
                    count_shoot -= count_shoot

                    await state.finish()

                elif user_shoot == 0 and bot_player == 0:
                    await message.answer(
                        'Вам повезло, в этот раз выстрел был холостым😮‍💨 \nНо сможешь ли ты ещё раз нажать на курок❓🫣😵')
                    await message.answer('Крутить барабан или сделать выстрел❓🧐\n', reply_markup=shoot_twist)

                    count_shoot += 1

                elif bot_player == 1:
                    await message.answer(f'Ты победил😎, для Джони {count_shoot + 1} выстрел оказался последним😵‍💫😬', reply_markup=user_game)
                    count_shoot -= count_shoot

                    await state.finish()

        revolver_drum.pop(6)
    else:
        if user_shoot == 1:
            await message.answer(f'Ты умер☠️ {count_shoot + 1} выстрел стал для тебя последним😵‍💫😬', reply_markup=user_game)
            count_shoot -= count_shoot

            await state.finish()

        elif user_shoot == 0 and bot_player == 0:
            await message.answer(
                'Вам повезло, в этот раз выстрел был холостым😮‍💨 \nНо сможешь ли ты ещё раз нажать на курок❓🫣😵')
            await message.answer('Крутить барабан или сделать выстрел❓🧐\n', reply_markup=shoot_twist)

            count_shoot += 1

        elif bot_player == 1:
            await message.answer(f'Ты победил😎, для Джони {count_shoot + 1} выстрел оказался последним😵‍💫😬', reply_markup=user_game)
            count_shoot -= count_shoot

            await state.finish()
