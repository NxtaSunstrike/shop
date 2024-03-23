import asyncio
from typing import Any, Awaitable, Callable, Dict, List, Union
from aiogram import BaseMiddleware
from aiogram import types



class MediaGroupMiddleware(BaseMiddleware):
    ALBUM_DATA: Dict[str, List[types.Message]] = {}

    def __init__(self, delay: Union[int, float] = 2):
        self.delay = delay

    async def __call__(
        self,
        handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any],
    ) -> Any:
        if not event.media_group_id:
            return await handler(event, data)

        try:
            self.ALBUM_DATA[event.media_group_id].append(event)
            return
        except KeyError:
            self.ALBUM_DATA[event.media_group_id] = [event]
            await asyncio.sleep(self.delay)
            data["album"] = self.ALBUM_DATA.pop(event.media_group_id)
        return await handler(event, data)
