import logging
from os import getenv
from typing import List, NamedTuple, Union, Optional

from aiogram_template.errors import PortMustBeNumberError


class LongPollingUpdateMethod:
    pass


class WebhookUpdateMethod(NamedTuple):
    host: str
    path: str
    webapp_host: str
    webapp_port: int

    @property
    def url(self) -> str:
        # It would be possible to apply the Path class from pathlib.
        # However, it doesn't fit:

        #   >>> from pathlib import Path
        #   >>> Path("localhost", "/path/to/bot")
        #   Path("/path/to/bot")

        # It would be possible to use a URL class from a third-party library called urlpath.
        # However, that doesn't fit either:

        #   >>> from urlpath import URL
        #   >>> URL("localhost", "/path/to/bot")
        #   URL("/path/to/bot")

        host = self.host[:-1] if self.host[-1] == "/" else self.host
        path = self.path[1:] if self.path[0] == "/" else self.path
        return host + "/" + path


UpdateMethodType = Union[LongPollingUpdateMethod, WebhookUpdateMethod]


class TgConfig(NamedTuple):
    token: str
    admins_id: List[int]
    update_method: UpdateMethodType
    parse_mode: str


class LogConfig(NamedTuple):
    level: int
    format: str


class Config(NamedTuple):
    telegram: TgConfig
    logging: LogConfig


def get_token() -> str:
    tg_token = getenv("TG_TOKEN")
    assert tg_token is not None, "TG_TOKEN is not set"
    return tg_token


def get_admins_id() -> List[int]:
    admins_id = getenv("ADMINS_ID")
    assert admins_id is not None, "ADMINS_ID is not set"

    admins_id = admins_id.split(",")
    for id in admins_id:
        assert id.isnumeric(), "ADMINS_ID must be a number"

    return list(map(int, admins_id))


def get_update_method() -> UpdateMethodType:
    webhook_host = getenv("WEBHOOK_HOST")
    webhook_path = getenv("WEBHOOK_PATH")
    webapp_host = getenv("WEBAPP_HOST")
    webapp_port = getenv("WEBAPP_PORT")

    return _compute_update_method(webhook_host,
                                  webhook_path,
                                  webapp_host,
                                  webapp_port)


def _compute_update_method(webhook_host: Optional[str],
                           webhook_path: Optional[str],
                           webapp_host: Optional[str],
                           webapp_port: Optional[str]) -> UpdateMethodType:
    """A pure function that creates UpdateMethodType. Created for unit testing"""
    if any(env is None for env in (webhook_host,
                                   webhook_path,
                                   webapp_host,
                                   webapp_port)):
        return LongPollingUpdateMethod()

    if not webapp_port.isnumeric():
        raise PortMustBeNumberError()

    webapp_port = int(webapp_port)

    return WebhookUpdateMethod(
        webhook_host,
        webhook_path,
        webapp_host,
        webapp_port
    )


def load_config() -> Config:
    return Config(
        telegram=TgConfig(
            token=get_token(),
            admins_id=get_admins_id(),
            update_method=get_update_method(),
            parse_mode="HTML"
        ),
        logging=LogConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
    )
