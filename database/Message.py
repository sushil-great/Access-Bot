from mongoengine import Document, LongField


class DBMessage(Document):

    # The ID of the Chat where the message resides
    current_chat_id: LongField = LongField(required=True)

    # The ID of the Message in the Chat
    current_message_id: LongField = LongField(required=True)

    # The ID of the original sender of the message
    original_chat_id: LongField = LongField(required=True)

    # The ID of the original message
    original_message_id: LongField = LongField(required=True)

    meta = {
        'db_alias': 'core',
        'collection': 'messages'
    }
