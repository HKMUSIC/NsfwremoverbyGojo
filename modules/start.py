# Copyright 2024 Qewertyy, MIT License

from pyrogram import Client, filters, types as t
from bot import StartTime

startText = """
An AntiNSFW bot Powered by @thedrxnet to protect your groups from NSFW content.
"""

@Client.on_message(filters.command(["start","help","repo","source"]))
async def start(_: Client, m: t.Message):
    await m.reply_text(
        startText,
        reply_markup=t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(text="˹sᴜᴘᴘᴏʀᴛ˼",url="https://t.me/Hehe_Stalker")
                ]
            ]
        )
    )
