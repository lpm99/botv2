import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

TELEGRAM_BOT_TOKEN = os.getenv('TOKEN')

DATABASE_URL = os.getenv('DB_URL')

CARD_INFO = os.getenv('CARD_INFO')

ADMIN_IDS = [int(admin_id) for admin_id in os.getenv('ADMIN_IDS').split(',')]
