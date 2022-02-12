import os
from dotenv import load_dotenv
from .server import Server

load_dotenv()
token = os.getenv("BOT_API")
interval = int(os.getenv("POLL_INTERVAL", 1))

server = Server(token)

server.poll(interval)
