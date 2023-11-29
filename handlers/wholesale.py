from handlers.post_counter import post_counter
from aiogram.types import Message, ContentType
from misc import dp, bot
import json
from config.censure import bad_expression
import phonenumbers
from config.config import SUPER_GROUP


@dp.message_handler(
    lambda message: message.chat.id == SUPER_GROUP,
    content_types=ContentType.ANY
)
async def filters(message: Message):
    if json.loads(str(message.pin)[38:-2]).get('reply_to_message').get('forum_topic_created').get('name') == 'Отзывы':

        res = await post_counter(message)
        print(res)
        if res is True:
            pass
        else:
            await message.delete()
            try:
                await bot.send_message(
                    text=f'{message.from_user.full_name}, пожалуйста ознакомтесь с правилами размещения объявлений.',
                    chat_id=message.from_user.id
                )
            except:
                await message.answer(
                    text=f'{message.from_user.full_name}, пожалуйста ознакомтесь с правилами размещения объявлений.')

        if len(message.photo) == 0:
            string = message.text
        else:
            string = message.caption

        items = phonenumbers.PhoneNumberMatcher(string, 'RU')
        # items_kz = phonenumbers.PhoneNumberMatcher(string, 'KZ')

        if len(message.photo) == 0:
            for i in message.text.split(' '):

                if i.lower() in bad_expression:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения',
                            chat_id=message.from_user.id)
                    except:
                        await message.answer(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения')

                elif message.text.lower() in bad_expression:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения',
                            chat_id=message.from_user.id)
                    except:
                        await message.answer(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения')
            try:
                items.next()
                # items_kz.next()
                await message.delete()
                try:
                    await bot.send_message(
                        text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки\n',
                        chat_id=message.from_user.id
                    )
                except:
                    await message.answer(
                        text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки')

            except:
                if 'http' in message.text:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки\n',
                            chat_id=message.from_user.id
                        )
                    except:
                        await message.answer(
                            text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки')

        else:
            for i in message.caption.split(' '):

                if i.lower() in bad_expression:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения',
                            chat_id=message.from_user.id)
                    except:
                        await message.answer(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения')

                elif message.caption.lower() in bad_expression:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения',
                            chat_id=message.from_user.id)
                    except:
                        await message.answer(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения')


            try:
                items.next()
                # items_kz.next()
                await message.delete()
                try:
                    await bot.send_message(
                        text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки\n',
                        chat_id=message.from_user.id
                )
                except:
                    await message.answer(text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки')

            except:
                if 'http' in message.caption:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки\n',
                            chat_id=message.from_user.id
                        )
                    except:
                        await message.answer(text=f'{message.from_user.full_name}, в этом чате нельзя отправлять номера телефонов и ссылки')



    else:
        if len(message.photo) == 0:
            for i in message.text.split(' '):

                if i.lower() in bad_expression:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения',
                            chat_id=message.from_user.id)
                    except:
                        await message.answer(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения')

                elif message.text.lower() in bad_expression:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения',
                            chat_id=message.from_user.id)
                    except:
                        await message.answer(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения')
        else:
            for i in message.caption.split(' '):

                if i.lower() in bad_expression:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения',
                            chat_id=message.from_user.id)
                    except:
                        await message.answer(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения')

                elif message.caption.lower() in bad_expression:
                    await message.delete()
                    try:
                        await bot.send_message(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения',
                            chat_id=message.from_user.id)
                    except:
                        await message.answer(
                            text=f'{message.from_user.full_name}, в этом чате запрещено употреблять такие выражения')
