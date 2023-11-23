import os
import re

from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')

SUPER_GROUP = os.environ.get('SUPER_GROUP')
