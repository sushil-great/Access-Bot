from filters.control_group_filter import ControlGroupFilter
from telegram.ext import MessageHandler, CallbackContext, Filters
from telegram import Update
from database.Message import DBMessage
from config import config


class ControlGroupMessageForward:

    def __init__(self):

        self.filters = (~Filters.command) & (ControlGroupFilter())
        self.handler = MessageHandler(
            filters=self.filters,
            callback=ControlGroupMessageForward.callback_function
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        if not update.effective_message.reply_to_message:
            return

        reply_to_message = update.effective_message.reply_to_message

        reply_to_message_object = DBMessage.objects(
            current_chat_id=config.control_group_id,
            current_message_id=reply_to_message.message_id
        ).first()

        original_chat_id = reply_to_message_object.original_chat_id
        original_message_id = reply_to_message_object.original_message_id

        context.bot.copy_message(
            chat_id=original_chat_id,
            from_chat_id=config.control_group_id,
            message_id=update.effective_message.message_id,
            reply_to_message_id=original_message_id
        )

        update.effective_message.reply_markdown(
            "*Forwarded* 📬"
        )


control_group_message_forwarder = ControlGroupMessageForward()
