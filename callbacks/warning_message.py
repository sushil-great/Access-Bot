from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import Update


class WarningCallBack:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.handler = CallbackQueryHandler(
            WarningCallBack.callback_function,
            pass_user_data=True,
            pass_chat_data=True,
            pass_groups=True,
            pattern="warn-msg"
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        update.callback_query.answer(
            text="The user seems to be already marked as approved in the database",
            show_alert=True
        )


warn_message_callback_handler = WarningCallBack()
