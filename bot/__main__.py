import logging as log
import ssl
import sys

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.utils import executor
from dependency_injector.wiring import Provide

from bot import di
from bot.utils.config import UpdateMethod, Config
from bot.utils.on_shutdown import on_shutdown
from bot.utils.on_startup import on_startup
from handlers import register_handlers


def run(di_container: di.Container,
        event_loop=Provide[di.Container.event_loop],
        config: Config = Provide[di.Container.config]):
    # Logging configuration
    log.basicConfig(
        level=log.getLevelName(config.log_level),
        format=config.log_format
    )

    # Storage
    if config.is_redis:
        storage = RedisStorage(
            config.redis_host,
            config.redis_port,
            config.redis_db,
            config.redis_password,
            loop=event_loop
        )
    else:
        storage = MemoryStorage()

    # Base
    bot = Bot(
        token=config.tg_token,
        parse_mode=config.tg_parse_mode
    )
    dp = Dispatcher(bot, storage=storage)

    # Register
    register_handlers(dp, di_container)

    # Start bot!
    if config.tg_update_method == UpdateMethod.LONG_POLLING:
        executor.start_polling(
            dispatcher=dp,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            loop=event_loop,
            skip_updates=config.tg_skip_updates
        )

    elif config.tg_update_method == UpdateMethod.WEBHOOKS:
        if config.ssl_is_set:
            ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
            ssl_context.load_cert_chain(
                config.ssl_certificate_path,
                config.ssl_private_key_path
            )
        else:
            ssl_context = None

        executor.start_webhook(
            dispatcher=dp,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            loop=event_loop,
            webhook_path=config.tg_webhook_path,
            host=config.webapp_host,
            port=config.webapp_port,
            ssl_context=ssl_context,
            skip_updates=config.tg_skip_updates
        )


if __name__ == "__main__":
    _di_container = di.Container()
    _di_container.wire(modules=[sys.modules[__name__]])

    run(_di_container)
