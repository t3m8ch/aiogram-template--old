import asyncio

from dependency_injector import containers, providers

from bot.utils.config import Config


class Container(containers.DeclarativeContainer):
    config = providers.Singleton(
        Config,
        _env_file=".env",
        _env_file_encoding="utf-8"
    )

    event_loop = providers.Singleton(asyncio.get_event_loop)
