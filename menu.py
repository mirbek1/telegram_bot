import telegram
from key_buttons import button, dop_button

def main_menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(button[0]),],
    [telegram.KeyboardButton(button[1]),
    telegram.KeyboardButton(button[2]),],
    [telegram.KeyboardButton(button[3]),],
    [telegram.KeyboardButton(button[4]),],
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def dopinfo_menu_keyboard():
    keyboard = ([
    [telegram.KeyboardButton(dop_button[0]),
    telegram.KeyboardButton(dop_button[1]),],
    [telegram.KeyboardButton(dop_button[2]),
    telegram.KeyboardButton(dop_button[3]),],
    [telegram.KeyboardButton(dop_button[4]),]
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )
