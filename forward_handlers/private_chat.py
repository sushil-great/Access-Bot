'''
This file handles the forwarding of messages
from users
to the control group
'''

import random

from config import config
from database.Chat import DBChat
from database.Message import DBMessage
from filters.private_chat_filter import PrivateChatFilter
from helpers.email import extract_gmail_email, has_email, has_gmail_email
from inline_keyboards.base_keyboard import base_keyboard
from helpers.status_control import get_invites_status
from telegram import (InlineKeyboardButton, InlineKeyboardMarkup, ParseMode,
                      Update)
from telegram.ext import CallbackContext, Filters, MessageHandler

class PrivateMessageForward:

    def __init__(self):

        self.filters = (~Filters.command) & (PrivateChatFilter())
        self.handler = MessageHandler(
            filters=self.filters,
            callback=PrivateMessageForward.callback_function
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        if (
            not update
            or not update.effective_message
            or not update.effective_chat
            or not update.effective_user
        ):
            return

        chat_object = DBChat.objects(
            chat_id=update.effective_chat.id
        ).first()

        if not chat_object:
            update.effective_message.reply_markdown('*Sorry, please send* /start *first*')
            return

        bot_status = get_invites_status()

        # Check if chat is banned
        if chat_object.chat_is_banned:
            update.effective_message.reply_animation(
                animation=random.choice(config.gifs_for_bans),
                caption="*You're Wasting Time*\n\n" +
                "You were banned from using this bot due to your fuck ups.",
                parse_mode=ParseMode.MARKDOWN
            )
            return

        # Check if chat is already approved
        if chat_object.chat_is_approved:
            update.effective_message.reply_animation(
                animation=random.choice(config.gifs_for_approval),
                caption="*What happened?? 🤔*\n\n" +
                "You are already in the group, go and enjoy.",
                parse_mode=ParseMode.MARKDOWN
            )
            return

        # Check if chat is in main group
        chat_membership_status = context.bot.get_chat_member(
            chat_id=config.group_neccessary,
            user_id=update.effective_chat.id
        )

        if chat_membership_status.status not in ['creator', 'administrator', 'member', 'restricted']:
            update.effective_message.reply_markdown(
                '*Sorry, Do I Know You*\n\n' +
                f'This bot is meant to be used by members of {config.invite_channel_link} only.'
            )
            return

        if bot_status == 'off':
            update.effective_message.reply_markdown(
                text=config.requests_closed_message,
                reply_markup=InlineKeyboardMarkup([
                    [
                        InlineKeyboardButton(
                            text="Doubts/Problems",
                            url=f"{config.help_group_link}"
                        )
                    ]
                ])
            )
            return

        # Checking if the person has a username
        if not update.effective_user.username:
            update.effective_message.reply_photo(
                photo='https://i.imgur.com/jnx5UeM.png',
                caption='''
*You cannot proceed further without setting up a username*

Please set a username first in your Telegram Account settings (see the photo)
''',
                parse_mode=ParseMode.MARKDOWN
            )
            return

        # Checking if the message is media
        if not (update.effective_message.text or update.effective_message.caption):

            if config.only_forward_with_email:
                update.effective_message.reply_markdown(
                    '❌ Messages not containing any email address will not be forwarded'
                )
                return

            forwarded_message = update.effective_message.forward(
                chat_id=config.control_group_id
            )

            forwarded_message_object = DBMessage()
            forwarded_message_object.current_chat_id = config.control_group_id
            forwarded_message_object.current_message_id = forwarded_message.message_id
            forwarded_message_object.original_chat_id = update.effective_chat.id
            forwarded_message_object.original_message_id = update.effective_message.message_id

            try:
                forwarded_message_object.save()
            except:
                update.effective_message.reply_text("Failed to forward due to some database issues")

            update.effective_message.reply_markdown(
                '*Your Message has been forwarded*\n\n' +
                'Have some patience now, it might take some time depending upon the availability of the admins 🍵🍵'
            )

            forwarded_message.reply_markdown(
                f"[user](tg://user?id={update.effective_user.id}) " +
                f"- `{update.effective_user.id}`"
            )

            return

        elif update.effective_message.caption:

            msg_has_email = has_email(update.effective_message.caption)

            if not msg_has_email and config.only_forward_with_email:
                update.effective_message.reply_markdown(
                    '❌ Messages not containing any email address will not be forwarded'
                )
                return

            if msg_has_email and not has_gmail_email(update.effective_message.caption):
                update.effective_message.reply_markdown(
                    'Only mail addresses that end with `@gmail.com` are allowed!!'
                )
                return

            forwarded_message = update.effective_message.forward(
                chat_id=config.control_group_id
            )

            forwarded_message_object = DBMessage()
            forwarded_message_object.current_chat_id = config.control_group_id
            forwarded_message_object.current_message_id = forwarded_message.message_id
            forwarded_message_object.original_chat_id = update.effective_chat.id
            forwarded_message_object.original_message_id = update.effective_message.message_id

            try:
                forwarded_message_object.save()
            except:
                update.effective_message.reply_text("Failed to forward due to some database issues")

            update.effective_message.reply_markdown(
                '*Your Message has been forwarded*\n\n' +
                'Have some patience now, it might take some time depending upon the availability of the admins 🍵🍵'
            )

            if not msg_has_email:
                forwarded_message.reply_markdown(
                    f"[user](tg://user?id={update.effective_user.id}) " +
                    f"- `{update.effective_user.id}`"
                )

            else:
                extracted_gmail_email = extract_gmail_email(
                    update.effective_message.caption
                )
                forwarded_message.reply_markdown(
                    f"[user](tg://user?id={update.effective_user.id})" +
                    f" - `{update.effective_user.id}`",
                    reply_markup=base_keyboard(
                        update.effective_chat.id,
                        extracted_gmail_email
                    )
                )

            return

        # Checking Email
        msg_has_email = has_email(update.effective_message.text)

        if not msg_has_email and config.only_forward_with_email:
            update.effective_message.reply_markdown(
                '❌ Messages not containing any email address will not be forwarded'
            )
            return

        if msg_has_email and not has_gmail_email(update.effective_message.text):
            update.effective_message.reply_markdown(
                'Only mail addresses that end with `@gmail.com` are allowed!!'
            )
            return

        forwarded_message = update.effective_message.forward(
            chat_id=config.control_group_id
        )

        forwarded_message_object = DBMessage()
        forwarded_message_object.current_chat_id = config.control_group_id
        forwarded_message_object.current_message_id = forwarded_message.message_id
        forwarded_message_object.original_chat_id = update.effective_chat.id
        forwarded_message_object.original_message_id = update.effective_message.message_id

        try:
            forwarded_message_object.save()
        except:
            update.effective_message.reply_text("Failed to forward due to some database issues")

        update.effective_message.reply_markdown(
            '*Your Message has been forwarded*\n\n' +
            'Have some patience now, it might take some time depending upon the availability of the admins 🍵🍵'
        )

        if not msg_has_email:
            forwarded_message.reply_markdown(
                f"[user](tg://user?id={update.effective_user.id}) " +
                f"- `{update.effective_user.id}`"
            )

        else:
            extracted_gmail_email = extract_gmail_email(
                update.effective_message.text
            )
            forwarded_message.reply_markdown(
                f"[user](tg://user?id={update.effective_user.id})" +
                f" - `{update.effective_user.id}`",
                reply_markup=base_keyboard(
                    update.effective_chat.id,
                    extracted_gmail_email
                )
            )


private_message_forwarder = PrivateMessageForward()
