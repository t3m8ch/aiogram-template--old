import asyncio

from dependency_injector import containers, providers

from bot.service.random_numbers import RandomNumbersService
from bot.utils.config import Config


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(
        Config,
        _env_file=".env",
        _env_file_encoding="utf-8"
    )

    event_loop = providers.Singleton(asyncio.get_event_loop)

    random_numbers_service = providers.Factory(RandomNumbersService)
