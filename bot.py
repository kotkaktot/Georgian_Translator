# -*- coding: utf-8 -*-
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import token
from datetime import datetime, timedelta
from translate import katoru_translate
import os

# Init
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename='{}/logs/logs_{}.log'.format(BASE_DIR, datetime.today().strftime('%Y%m%d')),
                    format=u'%(filename)+13s [ LINE:%(lineno)-4s] %(levelname)-8s [%(asctime)s] %(message)s',
                    level=logging.DEBUG)


def msg(update, context):
    try:
        context.bot.send_message(chat_id=update.effective_chat.id, text=katoru_translate(update.message.text))
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text='Что-то пошло не так!')


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Привет! Присылай мне текст на грузинском или его'
                                                                    ' транслитерацию, а я всё переведу на славный русский язык!')


msg_handler = MessageHandler(Filters.text, msg)
updater = Updater(token, use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(msg_handler)

updater.start_polling()
updater.idle()