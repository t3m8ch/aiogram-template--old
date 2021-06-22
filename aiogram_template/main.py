import asyncio
import logging

import dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from aiogram_template.handlers import register_handlers
from aiogram_template import config


async def run_async():
    # Get config
    dotenv.load_dotenv()
    cfg = config.load_config()

    # Logging configuration
    logging.basicConfig(
        level=cfg.logging.level,
        format=cfg.logging.format
    )
    logging.warning("START BOT!")

    # Base
    storage = MemoryStorage()  # TODO: Redis
    bot = Bot(
        token=cfg.telegram.token,
        parse_mode=cfg.telegram.parse_mode
    )
    dp = Dispatcher(bot, storage=storage)

    # Register
    register_handlers(dp)

    # Start bot!
    try:
        await dp.start_polling()  # TODO: Webhook
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


def run():
    try:
        asyncio.run(run_async())
    except (KeyboardInterrupt, SystemExit):
        logging.warning("BOT STOPPED!")


if __name__ == "__main__":
    run()
