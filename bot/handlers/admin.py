from typing import List

from aiogram import Router, F,types,Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from aiogram import types

from bot.filters.isadmin import IsAdmin
from bot.keyboards.inline import admin_kb
from bot.databases.add import add_cloth 
from bot.states.states import ShopFSM
from bot.keyboards.reply import start_keyboard
from bot.middlewares.mediagroup import MediaGroupMiddleware

router = Router()
router.message.middleware(MediaGroupMiddleware())


@router.message(F.text.lower().in_('admin💩'),IsAdmin(6317047101),ShopFSM.start)
async def shop(message:types.Message, state:FSMContext)->None:
    await message.answer_sticker(
                         'CAACAgIAAxkBAAI4S2X_DC2mlX_PUdvqdej35lujF_-mAALlCwACHYnISot5_Xgs3qeXNAQ',reply_markup=admin_kb()
                         )
    
@router.callback_query(F.data.in_('add'),ShopFSM.start)
async def new_cloth(callback:types.CallbackQuery, state:FSMContext)->None:
    await state.set_state(ShopFSM.add_cloth)
    await callback.message.answer('Write name of cloth',reply_markup=ReplyKeyboardRemove())
    

@router.message(ShopFSM.add_cloth,F.media_group_id)
async def add(message:types.Message,album: List[types.Message],bot:Bot)->None:
    cloths = {'path':[],'caption':[]}
    for element in album:
        if element.photo:
            cloths['path'].append('static/img/'+element.photo[-1].file_id+'.jpg')
            if element.caption is not None:
                cloths['caption'].append(element.caption)
        else:
            return message.answer("This media type isn't supported!")
    
    caption = ''.join((cloths['caption'])).split(',')

    if (len(caption)!=4 
        or len(caption[1])<50
        or caption[2].isdigit()==False
        or caption[3].isdigit()==False):
        return await message.answer('Wrong format')
    else:
        await message.answer('You succsesfully add new cloth', reply_markup=start_keyboard(user_id=message.from_user.id))
        cloth = ''.join(cloths['caption']).split(',')+[','.join(cloths['path'])]
        await add_cloth({'name':cloth[0], 'description':cloth[1], 'count':cloth[2], 'price':cloth[3], 'photo_path':cloth[4]})
        for element in cloths['path']:
            await bot.download(
                file = element.replace('static/img/','').replace('.jpg',''), 
                destination=f"bot/web_apps/shop/{element}"
                )

        
        
        

        

    
    
    

    
    


