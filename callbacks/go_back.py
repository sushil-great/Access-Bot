from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import Update
from inline_keyboards.base_keyboard import base_keyboard
from helpers.email import email_regex_str


class ApprovalGoBackCallback:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.handler = CallbackQueryHandler(
            ApprovalGoBackCallback.callback_function,
            pass_user_data=True,
            pass_chat_data=True,
            pass_groups=True,
            pattern=f"b;a;+[0-9]+;{email_regex_str};[0-9]+"
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        callback_data = update.callback_query.data.split(";")
        email_id_to_be_assigned = callback_data[3]
        confirming_admin = int(callback_data[4])

        if confirming_admin == update.callback_query.from_user.id:
            chat_id_to_be_approved = int(callback_data[2])
            update.effective_message.edit_reply_markup(
                base_keyboard(
                    chat_id_to_be_approved,
                    email_id_to_be_assigned
                )
            )

        else:
            update.callback_query.answer(
                text="Only the admin who started can use it",
                show_alert=True
            )


approval_go_back_callback_handler = ApprovalGoBackCallback()


class NoRequestGoBackCallback:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.handler = CallbackQueryHandler(
            NoRequestGoBackCallback.callback_function,
            pass_user_data=True,
            pass_chat_data=True,
            pass_groups=True,
            pattern=f"b;gr;+[0-9]+;{email_regex_str};[0-9]+"
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        callback_data = update.callback_query.data.split(";")
        email_id_to_be_assigned = callback_data[3]
        confirming_admin = int(callback_data[4])

        if confirming_admin == update.callback_query.from_user.id:
            chat_id_to_be_approved = int(callback_data[2])
            update.effective_message.edit_reply_markup(
                base_keyboard(
                    chat_id_to_be_approved,
                    email_id_to_be_assigned,
                )
            )

        else:
            update.callback_query.answer(
                text="Only the admin who started can use it",
                show_alert=True
            )


no_request_go_back_callback_handler = NoRequestGoBackCallback()
