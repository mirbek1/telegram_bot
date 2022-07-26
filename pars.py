from telegram import  Update
from urllib import request
from bs4 import BeautifulSoup
from telegram.ext import (
    CallbackContext,
)

from menu import main_menu_keyboard


def top(update: Update, context: CallbackContext):
    with request.urlopen('https://coinmarketcap.com/trending-cryptocurrencies/') as resp:
        data = resp.read()
        soup = BeautifulSoup(data, 'lxml')
        a = 0
        name = []
        for i in soup.find_all('p', attrs={'class': 'sc-1eb5slv-0 iworPT'}):
            a+=1
            name.append(i.get_text())
            if a == 10:
                break

        soup_price = BeautifulSoup(data, 'lxml')
        price = []
        for el in soup_price.find_all('td', attrs={'style': 'text-align:right'}):
            price.append(el.get_text())
        

        soup_procent = BeautifulSoup(data, 'lxml')
        procent = []
        for item in soup_procent.find_all('span', attrs={'class': 'sc-15yy2pl-0 hzgCfk'}):
            procent.append(item.get_text())


        update.message.reply_text(
        f'''
    🔵{name[0]}
    Цена:    {price[0]}
    Цена изменилась за неделю на: {procent[1]}

    🔵{name[1]}
    Цена:    {price[7]}
    Цена изменилась за неделю на: {procent[3]}

    🔵{name[2]}
    Цена:    {price[14]}
    Цена изменилась за неделю на: {procent[6]}

    🔵{name[3]}
    Цена:    {price[21]}
    Цена изменилась за неделю на: {procent[9]}

    🔵{name[4]}
    Цена:    {price[28]}
    Цена изменилась за неделю на: {procent[11]}

    🔵{name[5]}
    Цена:    {price[35]}
    Цена изменилась за неделю на: {procent[14]}

    🔵{name[6]}
    Цена:    {price[42]}
    Цена изменилась за неделю на: {procent[16]}

    🔵{name[7]}
    Цена:    {price[49]}
    Цена изменилась за неделю на: {procent[17]}

    🔵{name[8]}
    Цена:    {price[56]}
    Цена изменилась за неделю на: {procent[21]}

    🔵{name[9]}
    Цена:    {price[63]}
    Цена изменилась за неделю на: {procent[27]}
        ''',
        reply_markup=main_menu_keyboard()
        )

