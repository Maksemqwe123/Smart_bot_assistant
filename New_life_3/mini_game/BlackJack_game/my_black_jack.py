# -*- coding: utf-8 -*-

from aiogram import types
from New_life_3.mini_game.buttons import *

from aiogram.dispatcher.filters.state import StatesGroup, State

from aiogram.dispatcher import FSMContext


import random

cards_user_list = [0]
cards_bot_list = [0]

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'] * 4


class BJGame(StatesGroup):
    black_jack_game = State()


async def start_play_black_jack_game(message: types.Message):
    random.shuffle(deck)
    await message.answer('Игра в BlackJack началась♠️♣️♥️♦️')
    await message.answer(
        'В блэкджеке десятки, валеты, дамы и короли стоят по 10 очков.\nТуз может стоить 1 или 11 очков')
    await message.answer('Будете брать карту?♠️♥️', reply_markup=black_jack_game)

    await BJGame.black_jack_game.set()


async def message_user(message: types.Message):
    if cards_user_list[0] > 21 and cards_bot_list[0] > 21 and cards_bot_list[0] == cards_user_list[0]:
        return await message.answer(f'Ничья🤝 \nУ вас {cards_user_list[0]} очков, у крупье {cards_bot_list[0]} очков', reply_markup=user_game)

    elif cards_user_list[0] > 21 and cards_bot_list[0] > 21 and cards_bot_list[0] > cards_user_list[0]:
        return await message.answer(f'Вы победили🎉🎊 \nУ вас {cards_user_list[0]} очков, у крупье {cards_bot_list[0]} очков', reply_markup=user_game)

    elif cards_user_list[0] > 21 and cards_bot_list[0] > 21 and cards_bot_list[0] < cards_user_list[0]:
        return await message.answer(f'Вы проиграли😞 \nУ вас {cards_user_list[0]} очков, у крупье {cards_bot_list[0]} очков', reply_markup=user_game)

    elif cards_bot_list[0] == 21 or cards_user_list[0] > 21:
        return await message.answer(f'Вы проиграли😞 \nУ вас {cards_user_list[0]} очков, у крупье {cards_bot_list[0]} очков', reply_markup=user_game)

    elif cards_bot_list[0] > 21 or cards_user_list[0] == 21:
        return await message.answer(f'Вы победили🎉🎊 \nУ вас {cards_user_list[0]} очков, у крупье {cards_bot_list[0]} очков', reply_markup=user_game)

    else:
        return message.text


async def play_bot(message: types.Message):
    if cards_user_list[0] < 21 and cards_bot_list[0] < 21 and cards_user_list[0] > cards_bot_list[0]:
        return await message.answer(f'Вы победили🎉🎊 \nУ вас {cards_user_list[0]} очков, у крупье {cards_bot_list[0]} очков', reply_markup=user_game)

    elif cards_user_list[0] < 21 and cards_bot_list[0] < 21 and cards_user_list[0] < cards_bot_list[0]:
        return await message.answer(f'Вы проиграли😞 \nУ вас {cards_user_list[0]} очков, у крупье {cards_bot_list[0]} очков', reply_markup=user_game)

    elif cards_user_list[0] < 21 and cards_bot_list[0] < 21 and cards_user_list[0] == cards_bot_list[0]:
        return await message.answer(f'Ничья🤝 \nУ вас {cards_user_list[0]} очков, у крупье {cards_bot_list[0]} очков', reply_markup=user_game)

    elif cards_bot_list[0] > 21:
        return await message.answer(f'Вы победили🎉🎊 \nУ вас {cards_user_list[0]} очков, у крупье {cards_bot_list[0]} очков', reply_markup=user_game)


async def play_game_black_jack(message: types.Message, state: FSMContext):
    text_user = await message_user(message)
    cards_user_list.append(text_user)

    if cards_user_list[1] == 'Взять карту♣️♥️':
        cards_user = random.choice(deck)
        bot_list = random.choice(deck)

        if type(cards_user) is int:
            cards_user_list[0] += cards_user
            await message.answer(f'Вам попалась карта♣️ {cards_user}. У вас {cards_user_list[0]} очков.')

        elif cards_user == 'Ace':
            if cards_user_list[0] <= 10:
                cards_user_list[0] += 11
                await message.answer(f"Вам попалась карта♥️ 'Ace'. У вас {cards_user_list[0]} очков.")
            else:
                cards_user_list[0] += 1
                await message.answer(f"Вам попалась карта♥️ 'Ace'. У вас {cards_user_list[0]} очков.")

        elif cards_user == 'Jack':
            cards_user_list[0] += 10
            await message.answer(f"Вам попалась карта♦️ 'Jack'. У вас {cards_user_list[0]} очков.")

        elif cards_user == 'King':
            cards_user_list[0] += 10
            await message.answer(f"Вам попалась карта♠️ 'King'. У вас {cards_user_list[0]} очков.")

        elif cards_user == 'Queen':
            cards_user_list[0] += 10
            await message.answer(f"Вам попалась карта♣️ 'Queen'. У вас {cards_user_list[0]} очков.")

        if cards_bot_list[0] <= 18:
            if type(bot_list) is int:
                cards_bot_list[0] += bot_list
                await message.answer(f"Крупье попалась карта♣️ '{bot_list}'. У крупье {cards_bot_list[0]} очков.")

            elif bot_list == 'Ace':
                if cards_bot_list[0] <= 10:
                    cards_bot_list[0] += 11
                    await message.answer(f"Крупье попалась карта♥️ 'Ace'. У крупье {cards_bot_list[0]} очков.")

                else:
                    cards_bot_list[0] += 1
                    await message.answer(f"Крупье попалась карта♥️ 'Ace'. У крупье {cards_bot_list[0]} очков.")

            elif bot_list == 'Jack':
                cards_bot_list[0] += 10
                await message.answer(f"Крупье попалась карта♦️ 'Jack'. У крупье {cards_bot_list[0]} очков.")

            elif bot_list == 'King':
                cards_bot_list[0] += 10
                await message.answer(f"Крупье попалась карта♠️ 'King'. У крупье {cards_bot_list[0]} очков.")

            elif bot_list == 'Queen':
                cards_bot_list[0] += 10
                await message.answer(f"Крупье попалась карта♣️ 'Queen'. У крупье {cards_bot_list[0]} очков.")
            # if cards_bot_list[0] < 21 or cards_user_list[0] < 0:
            #     await message.answer('Будете брать карту? y/n\n')

        if cards_user_list[0] < 21 and cards_bot_list[0] < 21:
            await message.answer('Будете брать карту?♠️♥️', reply_markup=black_jack_game)
            cards_user_list.pop(1)

        else:
            await message_user(message)

            cards_user_list.clear()
            cards_bot_list.clear()

            cards_bot_list.append(0)
            cards_user_list.append(0)

            await state.finish()

    elif cards_user_list[1] == 'Хватит⛔️':
        while True:
            bot_list = random.choice(deck)
            if cards_bot_list[0] <= 18:
                if type(bot_list) is int:
                    cards_bot_list[0] += bot_list
                    await message.answer(f"Крупье попалась карта♣️ '{bot_list}'. У крупье {cards_bot_list[0]} очков.")

                elif bot_list == 'Ace':
                    if cards_bot_list[0] <= 10:
                        cards_bot_list[0] += 11
                        await message.answer(f"Крупье попалась карта♥️ 'Ace'. У крупье {cards_bot_list[0]} очков.")

                    else:
                        cards_bot_list[0] += 1
                        await message.answer(f"Крупье попалась карта♥️ 'Ace'. У крупье {cards_bot_list[0]} очков.")

                elif bot_list == 'Jack':
                    cards_bot_list[0] += 10
                    await message.answer(f"Крупье попалась карта♦️ 'Jack'. У крупье {cards_bot_list[0]} очков.")

                elif bot_list == 'King':
                    cards_bot_list[0] += 10
                    await message.answer(f"Крупье попалась карта♠️ 'King'. У крупье {cards_bot_list[0]} очков.")

                elif bot_list == 'Queen':
                    cards_bot_list[0] += 10
                    await message.answer(f"Крупье попалась карта♣️ 'Queen'. У крупье {cards_bot_list[0]} очков.")

            else:
                await play_bot(message)

                cards_user_list.clear()
                cards_bot_list.clear()

                cards_bot_list.append(0)
                cards_user_list.append(0)

                await state.finish()
                break

    elif cards_user_list[1] == 'Другие игры🎲🕹🎰':
        await message.answer('Другие наши игры🎲🕹🎰', reply_markup=user_game)

        cards_user_list.clear()
        cards_bot_list.clear()

        cards_bot_list.append(0)
        cards_user_list.append(0)

        await state.finish()

    else:
        await message.answer('Извините, но я вас не понимаю, воспользуйтесь меню панели ниже🔽')
        cards_user_list.pop(1)
