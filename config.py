import os
from telethon import TelegramClient

api_id = os.environ.get('API_ID')
api_hash = os.environ.get('API_HASH')
bot_token = os.environ.get('BOT_TOKEN')
auth_users = os.environ.get('AUTH_USERS').split()
for i in range(len(auth_users)):
    auth_users[i] = int(auth_users[i])

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
