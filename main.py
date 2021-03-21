import os
from dotenv import load_dotenv
from bot import Bot
from suggestion_service import SuggestionService
load_dotenv()

suggestion_service = SuggestionService(os.environ['FIREBASE_CONF_PATH'], os.environ['DATABASE_URL'])
bot = Bot(os.environ['TMI_TOKEN'], os.environ['CLIENT_ID'], os.environ['BOT_NICK'], os.environ['BOT_PREFIX'], os.environ['CHANNEL'], suggestion_service)

if __name__ == "__main__":
    bot.run()