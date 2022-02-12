from random import randint
from telegram.ext import Updater, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update

import os
from dotenv import load_dotenv
load_dotenv()

BOT_API = os.getenv("BOT_API")
updater = Updater(token=BOT_API, use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.DEBUG)
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="""Play wordle on Telegram.
https://telegram.me/rewordlebot?game=wordle
""", parse_mode='HTMl')

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def game(update: Update, _: CallbackContext):
    n = 0
    print(update)
    print("hello")
    query = update.callback_query
    # n = randint(1, 100)
    # query.bot.set_game_score(query.from_user.id, abs(n+100), chat_id = query.message.chat_id, message_id = query.message.message_id)
    query.answer(text="opening game", url="https://rewordlebot.netlify.app/")
    n = 0

from telegram.ext import CallbackQueryHandler
game_handler = CallbackQueryHandler(game)
dispatcher.add_handler(game_handler)

def sendgame(update, context):
    markup = InlineKeyboardMarkup([[
                            InlineKeyboardButton(text= "Play Wordle", callback_game="wordle"),
                        ]])
    context.bot.send_game(update.message.chat.id, 'wordle', reply_markup = markup)

from telegram.ext import CommandHandler
sendgame_handler = CommandHandler('play', sendgame)
dispatcher.add_handler(sendgame_handler)

updater.start_polling()