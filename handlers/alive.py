import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/30868ddf51d5599e8c777.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝙃𝙚𝙡𝙡𝙤, 𝙄 𝘼𝙢 𝙎𝙪𝙥𝙚𝙧 𝙁𝙖𝙨𝙩 𝙈𝙪𝙨𝙞𝙘 𝙋𝙡𝙖𝙮𝙚𝙧
𝘽𝙤𝙩 𝙁𝙤𝙧 𝙏𝙚𝙡𝙚𝙜𝙧𝙖𝙢 𝙂𝙧𝙤𝙪𝙥𝙨 ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ⚡𝗖𝗵𝗮𝗻𝗻𝗲𝗹⚡ : [𝗧𝗵𝗲 𝗦𝘂𝗽𝗲𝗿𝗶𝗼𝘂𝗿 𝗡𝗲𝘁𝘄𝗼𝗿𝗸](https://t.me/The_Superiour_Network)
┣★ ⚡𝗦𝘂𝗽𝗽𝗼𝗿𝘁⚡ : [𝐒𝐄𝐂𝐑𝐄𝐓𝐋𝐀𝐍𝐃_𝐗𝐃](https://t.me/SECRETLAND_XD)
┣★ ⚡𝗢𝘄𝗻𝗲𝗿⚡   : [𝐘𝐚𝐬𝐡 𝐑𝐚𝐣](https://t.me/give_up_to_god)
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ ❰ 𝗔𝗱𝗱 𝗠𝗲 𝗜𝗻 𝗚𝗿𝗼𝘂𝗽 ❱ ⚡", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "Yash"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/30868ddf51d5599e8c777.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡𝗦𝘂𝗽𝗽𝗼𝗿𝘁⚡", url=f"https://t.me/SECRETLAND_XD")
                ]
            ]
        ),
    )


@Client.on_message(commandpro(["DarkxMusic","Yash", "#Channel", "@Channel", "/Channel", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/65be304b45005b8bd84db.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡𝗖𝗵𝗮𝗻𝗻𝗲𝗹⚡", url=f"https://t.me/The_Superiour_Network")
                ]
            ]
        ),
    )
