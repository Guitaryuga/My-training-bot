import ephem

from datetime import datetime
from glob import glob
from random import choice
from utils import get_smile, main_keyboard, play_random_numbers


def greet_user(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    print('Вызван /start')
    update.message.reply_text(f"Здравствуй, пользователь {context.user_data['emoji']}!", reply_markup=main_keyboard())


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


def rickroll(update, context):
    print('Вызван /rickroll')
    update.message.reply_text('https://www.youtube.com/watch?v=dQw4w9WgXcQ')


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


def user_coordinates(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(f"Ваши координаты {coords} {context.user_data['emoji']}!", reply_markup=main_keyboard())


def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    username = update.effective_user.first_name
    text = update.message.text
    update.message.reply_text(f"Здравствуй, {username} {context.user_data['emoji']}! Ты написал: {text}")
