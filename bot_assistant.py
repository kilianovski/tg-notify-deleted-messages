#!/usr/bin/env python3
import os
import sys
import time

from dotenv import load_dotenv
from pathlib import Path
from telethon import TelegramClient

class BotAssistant():

    def __init__(self, target_chat, api_id, api_hash, bot_token):
        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.target_chat = target_chat

    async def notify_message_deletion(self, message, file=None):
        async with TelegramClient("db/bot_assistant", self.api_id, self.api_hash) as client:
            await client.sign_in(bot_token=self.bot_token)
            await client.send_message(self.target_chat, message)