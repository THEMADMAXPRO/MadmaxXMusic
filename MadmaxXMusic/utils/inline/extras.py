from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_9"], url=SUPPORT_CHAT),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
            InlineKeyboardButton(text="ᴧᴅᴅ ᴛʜɪs ʙσᴛ ɪɴ ʏσᴜʀ ɢʀσᴜᴘ", url="https://t.me/{app.username}?startgroup=true"),
        ],
    ]
    return buttons


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl


def supp_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["S_B_9"],
                    url=SUPPORT_CHAT,
                ),
            ]
        ]
    )
    return upl

def add_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(text="ᴧᴅᴅ ᴛʜɪs ʙσᴛ ɪɴ ʏσᴜʀ ɢʀσᴜᴘ", url="https://t.me/{app.username}?startgroup=true"),
           ],
        ]
    )
    return upl
