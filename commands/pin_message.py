from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update


class PinMessage:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.command_trigger: str = 'pin'
        self.handler = CommandHandler(
            self.command_trigger,
            PinMessage.callback_function,
            filters=self.filters,
            pass_args=True,
            run_async=True
        )

    @staticmethod
    def callback_function(update: Update, _: CallbackContext):

        if not update.effective_message.reply_to_message:
            update.effective_message.reply_markdown(
                "*Reply to a message*"
            )

        else:
            disable_notification = not context.args or context.args[0] != "loud"

            update.effective_message.reply_to_message.pin(
                disable_notification=disable_notification
            )


pin_message_command = PinMessage()
