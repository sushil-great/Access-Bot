from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update, ParseMode
from config import config
from inline_keyboards.banned_keyboard import banned_message
from database.Message import DBMessage
from database.Chat import DBChat
import random
import logging


class BanChat:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.command_trigger: str = 'ban'
        self.handler = CommandHandler(
            self.command_trigger,
            BanChat.callback_function,
            filters=self.filters,
            pass_args=True,
            run_async=True
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        chat_id_to_be_banned = 0
        chat_id_found = False

        if update.effective_message.reply_to_message:
            reply_to_message_id = update.effective_message.reply_to_message.message_id
            message_object: DBMessage = DBMessage.objects(
                current_message_id=reply_to_message_id,
                current_chat_id=config.control_group_id
            ).first()

            if not message_object:
                update.effective_message.reply_markdown(
                    '*Wrong Usage*\n\n' +
                    'Please reply to a message forwarded by me' +
                    ' or pass an ID 😭'
                )

            else:
                chat_id_to_be_banned = message_object.original_chat_id
                chat_id_found = True

        elif context.args and not chat_id_found and len(context.args) > 0:
            chat_id_to_be_banned = int(context.args[0])
            chat_id_found = True

        else:
            update.effective_message.reply_markdown(
                '*Hmmmm*\n\n' +
                'Tell me which user to ban 🤷‍♂️'
            )

        if not chat_id_found:
            return

        chat_to_be_banned: DBChat = DBChat.objects(
            chat_id=chat_id_to_be_banned,
            chat_type='private'
        ).first()

        if not chat_to_be_banned:
            update.effective_message.reply_markdown(
                '*Hmmmm*\n\n' +
                'I don\'t seem to have interacted with this' +
                ' user before 🤔'
            )

        else:

            if chat_to_be_banned.chat_is_banned:
                try:
                    update.effective_message.reply_markdown(
                        '*Well!!*\n\n' +
                        f'The [user](tg://user?id={chat_id_to_be_banned}) ' +
                        'was already banned 😈'
                    )

                    user_messages = DBMessage.objects(
                        current_chat_id=config.control_group_id,
                        original_chat_id=chat_id_to_be_banned
                    )

                    if not user_messages:
                        update.effective_message.reply_markdown("*No messages were found for this person*")

                    else:
                        for msg in user_messages:
                            context.bot.edit_message_reply_markup(
                                chat_id=config.control_group_id,
                                message_id=msg.current_message_id+1,
                                reply_markup=banned_message()
                            )

                except:
                    update.effective_message.reply_markdown(
                        '*Sorry*\n\n' +
                        'Some error occurred while banning 😕'
                    )

                return

            chat_to_be_banned.chat_is_approved = False
            chat_to_be_banned.chat_is_banned = True

            try:
                chat_to_be_banned.save()
                update.effective_message.reply_markdown(
                    '*Success!!*\n\n' +
                    f'The [user](tg://user?id={chat_id_to_be_banned}) ' +
                    'has been banned from using this bot 😈'
                )

                context.bot.send_animation(
                    chat_id=chat_id_to_be_banned,
                    animation=random.choice(config.gifs_for_bans),
                    caption='*You have been banned from using this bot!*',
                    parse_mode=ParseMode.MARKDOWN
                )

                user_messages = DBMessage.objects(
                    current_chat_id=config.control_group_id,
                    original_chat_id=chat_id_to_be_banned
                )

                for msg in user_messages:
                    context.bot.edit_message_reply_markup(
                        chat_id=config.control_group_id,
                        message_id=msg.current_message_id+1,
                        reply_markup=banned_message()
                    )

            except:
                update.effective_message.reply_markdown(
                    '*Sorry*\n\n' +
                    'Some error occurred while banning 😕'
                )


ban_chat_command = BanChat()
