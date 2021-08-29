from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import Update
from inline_keyboards.base_keyboard import base_keyboard
from helpers.email import email_regex_str


class UndoNoRequestCallback:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.handler = CallbackQueryHandler(
            UndoNoRequestCallback.callback_function,
            pass_user_data=True,
            pass_chat_data=True,
            pass_groups=True,
            pattern=f"u;[0-9]+;[0-9]+;{email_regex_str}"
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        callback_data = update.callback_query.data.split(";")
        message_id = int(callback_data[1])
        chat_id = int(callback_data[2])
        email_id = callback_data[3]

        context.bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )

        update.effective_message.edit_reply_markup(
            base_keyboard(
                chat_id,
                email_id
            )
        )

        update.callback_query.answer(
            text="The action was undone!",
            show_alert=True
        )


undo_no_request_callback_handler = UndoNoRequestCallback()
