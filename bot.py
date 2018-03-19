import config
import telebot
import botan
import random
import weather
bot = telebot.TeleBot(config.token)
random.seed()

@bot.message_handler(commands=["start"]) # Обработка /start
def handle_start(message):
    bot.send_message(message.from_user.id, 'Привет  \nMy dear friend ')




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


        
        
    

@bot.message_handler(content_types=['text'])
def hand_text(message):
   if message.text == "/weather":	
      string_weather = weather.getweather('Севастополь')
      bot.send_message(message.chat.id, string_weather)
      botan.track(config.botan_key, message.chat.id, message, 'Погода ')
      return
   elif message.text[:9] == "/weather " :
      s = message.text.split()
      city = s[1]
      bot.send_message(message.from_user.id, weather.getweather(city))
      botan.track(config.botan_key, message.chat.id, message, 'Погода')
      return
  else:   
     pass

@bot.message_handler(content_types=['text'])
def handle_text(message):

# Если пользователь отправил "привет, как тебя зовут?" отвечаем "робот я"
   if message.text == "привет, как тебя зовут?":
      bot.send_message(message.from_user.id, 'робот я')
      botan.track(config.botan_key, message.chat.id, message, 'text')
      return  
# Если пользователь отправил "и чо?" отвечаем "да ничо"
   elif message.text == "и чо?":
      bot.send_message(message.from_user.id, 'да ничо')
      botan.track(config.botan_key, message.chat.id, message, 'text')
      return
   
#Если пользователь отправил слово/фразу, на которое(ую) нет ответа
   else:
      bot.send_message(message.from_user.id, "Извините, я Вас не понимаю")
      botan.track(config.botan_key, message.chat.id, message, 'text')  
      return  



if __name__ == '__main__':
    global strings
    strings = ['Да', 'Нет']
    bot.polling(none_stop=True)

