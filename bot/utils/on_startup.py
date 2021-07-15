from aiogram import Dispatcher
from dependency_injector.wiring import Provide

import logging as log

from bot import di
from bot.utils.config import UpdateMethod, Config


async def on_startup(dp: Dispatcher,
                     config: Config = Provide[di.Container.config]):
    if config.tg_update_method == UpdateMethod.WEBHOOKS:
        if config.ssl_is_set:
            with open(config.ssl_certificate_path, 'rb') as file:
                ssl_certificate = file.read()
        else:
            ssl_certificate = None

        await dp.bot.set_webhook(
            url=config.tg_webhook_url,
            certificate=ssl_certificate
        )

    log.warning("START BOT!")
