#!/usr/bin/env python3
import os
import sys
import time

from dotenv import load_dotenv
from pathlib import Path
from telethon import TelegramClient

class BotAssistant():

    def __init__(self, target_chat, api_id, api_hash, bot_token):
        client = TelegramClient("db/bot_assistant", api_id, api_hash)
        assert client.connect()

        client.sign_in(bot_token=bot_token)

        self.client = client
        self.target_chat = target_chat

    def notify_message_deletion(self, message, file=None):
        self.client.send_message(self.target_chat, message,file=file)