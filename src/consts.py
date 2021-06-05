import os
import time

import pytz
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

COGS = [
    'cogs.help',
    'cogs.ping',
    'cogs.flux.add_rss',
    'cogs.flux.del_rss',
    'cogs.flux.flux',
    'cogs.flux.reload',
]

CSV_PARAM = "./param.csv"
date = time.time()
titles = []
TEMP_IMG = "temp-image{}.jpg"
PREFIX = os.getenv("PREFIX")
bot = commands.Bot(command_prefix=PREFIX, help_command=None)
DEFAULT_COLOR = 0x2b41ff
PARAM_CSV = []
FIELD_NAMES = []
TZINFOS = {
    'PDT': pytz.timezone('US/Pacific'),
    '+0200': pytz.timezone('Africa/Cairo')
}
TOKEN = os.getenv("DISCORD_TOKEN")
