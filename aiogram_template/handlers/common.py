from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart


# -------- /start --------
def register_cmd_start(dp: Dispatcher):
    dp.register_message_handler(cmd_start, CommandStart())


async def cmd_start(message: types.Message):
    await message.reply("Hello!")


# -------- echo --------
def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)


async def echo(message: types.Message):
    await message.reply(message.text)


handlers = [
    register_cmd_start,
    register_echo
]
