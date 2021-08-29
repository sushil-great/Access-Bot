from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CallbackContext, CallbackQueryHandler
from telegram import Update, ParseMode
from database.Chat import DBChat
from database.Message import DBMessage
from config import config
import random
from inline_keyboards.confirm_approval_keyboard import confirm_approval_keyboard
from inline_keyboards.warning_keyboard import warning_keyboard
from inline_keyboards.approved_keyboard import approved_keyboard
from helpers.email import email_regex_str


class ApprovalCallback:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.handler = CallbackQueryHandler(
            ApprovalCallback.callback_function,
            pass_user_data=True,
            pass_chat_data=True,
            pass_groups=True,
            pattern=f"[0-9]+;{email_regex_str};[01](;[0-9]+)?"
        )

    @staticmethod
    def callback_function(update: Update, context: CallbackContext):

        callback_data = update.callback_query.data.split(";")
        chat_id_to_be_approved = int(callback_data[0])
        email_id_to_be_assigned = callback_data[1]
        approval_confirm = callback_data[2]

        if approval_confirm == "0":
            update.effective_message.edit_reply_markup(
                confirm_approval_keyboard(
                    chat_id_to_be_approved,
                    email_id_to_be_assigned,
                    update.callback_query.from_user.id
                )
            )
            return

        confirming_admin = int(callback_data[3])
        if approval_confirm == "1" and update.callback_query.from_user.id == confirming_admin:
            chat_to_approve_object = DBChat.objects(
                chat_id=chat_id_to_be_approved
            ).first()

            if not chat_to_approve_object:
                update.effective_chat.send_message(
                    text=f"Sorry {update.callback_query.from_user.mention_markdown()}, the id: {chat_id_to_be_approved} is new to me",
                    parse_mode=ParseMode.MARKDOWN
                )
                update.callback_query.answer(
                    text="Failure",
                    show_alert=True
                )
                return

            if chat_to_approve_object.chat_is_approved:
                update.callback_query.answer(
                    text="Warning!! The User is already marked approved in the database.",
                    show_alert=True
                )
                update.effective_message.edit_reply_markup(
                    warning_keyboard()
                )
                return

            chat_to_approve_object.chat_is_banned = False
            chat_to_approve_object.chat_is_approved = True
            chat_to_approve_object.email_address = email_id_to_be_assigned

            try:
                chat_to_approve_object.save()
            except:
                update.effective_chat.send_message(
                    text=f"Sorry {update.callback_query.from_user.mention_markdown()}, the id: {chat_id_to_be_approved} could not be approved due to DB Errors",
                    parse_mode=ParseMode.MARKDOWN
                )
                update.callback_query.answer(
                    text="Failure",
                    show_alert=True
                )
                return

            update.effective_chat.send_message(
                text=f"Dear {update.callback_query.from_user.mention_markdown()}, the [user](tg://user?id={chat_id_to_be_approved}) has been approved",
                parse_mode=ParseMode.MARKDOWN
            )
            update.callback_query.answer(
                text="Success",
                show_alert=True
            )
            context.bot.send_animation(
                chat_id=chat_id_to_be_approved,
                animation=random.choice(config.gifs_for_approval),
                caption="*Congratulations!*\n\n" +
                f"Your email `({email_id_to_be_assigned})` has been accepted in the Google Group",
                parse_mode=ParseMode.MARKDOWN
            )

            user_messages = DBMessage.objects(
                current_chat_id=config.control_group_id,
                original_chat_id=chat_id_to_be_approved
            )
            for msg in user_messages:
                try:
                    context.bot.edit_message_reply_markup(
                        chat_id=config.control_group_id,
                        message_id=msg.current_message_id+1,
                        reply_markup=approved_keyboard(email_id_to_be_assigned)
                    )
                except:
                    pass

            context.bot.send_message(
                chat_id=config.log_channel_id,
                text=f"*Email:* {email_id_to_be_assigned}\n" +
                f"*ID:* `{chat_id_to_be_approved}`\n" +
                f"*Link:* [user](tg://user?id={chat_id_to_be_approved})",
                parse_mode=ParseMode.MARKDOWN
            )

        else:
            update.callback_query.answer(
                text="It needs to be confirmed by the admin who started it.",
                show_alert=True
            )


approval_callback_handler = ApprovalCallback()
