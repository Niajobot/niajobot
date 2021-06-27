import logging
import os
from dotenv import load_dotenv
from bot import Bot
from configuration.firebase_configuration import FirebaseConfiguration
from services.suggestion_service import SuggestionService
from services.discord_service import DiscordService
logging.basicConfig(level=logging.INFO)
load_dotenv()

FirebaseConfiguration(os.environ['FIREBASE_CONF_PATH'], os.environ['DATABASE_URL'])
suggestion_service = SuggestionService()
discord_service = DiscordService(suggestion_service)
bot = Bot(os.environ['TMI_TOKEN'], os.environ['CLIENT_ID'], os.environ['BOT_NICK'], os.environ['BOT_PREFIX'], os.environ['CHANNELS'],
          suggestion_service, discord_service)

if __name__ == "__main__":
    bot.run()