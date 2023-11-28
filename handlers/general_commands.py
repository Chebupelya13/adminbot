import json

from misc import dp, bot
from aiogram.types import Message


@dp.message_handler(
    commands='help'
)
async def help(message: Message):
    print('id: ', message.chat.id)
    print('name: ', json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get('name'))
    await message.delete()









