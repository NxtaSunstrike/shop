from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types.web_app_info import WebAppInfo


def start_keyboard(user_id:int)->ReplyKeyboardMarkup:
    button_users = [
        [
         KeyboardButton(text = 'shop👻',web_app=WebAppInfo(url='https://nxtasunstrike.github.io/flasks/'))
         ]
    ]
    button_admin = [
        [
         KeyboardButton(text = 'shop👻',web_app=WebAppInfo(url='https://nxtasunstrike.github.io/flasks/')),
         KeyboardButton(text = 'admin💩')
         ]
    ]

    if user_id == 6317047101:
        return ReplyKeyboardMarkup(keyboard=button_admin,
                                   one_time_keyboard=True,
                                   resize_keyboard=True)
    else:
        return ReplyKeyboardMarkup(keyboard=button_users,
                                   one_time_keyboard=True,
                                   resize_keyboard=True)