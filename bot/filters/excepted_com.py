from aiogram.filters import BaseFilter
from aiogram.types import Message

class ExcCom(BaseFilter):

    def __init__ (self,msg: str | list[str]) -> None:
        self.msg = msg
        
    async def __call__ (self, message: Message) -> bool:
        if isinstance(self.msg, str):
            return message.text != self.msg
        return message.text not in self.msg 