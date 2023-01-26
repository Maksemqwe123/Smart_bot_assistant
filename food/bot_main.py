import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from food.app.config_reader import load_config
from food.app.handler.common import register_handlers_common
from app.handler import food_handlers, drinks_handlers

logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command='/start', description='Начало работы'),
        BotCommand(command='/food', description='Выбор еды'),
        BotCommand(command='/drinks', description='Выбор напитков'),
        BotCommand(command='/cancel', description='Отмена')
    ]

    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logger.info('Starting bot')

    config = load_config(r'C:\Users\makce\PycharmProjects\pythonProject\food\config\bot_config.ini')

    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    register_handlers_common(dp)
    food_handlers(dp)
    drinks_handlers(dp)

    await set_commands(bot)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
