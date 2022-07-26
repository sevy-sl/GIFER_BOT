import logging
import random
from config1 import TOKEN
from uuid import uuid4
from telegram import InlineQueryResultGif
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from google_images_download import google_images_download 

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, _):
    update.message.reply_text('Hello! :)')

def help_command(update, _):
    update.message.reply_text('Mention my username and write a word or two or more for what you want to search in gifs :-)')


def gifs(update, _):
    query = update.inline_query.query
    response = google_images_download.googleimagesdownload()   
    
    arguments = {"keywords": query,
                "format": "gif",
                "limit":20,
                "print_urls":True,
                'no_download': True}
    paths = response.download(arguments)

    gifs_paths = []
    for k, v in paths[0].items():
        gifs_paths += v

    random_gifs = random.sample(range(20), 20)
    gif1 = gifs_paths[random_gifs[0]]
    gif2 = gifs_paths[random_gifs[1]]
    gif3 = gifs_paths[random_gifs[2]]
    gif4 = gifs_paths[random_gifs[3]]
    gif5 = gifs_paths[random_gifs[4]]
    gif6 = gifs_paths[random_gifs[5]]
    gif7 = gifs_paths[random_gifs[6]]
    gif8 = gifs_paths[random_gifs[7]]
    gif9 = gifs_paths[random_gifs[8]]
    gif10 = gifs_paths[random_gifs[9]]

    update.inline_query.answer([
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif1,
            thumb_url=gif1,
            gif_width=100,
            gif_height=100,
        ),
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif2,
            thumb_url=gif2,
            gif_width=100,
            gif_height=100,
        ),
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif3,
            thumb_url=gif3,
            gif_width=100,
            gif_height=100,
        ),
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif4,
            thumb_url=gif4,
            gif_width=100,
            gif_height=100,
        ),
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif5,
            thumb_url=gif5,
            gif_width=100,
            gif_height=100,
        ),
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif6,
            thumb_url=gif6,
            gif_width=100,
            gif_height=100,
        ),
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif7,
            thumb_url=gif7,
            gif_width=100,
            gif_height=100,
        ),
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif8,
            thumb_url=gif8,
            gif_width=100,
            gif_height=100,
        ),
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif9,
            thumb_url=gif9,
            gif_width=100,
            gif_height=100,
        ),
        InlineQueryResultGif(
            id=uuid4(),
            gif_url=gif10,
            thumb_url=gif10,
            gif_width=100,
            gif_height=100,
        )
    ])


if __name__ == '__main__':

    upd = Updater(TOKEN)

    dp = upd.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(InlineQueryHandler(gifs))

    upd.start_polling()
    upd.idle()