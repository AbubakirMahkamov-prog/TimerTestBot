import time
from datetime import datetime
end_time=datetime(2021,11,9,7)
import telebot
Token=''
bot=telebot.TeleBot(Token)
import datetime
@bot.message_handler(commands=['start'])
def send_message(message):
    while True:
        structTime = time.localtime()
        if (end_time-datetime.datetime(*structTime[:6])).days==0:
            msg="Vaqt tugashiga  Kun , soat:min:sekund  :   "+"0 days   ,"+str(end_time-datetime.datetime(*structTime[:6]))+" qoldi."
        else:
            msg="Vaqt tugashiga  Kun , soat:min:sekund  :   "+str(end_time-datetime.datetime(*structTime[:6]))+" qoldi."
        bot.send_message(message.chat.id,msg)
        time.sleep(3600)
bot.polling()