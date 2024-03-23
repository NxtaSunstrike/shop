from typing import Any, List

from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdmin(BaseFilter):

    def __init__ (self,user_id: int | list[int]) -> None:
        self.user_id = user_id
        
    async def __call__ (self, message: Message) -> bool:
        if isinstance(self.user_id, int):
            return message.from_user.id == self.user_id
        return message.from_user.id in self.user_id