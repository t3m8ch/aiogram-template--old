import asyncio
import logging

import dotenv
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from aiogram_template.config import LongPollingUpdateMethod, \
    WebhookUpdateMethod, Config

from aiogram_template.handlers import register_handlers
from aiogram_template import config


def on_startup(cfg: Config):
    async def func(dp: Dispatcher):
        update_method = type(cfg.telegram.update_method)
        if update_method == WebhookUpdateMethod:
            await dp.bot.set_webhook(cfg.telegram.update_method.url)

        logging.warning("START BOT!")

    return func


async def on_shutdown(dp: Dispatcher):
    await dp.bot.delete_webhook()

    await dp.storage.close()
    await dp.storage.wait_closed()

    logging.warning("BOT STOPPED!")


def run():
    # Get config
    dotenv.load_dotenv()
    cfg = config.load_config()

    # Logging configuration
    logging.basicConfig(
        level=cfg.logging.level,
        format=cfg.logging.format
    )

    # Base
    event_loop = asyncio.get_event_loop()
    storage = MemoryStorage()  # TODO: Redis
    bot = Bot(
        token=cfg.telegram.token,
        parse_mode=cfg.telegram.parse_mode
    )
    dp = Dispatcher(bot, storage=storage)

    # Register
    register_handlers(dp)

    # Start bot!
    if type(cfg.telegram.update_method) == LongPollingUpdateMethod:
        executor.start_polling(
            dispatcher=dp,
            on_startup=on_startup(cfg),
            on_shutdown=on_shutdown,
            loop=event_loop
        )

    elif type(cfg.telegram.update_method) == WebhookUpdateMethod:
        executor.start_webhook(
            dispatcher=dp,
            on_startup=on_startup(cfg),
            on_shutdown=on_shutdown,
            loop=event_loop,
            webhook_path=cfg.telegram.update_method.webhook_path,
            host=cfg.telegram.update_method.webapp_host,
            port=cfg.telegram.update_method.webapp_port,
        )


if __name__ == "__main__":
    run()
