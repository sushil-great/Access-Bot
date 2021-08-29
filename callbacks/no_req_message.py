from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import Update


class NoRequestMsgCallBack:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.handler = CallbackQueryHandler(
            NoRequestMsgCallBack.callback_function,
            pass_user_data=True,
            pass_chat_data=True,
            pass_groups=True,
            pattern="gr-msg"
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        update.callback_query.answer(
            text="The message that there was no request with provided email has been forwarded to the user",
            show_alert=True
        )


no_request_message_callback_handler = NoRequestMsgCallBack()
