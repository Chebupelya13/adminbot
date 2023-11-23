import sqlite3 as sq
from aiogram.types import Message
import datetime


async def post_counter(message: Message):
    with (sq.connect('users.db') as db):
        cur = db.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users(
        id INT,
        date_for_post TEXT
        )''')
        cur.execute(f'''SELECT * FROM users WHERE id = {message.from_user.id}''')

        data = cur.fetchall()

        if len(data) != 0 and str(datetime.datetime.now() - datetime.datetime.strptime(data[0][1], '%Y-%m-%d %H:%M:%S.%f'))[0] != '-':
            cur.execute(f'''UPDATE users SET date_for_post = "{datetime.datetime.now() + datetime.timedelta(days=1)}" WHERE id = {message.from_user.id}''')
            return True

        elif len(data) != 0:
            return False

        elif len(data) == 0:
            cur.execute(f'''INSERT INTO users VALUES({message.from_user.id}, "{datetime.datetime.now() + datetime.timedelta(days=1)}")''')
            return True




