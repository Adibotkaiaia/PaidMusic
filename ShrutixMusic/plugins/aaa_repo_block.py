from pyrogram import filters
from pyrogram.types import Message
from ShrutixMusic import nand
from config import BANNED_USERS

@nand.on_message(filters.command("repo") & ~BANNED_USERS, group=0)
async def repo_disabled(client, message: Message):
    await message.stop_propagation()
