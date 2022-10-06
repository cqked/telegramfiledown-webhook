import jsonpath as jsjx


class Message:
    def __init__(self, messages):
        message = jsjx.jsonpath(messages, '$.message')[0]
        # self.message_id = jsjx.jsonpath(message, '$.message_id')
        # self.from_id = jsjx.jsonpath(message, '$.from.id')
        # self.from_is_bot = jsjx.jsonpath(message, '$.from.is_bot')
        # self.from_first_name = jsjx.jsonpath(message, '$.from.first_name')
        # self.from_last_name = jsjx.jsonpath(message, '$.from.last_name')
        # self.from_language_code = jsjx.jsonpath(message, '$.from.language_code')
        self.chat_id = jsjx.jsonpath(message, '$..chat.id')
        # self.chat_first_name = jsjx.jsonpath(message, '$.chat.first_name')
        # self.chat_type = jsjx.jsonpath(message, '$.chat.type')
        self.date = jsjx.jsonpath(message, '$..date')
        self.media_group_id = (
            jsjx.jsonpath(message, '$..media_group_id')[-1]
            if jsjx.jsonpath(message, '$..media_group_id')
            else None
            )
        self.file_name = (
            jsjx.jsonpath(message, '$..file_name')[-1]
            if jsjx.jsonpath(message, '$..file_name')
            else None
            )
        if jsjx.jsonpath(message, '$..photo'):
            self.file_id = jsjx.jsonpath(message, '$..photo[-1:].file_id')[-1]
        elif jsjx.jsonpath(message, '$..file_id'):
            self.file_id = jsjx.jsonpath(message, '$..file_id')[0]
        else:
            self.file_id = None
        self.file_unique_id = (jsjx.jsonpath(message, '$..file_unique_id')[-1]
                               if jsjx.jsonpath(message, '$..file_unique_id')
                               else None)