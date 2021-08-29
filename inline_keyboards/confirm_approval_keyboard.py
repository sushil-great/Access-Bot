from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def confirm_approval_keyboard(chat_id: int, email: str, confirmer_id: int):

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text="Yes, Approve ✔️",
                callback_data=f"{chat_id};{email};1;{confirmer_id}"
            )
        ], [
            InlineKeyboardButton(
                text="Go Back ⬅️",
                callback_data=f"b;a;{chat_id};{email};{confirmer_id}"
            )
        ]
    ])
