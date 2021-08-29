from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def confirm_no_request_keyboard(chat_id: int, email: str, confirmer_id: int):

    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Yes, No Req Found ✔️",
                    callback_data=f"gr;{chat_id};{email};1;{confirmer_id}"
                )
            ], [
                InlineKeyboardButton(
                    text="Go Back ⬅️",
                    callback_data=f"b;gr;{chat_id};{email};{confirmer_id}"
                )
            ]
        ]
    )
