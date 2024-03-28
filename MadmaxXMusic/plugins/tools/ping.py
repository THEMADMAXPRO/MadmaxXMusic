from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from MadmaxXMusic import app
from MadmaxXMusic.core.call import Madmax
from MadmaxXMusic.utils import bot_sys_stats
from MadmaxXMusic.utils.decorators.language import language
from MadmaxXMusic.utils.inline import supp_markup
from config import BANNED_USERS, PING_IMG_URL


@app.on_message(filters.command(["ping", "alive"]) & ~BANNED_USERS)
@language
async def ping_com(client, message: Message, _):
    start = datetime.now()
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"].format(app.mention),
    )
    pytgping = await Madmax.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(resp, app.mention, UP, RAM, CPU, DISK, pytgping),
        reply_markup=InlineKeyboardMarkup(
            [
               [ 
                   InlineKeyboardButton(
                       text= "ᴀᴅᴅ ˹ᴇᴍᴍᴀ ✘ ᴍᴜsɪᴄ˼ ♪ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ", url="https://t.me/emma_musicop_bot?startgroup=true"
                   )
               ]
                [
                    InlineKeyboardButton(
                        text="sᴜᴩᴩᴏʀᴛ", url="https://t.me/voiceofheart0"
                    ),
                    InlineKeyboardButton(
                        text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/THEMADMAXPRO/MadmaxXMusic"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        text="ᴜᴘᴅᴀᴛᴇ", url="https://t.me/STATUSDAIRY2"
                    ),
                    InlineKeyboardButton(
                        text="ᴄʟᴏsᴇ", callback_data=f"close"
                    ),
                ]
            ]
        ),
    )
