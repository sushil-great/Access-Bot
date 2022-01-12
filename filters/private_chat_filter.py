from telegram.ext import UpdateFilter
from telegram import Update


class PrivateChatFilter(UpdateFilter):

    def filter(self, update: Update):

        return update.effective_chat.type == "private"
