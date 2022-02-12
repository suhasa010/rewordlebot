import logging
import os
from .handlers import handlers
from telegram.ext import Defaults, Updater

class Server:
    stickers = []
    def __init__(self, token: str):

        """
        Server uses Updater to handle different updates from Telegram.
        The bot token and database URL, are obtained from arguments.
        """
        self.updater = Updater(token, user_sig_handler=self.sig_handler, workers = 2, request_kwargs={'read_timeout': 30, 'connect_timeout': 30})
        logging.basicConfig(
            format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
        )
        self._add_handlers()

    def _add_handlers(self):
        dispatcher = self.updater.dispatcher
        for handler_type, handles in handlers.items():
            for handler_kwargs, disp_args in handles:
                handler_obj = handler_type(**handler_kwargs)
                dispatcher.add_handler(handler_obj, *disp_args)
        # for handler_type, handles in deeplinks.items():
        #     for handler_kwargs, disp_args in handles:
        #         handler_obj = handler_type(**handler_kwargs)
        #         dispatcher.add_handler(handler_obj, *disp_args)

    def poll(self, interval):

        """
        Starts polling for updates.
        """  
        self.updater.start_polling()
        logging.info("Started polling")
        self.updater.idle()
    
    def sig_handler(self, *_):
        """
        Shuts down the bot
        """
        print("Shutting down. Bye.")

