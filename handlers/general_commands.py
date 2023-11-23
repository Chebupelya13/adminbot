from config.general_texts import help_text
from misc import dp, bot
from aiogram.types import Message


@dp.message_handler(
    commands='help'
)
async def help(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text=help_text)









