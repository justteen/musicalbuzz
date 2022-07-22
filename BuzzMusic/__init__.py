#
# Copyright (C) 2021-2022 by Buzz@Github, < https://github.com/justteen >.
#
# This file is part of < https://github.com/justteen/musicalbuzz > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/justteen/musicalbuzz/blob/main/LICENSE >
#
# All rights reserved.

from BuzzMusic.core.bot import BuzzBot
from BuzzMusic.core.dir import dirr
from BuzzMusic.core.git import git
from BuzzMusic.core.userbot import Userbot
from BuzzMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = BuzzBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
