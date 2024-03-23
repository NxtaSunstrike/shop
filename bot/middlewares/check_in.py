from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware,types

from bot.keyboards.inline import subscriber_kb
class CheckSubs(BaseMiddleware):
    
    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any]
    ) -> Any:
        member = await event.bot.get_chat_member('@ayeshacloths',event.from_user.id)
        
        if member.status == 'left':
            return await event.answer(
                'You are not subscribed to the channel',
                reply_markup=subscriber_kb()
                )
        else:
            return await handler(event, data)