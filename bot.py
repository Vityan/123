import config
import telebot
import botan
import random
import weather
bot = telebot.TeleBot(config.token)
random.seed()


@bot.message_handler(commands=["start"]) # Обработка /start
def handle_start(message):
    bot.send_message(message.from_user.id, 'Привет  \nMy pezduk')


@bot.message_handler(commands=['random'])
def cmd_random(message):
    bot.send_message(message.chat.id, random.randint(1, 10))
    # Если не нужно собирать ничего, кроме количества использований, замените третий аргумент message на None
    botan.track(config.botan_key, message.chat.id, message, 'Случайное число')
    return


@bot.message_handler(commands=['yesorno'])
def cmd_yesorno(message):
    bot.send_message(message.chat.id, random.choice(strings))
    # Если не нужно собирать ничего, кроме количества использований, замените третий аргумент message на None
    botan.track(config.botan_key, message.chat.id, message, 'Да или нет')
    return


@bot.message_handler(commands=['weather'])
def cmd_weather(message):
    gorod=str(input())
    string_weather = weather.getweather('gorod')
    bot.send_message(message.chat.id, string_weather)
    botan.track(config.botan_key, message.chat.id, message, 'Погода')
    return

if __name__ == '__main__':
    global strings
    strings = ['Да', 'Нет']
    bot.polling(none_stop=True)

