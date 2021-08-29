from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def help_main_keyboard():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                text='Ban',
                callback_data='help-ban'
            ),
            InlineKeyboardButton(
                text='Unban',
                callback_data='help-unban'
            )
        ], [
            InlineKeyboardButton(
                text='Find Mem.',
                callback_data='help-find-mem'
            ),
            InlineKeyboardButton(
                text='Find Req.',
                callback_data='help-find-req'
            )
        ], [
            InlineKeyboardButton(
                text='Purge',
                callback_data='help-purge'
            )
        ], [
            InlineKeyboardButton(
                text='Start',
                callback_data='help-start'
            )
        ]
    ])
