import logging
from os import getenv
from typing import List, NamedTuple


class TgConfig(NamedTuple):
    token: str
    admins_id: List[int]
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


def load_config() -> Config:
    return Config(
        telegram=TgConfig(
            token=get_token(),
            admins_id=get_admins_id(),
            parse_mode="HTML"
        ),
        logging=LogConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
    )
