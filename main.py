import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    CallbackContext,
    Updater,
    PicklePersistence,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler,
)
from cred import TOKEN
from menu import main_menu_keyboard, dopinfo_menu_keyboard
from key_buttons import button, dop_button
from pars import *

def start(update:  Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id = update.effective_chat.id,
        sticker = 'CAACAgQAAxkBAAEFQolizpgJnmLj3z9BJoi55JWfuIYeOwACDhUAAtqjlSzTnxMVjfioWCkE'
        )
    update.message.reply_text(
        'Здравствуйте, {username}'.format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                    else update.effective_user
        ),
        reply_markup=main_menu_keyboard()             
    )

def back(update:  Update, context: CallbackContext):
    update.message.reply_text(
        'Вы в главном меню 🙂',
        reply_markup=main_menu_keyboard()             
    )
            
KRIPTO_WHAT = r'(?=('+(button[0])+r'))'
KRIPTO = r'(?=('+(button[1])+r'))'
BUY = r'(?=('+(button[2])+r'))'
OTZUV = r'(?=('+(button[3])+r'))'
DOPINFO = r'(?=('+(button[4])+r'))'


NFT = r'(?=('+(dop_button[0])+r'))'
META = r'(?=('+(dop_button[1])+r'))'
MAYNING = r'(?=('+(dop_button[2])+r'))'
BLOCK = r'(?=('+(dop_button[3])+r'))'
BACK = r'(?=('+(dop_button[4])+r'))'


def otpravit_otzuv(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id = update.effective_chat.id,
        sticker = 'CAACAgQAAxkBAAEFQotizpnXHCD5GjmgZbxdIoe-Ln-BoQACHBUAAtqjlSzC9x8osVawrCkE'
        )
    a = update.message.text
    if a[:5] == 'Отзыв':
        context.bot.send_message(
            chat_id= '@kkrriippttoo',
            text = a,
        )

def otzuv(update: Update, context: CallbackContext):
    info = re.match(OTZUV, update.message.text)
    update.message.reply_text(
    text = """
Напишите сообщение с "Отзыв: " и оставте свой отзыв🙂
""",
    reply_markup=main_menu_keyboard()
 )

def resive_what_menu(update:Update, context: CallbackContext):
    update.message.reply_text(
        '''
        🟠 Криптовалюта – это любой вид валюты в цифровой или виртуальной форме; для защиты транзакций в криптовалюте используется шифрование (криптография). Не существует центрального органа по выпуску или регулированию криптовалют. Для записи транзакций и выпуска новых единиц используется децентрализованная система.
        ''',
        reply_markup=main_menu_keyboard()
    )

def buy(update: Update, context: CallbackContext):
    update.message.reply_text('https://coinmarketcap.com/')

def resive_dop_menu(update:Update, context: CallbackContext):
    update.message.reply_text(
        'Вы перешли в меню дополнительной информации 👍',
        reply_markup= dopinfo_menu_keyboard()
    )

def nft(update: Update, context: CallbackContext):
    context.bot.sendPhoto(
        update.effective_chat.id,
        photo = open('img/nft.jpg', 'rb'),
        caption = '''
        🟢 NFT (Non-fungible token) — это невзаимозаменяемый токен, который «привязан» к единственному объекту, этим объектом может быть: фотография, картина, гифка, видео, музыкальный трек, персонаж в игре и т. п. цифровой контент
        ''',
        reply_markup= dopinfo_menu_keyboard()
    )

def meta(update: Update, context: CallbackContext):
    context.bot.sendPhoto(
        update.effective_chat.id,
        photo = open('img/metaverce.jpg', 'rb'),
        caption = '''
        🟢 Мир, сочетающий в себе «настоящую» и виртуальную реальность, сейчас принято называть метавселенной.Метавселенная объединяет физический и цифровой миры, открытые и закрытые платформы, частные и общедоступные сети.
        ''',
        reply_markup= dopinfo_menu_keyboard()
    )

def majning(update: Update, context: CallbackContext):
    context.bot.sendPhoto(
        update.effective_chat.id,
        photo = open('img/majning.jpg', 'rb'),
        caption = '''
        🟢 Майнинг – это добыча цифровой валюты с помощью специального оборудования. Если говорить на языке блокчейн-инженеров, майнинг представляет собой присоединение блоков, в которых хранится информация о проведенных транзакциях. В результате они образуют непрерывную и последовательную цепочку – блокчейн.
        ''',
        reply_markup= dopinfo_menu_keyboard()
    )

def block(update: Update, context: CallbackContext):
    context.bot.sendPhoto(
        update.effective_chat.id,
        photo = open('img/block.jpg', 'rb'),
        caption = '''
        🟢 Если упростить сложную терминологию и высказаться доступным языком, то блокчейн – это последовательно выстроенная, непрерывная связка блоков, содержащих определенные данные
        ''',
        reply_markup= dopinfo_menu_keyboard()
    )

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot-data'))
updater.dispatcher.add_handler(CommandHandler('start',start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KRIPTO_WHAT),
    resive_what_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(KRIPTO),
    top
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BUY),
    buy
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(DOPINFO),
    resive_dop_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(NFT),
    nft
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(META),
    meta
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(MAYNING),
    majning
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BLOCK),
    block
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK),
    back
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(OTZUV),
    otzuv
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    otpravit_otzuv,
))


updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()