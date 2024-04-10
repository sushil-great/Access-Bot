from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from helpers.email import has_email, extract_email
from helpers.google_group import get_google_group_member


class FindMember:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.command_trigger: str = 'findmember'
        self.handler = CommandHandler(
            self.command_trigger,
            FindMember.callback_function,
            filters=self.filters,
            pass_args=True,
            run_async=True
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        member_email_id = None

        if update.effective_message.reply_to_message:
            replied_to_message = update.effective_message.reply_to_message

            if has_email(replied_to_message.text):
                member_email_id = extract_email(replied_to_message.text)

        if member_email_id is None and has_email(update.effective_message.text):
            member_email_id = extract_email(update.effective_message.text)

        if member_email_id is None:
            update.effective_message.reply_markdown(
                "*Please specify the email id of the member to find on Google Group*"
            )
            return

        update.effective_message.reply_markdown(
            "*Here You Go*",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton(
                    text="Search Results",
                    url=get_google_group_member(member_email_id)
                )]
            ])
        )


find_member_command = FindMember()
