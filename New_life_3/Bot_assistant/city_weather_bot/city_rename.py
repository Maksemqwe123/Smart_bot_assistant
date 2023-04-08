# -*- coding: utf-8 -*-

from aiogram.dispatcher import FSMContext

from aiogram import types

from buttons_bot.buttons import *

location_city_name = []


async def rename_leisure_city(message: types.Message, state: FSMContext):
    if message.text == 'Гомель':
        location_city_name.append('gomel')

        await message.answer('Можно сходить в кино/театр,🎥🎭 можно весело провести время катаясь на коньках.⛸️'
                             'В холодную погоду не помешает выпить кофе/чая.☕🍵 Также можно пройтись по прекрасному парку,🌅'
                             'а в конце вечера можно сходить покушать пиццы🍕', reply_markup=help_assistant_street)

        await state.finish()

    elif message.text == 'Минск':
        location_city_name.append('minsk')

        await message.answer('Можно сходить в кино/театр,🎥🎭 можно весело провести время катаясь на коньках.⛸️'
                             'В холодную погоду не помешает выпить кофе/чая.☕🍵 Также можно пройтись по прекрасному парку,🌅'
                             'а в конце вечера можно сходить покушать пиццы🍕', reply_markup=help_assistant_street)

        await state.finish()

    elif message.text == 'Брест':
        location_city_name.append('brest')

        await message.answer('Можно сходить в кино/театр,🎥🎭 можно весело провести время катаясь на коньках.⛸️'
                             'В холодную погоду не помешает выпить кофе/чая.☕🍵 Также можно пройтись по прекрасному парку,🌅'
                             'а в конце вечера можно сходить покушать пиццы🍕', reply_markup=help_assistant_street)

        await state.finish()

    elif message.text == 'Витебск':
        location_city_name.append('vitebsk')

        await message.answer('Можно сходить в кино/театр,🎥🎭 можно весело провести время катаясь на коньках.⛸️'
                             'В холодную погоду не помешает выпить кофе/чая.☕🍵 Также можно пройтись по прекрасному парку,🌅'
                             'а в конце вечера можно сходить покушать пиццы🍕', reply_markup=help_assistant_street)

        await state.finish()

    elif message.text == 'Могилёв':
        location_city_name.append('mogilev')

        await message.answer('Можно сходить в кино/театр,🎥🎭 можно весело провести время катаясь на коньках.⛸️'
                             'В холодную погоду не помешает выпить кофе/чая.☕🍵 Также можно пройтись по прекрасному парку,🌅'
                             'а в конце вечера можно сходить покушать пиццы🍕', reply_markup=help_assistant_street)

        await state.finish()

    elif message.text == 'Гродно':
        location_city_name.append('grodno')

        await message.answer('Можно сходить в кино/театр,🎥🎭 можно весело провести время катаясь на коньках.⛸️'
                             'В холодную погоду не помешает выпить кофе/чая.☕🍵 Также можно пройтись по прекрасному парку,🌅'
                             'а в конце вечера можно сходить покушать пиццы🍕', reply_markup=help_assistant_street)

        await state.finish()

    else:
        await message.answer('Извините, но я вас не понимаю, воспользуйтесь клавиатурой ниже')