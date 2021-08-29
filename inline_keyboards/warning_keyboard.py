from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def warning_keyboard():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="❌ Warning ❌",
                callback_data="warn-msg"
            )
        ]
    ])
