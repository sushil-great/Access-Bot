from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def banned_message():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="☠️ User Banned ☠️",
                callback_data="banned-msg"
            )
        ]
    ])
