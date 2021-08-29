from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update


class PurgeMessages:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.command_trigger: str = 'purge'
        self.handler = CommandHandler(
            self.command_trigger,
            PurgeMessages.callback_function,
            filters=self.filters,
            pass_args=True,
            run_async=True
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        first_message_id: int = 0
        last_message_id: int = update.effective_message.message_id

        if not update.effective_message.reply_to_message:
            update.effective_message.reply_markdown(
                '*Wrong Usage*\n\n' +
                'Reply to a message from where to start.'
            )
        else:
            first_message_id = update.effective_message.\
                reply_to_message.message_id

        try:
            for message_id in range(first_message_id, last_message_id+1):
                context.bot.delete_message(
                    chat_id=update.effective_chat.id,
                    message_id=message_id
                )
            update.effective_chat.send_message(
                text="Successfully purged"
            )
        except:
            update.effective_message.reply_markdown("*Some Error Occurred !*")


purge_messages_command = PurgeMessages()
