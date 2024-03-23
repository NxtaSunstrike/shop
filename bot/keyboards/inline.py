from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

def admin_kb()->InlineKeyboardMarkup:
    button_admin = [
        [
            InlineKeyboardButton(text = 'add cloth👻',callback_data='add')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=button_admin)

def subscriber_kb()->InlineKeyboardMarkup:
    button_subscriber = [
        [
            InlineKeyboardButton(text = '🤡subscribe🤡',url='https://t.me/ayeshacloths')
         ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=button_subscriber)