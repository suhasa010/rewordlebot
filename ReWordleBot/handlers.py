from telegram.ext import (CallbackQueryHandler, CommandHandler, InlineQueryHandler)

from .rewordlebot import game, inline_game, sendgame
handlers = {
    CallbackQueryHandler: [
        ({"callback": game}, ()),
    ],
    CommandHandler: [
        ({"command": ['play','start'], "callback": sendgame}, ()),
    ],
    InlineQueryHandler: [
        ({"callback": inline_game}, ()),
    ],
}