from .model import Messages


class MessagesService:

    async def create_message(self, *, message: str) -> Messages:
        message = Messages(message=message)
        await message.save()
        return message


message_service = MessagesService()
