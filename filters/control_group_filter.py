from telegram.ext import UpdateFilter
from telegram import Update
from config import config


class ControlGroupFilter(UpdateFilter):

    def filter(self, update: Update):

        if update.effective_chat.id == config.control_group_id:
            return True

        else:
            return False
