import asyncio

from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    event_loop = providers.Singleton(asyncio.get_event_loop)
