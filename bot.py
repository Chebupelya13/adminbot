from aiogram import executor
from misc import dp
import handlers


async def on_startup(_):
    print('Bot is working...')


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
