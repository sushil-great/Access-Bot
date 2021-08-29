from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from helpers.google_group import get_google_group_member


def approved_keyboard(email: str):

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="Approved ✅",
                url=get_google_group_member(email)
            )
        ]
    ])
