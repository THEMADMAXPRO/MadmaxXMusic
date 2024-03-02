from MadmaxXMusic.core.bot import Madmax
from MadmaxXMusic.core.dir import dirr
from MadmaxXMusic.core.git import git
from MadmaxXMusic.core.userbot import Userbot
from MadmaxXMusic.misc import dbb, heroku

from .logging import LOGGER


dirr()
git()
dbb()
heroku()

app = Madmax()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
