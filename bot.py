import telebot
import random
import pyowm


token ="1453354099:AAEqa67IvI4p30HE8Y3mLB7HGqH92NzwBZA"

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, f"Hello, {message.chat.first_name}. In which city should you show the weather?")

@bot.message_handler(content_types=['text'])
def weather(message):
    #city = bot.send_message(message.chat.id, "В каком городе Вам показать погодку?")
    #bot.register_next_step_handler(city, weath)
    owm = pyowm.OWM("2eee802b4810955855cf20441092be57")
    mgr = owm.weather_manager()
    obsarvation = mgr.weather_at_place(message.text)
    w = obsarvation.weather
    temperature = w.temperature('celsius')['temp']
    wind = w.wind()['speed'] 
    hum = w.humidity   
    desc = w.detailed_status
    bot.send_message(message.chat.id, f"It`s {str(desc)} in {str(message.text)} \nTemperature: {str(temperature)} °C\nHumidity: {str(hum)}%\nWind speed: {str(wind)} м/с.")  

if __name__ == "__main__":
    bot.polling(none_stop=True)