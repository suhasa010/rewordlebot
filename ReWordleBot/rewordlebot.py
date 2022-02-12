from uuid import uuid4
from telegram.ext import Updater, CallbackContext
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InlineQueryResultArticle, InlineQueryResultGame, InputTextMessageContent, Update

def game(update: Update, _: CallbackContext):
    query = update.callback_query
    query.answer(text="opening game", url="https://rewordlebot.netlify.app/")


def sendgame(update, context):
    markup = InlineKeyboardMarkup([[
                            InlineKeyboardButton(text= "Play ReWordle", callback_game="wordle"),
                        ],
                        [
                            InlineKeyboardButton(text= "Switch to Inline", switch_inline_query_current_chat=""),
                            InlineKeyboardButton(text= "Play with Friends", switch_inline_query=""),
                        ],
            ])
    context.bot.send_game(update.message.chat.id, 'wordle', reply_markup = markup)

def inline_game(update: Update, context: CallbackContext):
    results = list()
    query = update.inline_query.query
    markup = InlineKeyboardMarkup([[
                            InlineKeyboardButton(text= "Play ReWordle", callback_game="wordle"),
                        ],
                        [
                            InlineKeyboardButton(text= "Switch to Inline", switch_inline_query_current_chat=""),
                            InlineKeyboardButton(text= "Play with Friends", switch_inline_query=""),
                        ],
            ])
    if query.lower().startswith(''):
        results.append(
        InlineQueryResultGame(
                type= "game",
                id = update.inline_query.id,
                game_short_name="wordle",
                reply_markup=markup
            )
        )
        context.bot.answer_inline_query(update.inline_query.id, results)