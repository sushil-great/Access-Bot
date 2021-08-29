from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import Update


class BannedMessageCallback:

    def __init__(self):
        self.filters = ControlGroupFilter()
        self.handler = CallbackQueryHandler(
            BannedMessageCallback.callback_function,
            pass_user_data=True,
            pass_chat_data=True,
            pass_groups=True,
            pattern="banned-msg"
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        update.callback_query.answer(
            text="The user is banned from using this bot, to unban reply /unban to a fwd message or send /unban [user-id]",
            show_alert=True
        )


banned_message_callback_handler = BannedMessageCallback()
