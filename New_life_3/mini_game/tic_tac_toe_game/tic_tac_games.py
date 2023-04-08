# -*- coding: utf-8 -*-

from aiogram import types

from New_life_3.mini_game.buttons import *

from aiogram.dispatcher.filters.state import StatesGroup, State

from aiogram.dispatcher import FSMContext

import random


class TicTacGame(StatesGroup):
    tic_tac_user = State()


moves_user = []
moves_bot = []
number = []


async def win_lose(callback_query: types.CallbackQuery, state: FSMContext):
    if empty_field_dict.get(1) == 'X' and empty_field_dict.get(2) == 'X' and empty_field_dict.get(3) == 'X':
        await callback_query.message.answer('Ты победил🎊🎉 \nТы профессионал или это я плохо играю🧐', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(4) == 'X' and empty_field_dict.get(5) == 'X' and empty_field_dict.get(6) == 'X':
        await callback_query.message.answer('Ты победил🎊🎉 \nТы профессионал или это я плохо играю🧐', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(7) == 'X' and empty_field_dict.get(8) == 'X' and empty_field_dict.get(9) == 'X':
        await callback_query.message.answer('Ты победил🎊🎉 \nТы профессионал или это я плохо играю🧐', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(1) == 'X' and empty_field_dict.get(4) == 'X' and empty_field_dict.get(7) == 'X':
        await callback_query.message.answer('Ты победил🎊🎉 \nТы профессионал или это я плохо играю🧐', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(2) == 'X' and empty_field_dict.get(5) == 'X' and empty_field_dict.get(8) == 'X':
        await callback_query.message.answer('Ты победил🎊🎉 \nТы профессионал или это я плохо играю🧐', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(3) == 'X' and empty_field_dict.get(6) == 'X' and empty_field_dict.get(9) == 'X':
        await callback_query.message.answer('Ты победил🎊🎉 \nТы профессионал или это я плохо играю🧐', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(1) == 'X' and empty_field_dict.get(5) == 'X' and empty_field_dict.get(9) == 'X':
        await callback_query.message.answer('Ты победил🎊🎉 \nТы профессионал или это я плохо играю🧐', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(3) == 'X' and empty_field_dict.get(5) == 'X' and empty_field_dict.get(7) == 'X':
        await callback_query.message.answer('Ты победил🎊🎉 \nТы профессионал или это я плохо играю🧐', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    if empty_field_dict.get(1) == '0' and empty_field_dict.get(2) == '0' and empty_field_dict.get(3) == '0':
        await callback_query.message.answer('Ты проиграл😞 \nНо в следующий раз ты точно выиграешь😉', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(4) == '0' and empty_field_dict.get(5) == '0' and empty_field_dict.get(6) == '0':
        await callback_query.message.answer('Ты проиграл😞 \nНо в следующий раз ты точно выиграешь😉', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(7) == '0' and empty_field_dict.get(8) == '0' and empty_field_dict.get(9) == '0':
        await callback_query.message.answer('Ты проиграл😞 \nНо в следующий раз ты точно выиграешь😉', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(1) == '0' and empty_field_dict.get(4) == '0' and empty_field_dict.get(7) == '0':
        await callback_query.message.answer('Ты проиграл😞 \nНо в следующий раз ты точно выиграешь😉', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(2) == '0' and empty_field_dict.get(5) == '0' and empty_field_dict.get(8) == '0':
        await callback_query.message.answer('Ты проиграл😞 \nНо в следующий раз ты точно выиграешь😉', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(3) == '0' and empty_field_dict.get(6) == '0' and empty_field_dict.get(9) == '0':
        await callback_query.message.answer('Ты проиграл😞 \nНо в следующий раз ты точно выиграешь😉', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(1) == '0' and empty_field_dict.get(5) == '0' and empty_field_dict.get(9) == '0':
        await callback_query.message.answer('Ты проиграл😞 \nНо в следующий раз ты точно выиграешь😉', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()

    elif empty_field_dict.get(3) == '0' and empty_field_dict.get(5) == '0' and empty_field_dict.get(7) == '0':
        await callback_query.message.answer('Ты проиграл😞 \nНо в следующий раз ты точно выиграешь😉', reply_markup=user_game)
        empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
        await state.finish()


async def start_tic_tac(callback_query: types.CallbackQuery, state: FSMContext):
    store_buttons_clicked = callback_query.data

    try:
        if int(store_buttons_clicked) == 1 and empty_field_dict.get(1) == ' ':

            empty_field_dict.update({1: 'X'})
            for i in empty_field_dict.items():
                if i[1] == ' ':
                    number.append(i[0])

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

            field_none = random.choice(number)
            number.clear()
            empty_field_dict.update({field_none: '0'})

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

        if int(store_buttons_clicked) == 2 and empty_field_dict.get(2) == ' ':

            empty_field_dict.update({2: 'X'})
            for i in empty_field_dict.items():
                if i[1] == ' ':
                    number.append(i[0])

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

            field_none = random.choice(number)
            number.clear()
            empty_field_dict.update({field_none: '0'})

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

        if int(store_buttons_clicked) == 3 and empty_field_dict.get(3) == ' ':

            empty_field_dict.update({3: 'X'})
            for i in empty_field_dict.items():
                if i[1] == ' ':
                    number.append(i[0])

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

            field_none = random.choice(number)
            number.clear()
            empty_field_dict.update({field_none: '0'})

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

        if int(store_buttons_clicked) == 4 and empty_field_dict.get(4) == ' ':

            empty_field_dict.update({4: 'X'})
            for i in empty_field_dict.items():
                if i[1] == ' ':
                    number.append(i[0])

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

            field_none = random.choice(number)
            number.clear()
            empty_field_dict.update({field_none: '0'})

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

        if int(store_buttons_clicked) == 5 and empty_field_dict.get(5) == ' ':

            empty_field_dict.update({5: 'X'})
            for i in empty_field_dict.items():
                if i[1] == ' ':
                    number.append(i[0])

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

            field_none = random.choice(number)
            number.clear()
            empty_field_dict.update({field_none: '0'})

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

        if int(store_buttons_clicked) == 6 and empty_field_dict.get(6) == ' ':

            empty_field_dict.update({6: 'X'})
            for i in empty_field_dict.items():
                if i[1] == ' ':
                    number.append(i[0])

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

            field_none = random.choice(number)
            number.clear()
            empty_field_dict.update({field_none: '0'})

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

        if int(store_buttons_clicked) == 7 and empty_field_dict.get(7) == ' ':

            empty_field_dict.update({7: 'X'})
            for i in empty_field_dict.items():
                if i[1] == ' ':
                    number.append(i[0])

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

            field_none = random.choice(number)
            number.clear()
            empty_field_dict.update({field_none: '0'})

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

        if int(store_buttons_clicked) == 8 and empty_field_dict.get(8) == ' ':

            empty_field_dict.update({8: 'X'})
            for i in empty_field_dict.items():
                if i[1] == ' ':
                    number.append(i[0])

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

            field_none = random.choice(number)
            number.clear()
            empty_field_dict.update({field_none: '0'})

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

        if int(store_buttons_clicked) == 9 and empty_field_dict.get(9) == ' ':

            empty_field_dict.update({9: 'X'})
            for i in empty_field_dict.items():
                if i[1] == ' ':
                    number.append(i[0])

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

            field_none = random.choice(number)
            number.clear()
            empty_field_dict.update({field_none: '0'})

            await callback_query.message.edit_reply_markup(reply_markup=update_menu(empty_field_dict))

        await win_lose(callback_query, state)

    except IndexError:
        await win_lose(callback_query, state)

        for i in empty_field_dict.items():
            if i[1] != ' ':
                await callback_query.message.answer('Ничья, у меня есть брат близнец🤨', reply_markup=user_game)
                print(empty_field_dict)
                empty_field_dict.update({1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})
                await state.finish()
