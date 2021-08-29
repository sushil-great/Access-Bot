from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from helpers.google_group import get_google_group_request


def base_keyboard(chat_id: int, email: str):

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="Search Results",
                url=get_google_group_request(email)
            ),
            InlineKeyboardButton(
                text="No Results?",
                callback_data=f"gr;{chat_id};{email};0"
            )
        ], [
            InlineKeyboardButton(
                text="Approve",
                callback_data=f"{chat_id};{email};0"
            )
        ]
    ])
