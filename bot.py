import logging
import settings

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from handlers import (greet_user, know_const, rickroll, word_counting, next_full_moon, guess_number, send_shiba_picture,
                      user_coordinates, talk_to_me)
logging.basicConfig(filename='bot.log', level=logging.INFO)


def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", know_const))
    dp.add_handler(CommandHandler("rickrollme", rickroll))
    dp.add_handler(CommandHandler("wordcount", word_counting))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("shiba", send_shiba_picture))
    dp.add_handler(MessageHandler(Filters.regex('^(Прислать шибера)$'), send_shiba_picture))
    dp.add_handler(MessageHandler(Filters.location, user_coordinates))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
