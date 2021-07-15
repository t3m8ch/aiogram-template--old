from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Command
from dependency_injector.wiring import Provide, inject

from bot import di
from bot.service.random_numbers import RandomNumbersService
from bot.utils import Router

router = Router()


# -------- /rnd ---------
@router.message(Command(["rnd", "random"]))
@inject
async def cmd_random_number(message: types.Message,
                            random_numbers_service: RandomNumbersService
                            = Provide[di.Container.random_numbers_service]):
    await message.reply(str(random_numbers_service.generate_random_number()))


# -------- /start --------
@router.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.reply("Hello!")


# -------- echo --------
@router.message()
async def echo(message: types.Message):
    await message.reply(message.text)
