from handlers.post_counter import post_counter
from aiogram.types import Message
from misc import dp
import json
from config.censure import bad_expression
import phonenumbers


@dp.message_handler(
    lambda message:
    json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get('name') == 'Общение'
    or
    json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get(
        'name') == 'Розничная продажа'
    or
    json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get(
        'name') == 'Оптовые продажи'
)
async def filters(message: Message):
    for i in message.text.split(' '):

        if i.lower() in bad_expression:
            await message.delete()
            await message.answer(f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения')

    if json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get(
            'name') == 'Оптовые продажи':
        string = message.text
        items = phonenumbers.PhoneNumberMatcher(string, 'RU')
        items_kz = phonenumbers.PhoneNumberMatcher(string, 'KZ')

        try:
            items.next()
            items_kz.next()
            await message.delete()
            await message.answer(
                f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки\n')

        except:
            if 'http' in message.text:
                await message.delete()
                await message.answer(
                    f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки\n')

            else:
                res = await post_counter(message)
                if res is True:
                    pass
                else:
                    await message.delete()
                    await message.answer(
                        f'{message.from_user.full_name}, пожалуйста ознакомтесь с правилами размещения объявлений.')
