from handlers.post_counter import post_counter
from aiogram.types import Message
from misc import dp, bot
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
        'name') == 'Отзывы'
    # or
    # json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get(
    #     'name') == 'Мошенники'
    or
    json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get(
        'name') == 'Новости'
    or
    json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get(
        'name') == 'Продать'
    or
    json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get(
        'name') == 'Продажа Б/У товаров'
    or
    json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get(
        'name') == 'Оптовые продажи'
)
async def filters(message: Message):
    for i in message.text.split(' '):

        if i.lower() in bad_expression:
            await message.delete()
            await bot.send_message(text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения', chat_id=message.from_user.id)
        elif message.text.lower() in bad_expression:
            await message.delete()
            await bot.send_message(
                text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения',
                chat_id=message.from_user.id)

    if json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get(
            'name') == 'Отзывы':
        string = message.text
        items = phonenumbers.PhoneNumberMatcher(string, 'RU')
        items_kz = phonenumbers.PhoneNumberMatcher(string, 'KZ')

        try:
            items.next()
            items_kz.next()
            await message.delete()
            await bot.send_message(
                text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки\n',
                chat_id=message.from_user.id
            )

        except:
            if 'http' in message.text:
                await message.delete()
                await bot.send_message(
                    text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки\n',
                    chat_id=message.from_user.id
                )

            else:
                res = await post_counter(message)
                if res is True:
                    pass
                else:
                    await message.delete()
                    await bot.send_message(
                        text=f'{message.from_user.full_name}, пожалуйста ознакомтесь с правилами размещения объявлений.',
                        chat_id=message.from_user.id
                    )
