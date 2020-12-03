import logging
import settings
import ephem
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.API_KEY, use_context = True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", know_const))
    dp.add_handler(CommandHandler("rickrollme", rickroll))
    dp.add_handler(CommandHandler("wordcount", word_counting))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Bot started")
    mybot.start_polling()
    mybot.idle()

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
    
def goodbye(update,context):  # не работает вместе с предыдущим MessageHandler
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
      planet_calc = planet_precalc(planet_date) #planet_dictionary[planet]
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

main()