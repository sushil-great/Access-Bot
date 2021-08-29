from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def no_request_keyboard(chat_id: int, email: str, message_id: int):

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="No Req Found ❌",
                    callback_data="gr-msg"
                ),
                InlineKeyboardButton(
                    text="◀️ Undo",
                    callback_data=f"u;{message_id};{chat_id};{email}"
                )
            ]
        ]
    )
