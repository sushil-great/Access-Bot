from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, ParseMode
from config import config
from database.Message import DBMessage
from database.Chat import DBChat
import random


class UnBanChat:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.command_trigger: str = 'unban'
        self.handler = CommandHandler(
            self.command_trigger,
            UnBanChat.callback_function,
            filters=self.filters,
            pass_args=True,
            run_async=True
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        chat_id_to_be_unbanned = 0
        chat_id_found = False

        if update.effective_message.reply_to_message:
            reply_to_message_id = update.effective_message.reply_to_message.message_id
            message_object: DBMessage = DBMessage.objects(
                current_chat_id=update.effective_chat.id,
                current_message_id=reply_to_message_id
            ).first()

            if not message_object:
                update.effective_message.reply_markdown(
                    '*Wrong Usage*\n\n' +
                    'Please reply to a message forwarded by me' +
                    ' or pass an ID 😭'
                )

            else:
                chat_id_to_be_unbanned = message_object.original_chat_id
                chat_id_found = True

        elif context.args and not chat_id_found and len(context.args) > 0:
            chat_id_to_be_unbanned = int(context.args[0])
            chat_id_found = True

        else:
            update.effective_message.reply_markdown(
                '*Hmmmm*\n\n' +
                'Tell me which user to un-ban 🤷‍♂️'
            )

        if not chat_id_found:
            return

        chat_to_be_unbanned: DBChat = DBChat.objects(
            chat_id=chat_id_to_be_unbanned,
            chat_type='private'
        ).first()

        if not chat_to_be_unbanned:
            update.effective_message.reply_markdown(
                '*Hmmmm*\n\n' +
                'I don\'t seem to have interacted with this' +
                ' user before 🤔'
            )

        else:

            chat_is_approved = chat_to_be_unbanned.chat_is_approved
            chat_is_banned = chat_to_be_unbanned.chat_is_banned

            if not chat_is_approved and not chat_is_banned:
                update.effective_message.reply_markdown(
                    f"*The* [user](tg://user?id={chat_id_to_be_unbanned}) *was already un-banned and can use the bot.*"
                )
                return

            chat_to_be_unbanned.chat_is_approved = False
            chat_to_be_unbanned.chat_is_banned = False

            try:
                chat_to_be_unbanned.save()
                update.effective_message.reply_markdown(
                    '*Success!!*\n\n' +
                    f'The [user](tg://user?id={chat_id_to_be_unbanned}) ' +
                    'has been un-banned and can use the bot again 😈'
                )

                context.bot.send_animation(
                    chat_id=chat_id_to_be_unbanned,
                    animation=random.choice(config.gifs_for_unbans),
                    caption='*You have been un-banned and can use this bot again!*',
                    parse_mode=ParseMode.MARKDOWN
                )

            except:
                update.effective_message.reply_markdown(
                    '*Sorry*\n\n' +
                    'Some error occurred while saving to database 😕'
                )


unban_chat_command = UnBanChat()
