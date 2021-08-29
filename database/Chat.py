from mongoengine import Document, \
    StringField, BooleanField, EmailField, LongField


class DBChat(Document):

    # The Telegram ID of the Chat
    chat_id: LongField = LongField(
        required=True,
        unique=True
    )

    # The Telegram Type of the Chat
    chat_type: StringField = StringField(
        required=True,
        choices=[
            "private",
            "supergroup",
            "group",
            "channel"
        ]
    )

    # True if the Chat is banned
    chat_is_banned: BooleanField = BooleanField(
        required=True,
        default=False
    )

    # True if the Chat is approved
    chat_is_approved: BooleanField = BooleanField(
        required=True,
        default=False
    )

    # Holds the email addresses of the approved chats
    email_address: EmailField = EmailField(
        required=False
    )

    meta = {
        'db_alias': 'core',
        'collection': 'chats'
    }
