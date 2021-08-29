from telegram.ext import UpdateFilter
from telegram import Update


class PrivateChatFilter(UpdateFilter):

    def filter(self, update: Update):

        if update.effective_chat.type == "private":
            return True

        return False
