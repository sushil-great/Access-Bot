from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import Update, ParseMode
from inline_keyboards.confirm_no_request_keyboard import confirm_no_request_keyboard
from inline_keyboards.no_request_keyboard import no_request_keyboard
from helpers.email import email_regex_str


class NoRequestCallback:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.handler = CallbackQueryHandler(
            NoRequestCallback.callback_function,
            pass_user_data=True,
            pass_chat_data=True,
            pass_groups=True,
            pattern=f"gr;[0-9]+;{email_regex_str};[01](;[0-9]+)?"
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        callback_data = update.callback_query.data.split(";")
        chat_id_with_no_req = int(callback_data[1])
        email_id_used = callback_data[2]
        no_req_confirm = callback_data[3]

        if no_req_confirm == "0":
            update.effective_message.edit_reply_markup(
                confirm_no_request_keyboard(
                    chat_id_with_no_req,
                    email_id_used,
                    update.callback_query.from_user.id
                )
            )
            return

        confirming_admin = int(callback_data[4])
        if no_req_confirm == "1" and update.callback_query.from_user.id == confirming_admin:
            try:
                message_sent = context.bot.send_message(
                    chat_id=chat_id_with_no_req,
                    text="*Dear member*\n\n" +
                    "we could not find any request on the Google Group" +
                    f"with the email you provided i.e. `{email_id_used}`",
                    parse_mode=ParseMode.MARKDOWN
                )
            except:
                update.callback_query.answer(
                    text="There was an error conveying your message :(",
                    show_alert=True
                )
                return

            update.effective_message.edit_reply_markup(
                no_request_keyboard(
                    chat_id_with_no_req,
                    email_id_used,
                    message_sent.message_id
                )
            )

        else:
            update.callback_query.answer(
                text="It needs to be confirmed by the admin who started it.",
                show_alert=True
            )


no_request_callback_handler = NoRequestCallback()
