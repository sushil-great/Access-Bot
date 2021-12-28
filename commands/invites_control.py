from filters.control_group_filter import ControlGroupFilter
from telegram.ext import CommandHandler, CallbackContext
from telegram import Update

from helpers.status_control import get_invites_status, set_invites_status

class BotStatus:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.command_trigger: str = 'status'
        self.handler = CommandHandler(
            self.command_trigger,
            BotStatus.callback_function,
            filters=self.filters,
            pass_args=True,
            run_async=True
        )

    @staticmethod
    def callback_function(update: Update, _: CallbackContext):

        bot_status = get_invites_status()

        if bot_status == 'on':
            update.message.reply_text(f'The bot is currently accepting requests.')
        else:
            update.message.reply_text(f'The bot is currently *NOT* accepting any requests.')


class InvitesOn:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.command_trigger: str = 'inviteson'
        self.handler = CommandHandler(
            self.command_trigger,
            InvitesOn.callback_function,
            filters=self.filters,
            pass_args=True,
            run_async=True
        )

    @staticmethod
    def callback_function(update: Update, _: CallbackContext):

        set_invites_status('on')
        update.message.reply_text('Invites are now ON')


class InvitesOff:

    def __init__(self):

        self.filters = ControlGroupFilter()
        self.command_trigger: str = 'invitesoff'
        self.handler = CommandHandler(
            self.command_trigger,
            InvitesOff.callback_function,
            filters=self.filters,
            pass_args=True,
            run_async=True
        )

    @staticmethod
    def callback_function(update: Update, _: CallbackContext):

        set_invites_status('off')
        update.message.reply_text('Invites are now OFF')


bot_status_command = BotStatus()
invites_on_command = InvitesOn()
invites_off_command = InvitesOff()
