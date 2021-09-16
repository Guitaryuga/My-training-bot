import logging
import settings
import ephem
from datetime import datetime
from emoji import emojize
from glob import glob
from random import randint, choice
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
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
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()


def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать шибера']])


def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    print('Вызван /start')
    update.message.reply_text(f"Здравствуй, пользователь {context.user_data['emoji']}!", reply_markup=main_keyboard())


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    update.message.reply_text(f"Здравствуй, {username} {context.user_data['emoji']}! Ты написал: {text}")


def goodbye(update, context):  # не работает вместе с предыдущим MessageHandler
    user_text = update.message.text.lower()
    if 'пока' in user_text:
        update.message.reply_text('Пока, пользователь!Удачи!')


def know_const(update, context):
    name_planet = update.message.text.split()
    planet_date = datetime.now().date()
    planet = name_planet[1]
    if not hasattr(ephem, planet):
        update.message.reply_text('К сожалению, я пока не знаю такой планеты')
    else:
        planet_precalc = getattr(ephem, planet)
        planet_calc = planet_precalc(planet_date)  # planet_dictionary[planet]
        const = ephem.constellation(planet_calc)
        update.message.reply_text(f'Сегодня планета {planet} находится в созвездии {const}')


def word_counting(update, context):
    user_text = update.message.text.split()
    if not user_text:
        update.message.reply_text("Ты ничего не написал!")
    else:
        counter = len(user_text)
        update.message.reply_text(f'{counter - 1} слов(а)')


def next_full_moon(update, context):
    planet_date = datetime.now().date()
    full_moon = ephem.next_full_moon(planet_date)
    update.message.reply_text(f'Ближайшее полнолуние будет {full_moon}')


def rickroll(update, context):
    print('Вызван /rickroll')
    update.message.reply_text('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    if user_number > bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!"
    elif user_number == bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ничья!"
    else:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, я выиграл!"
    return message


def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = "Введите целое число"
    else:
        message = "Введите целое число"
    update.message.reply_text(message)


def send_shiba_picture(update, context):
    shiba_photos_list = glob('images/shiba*.jp*g')
    shiba_pic_filename = choice(shiba_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(shiba_pic_filename, 'rb'), reply_markup=main_keyboard())


if __name__ == "__main__":
    main()
