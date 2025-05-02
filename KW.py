

import telebot
import time as tm
bot_token = "7720271882:AAEmrP5hVotNNmS2jigrnQhmANqTSHL2N78"
bot = telebot.TeleBot(bot_token)
rem = ''
min = 0
rems = []
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет,это бот напоминалка чтобы начать напишите каоманду - /set или если вы хотите посмореть историю своих напоминаний напишите коману - /history")
@bot.message_handler(commands=['set'])
def set_timer(message):
    global rems
    bot.send_message(message.chat.id, "напишите напоминание")
    bot.register_next_step_handler(message,second_step)
    #timer = int(rem.split()[-1])
    #tm.sleep(timer*60)
    #bot.send_message(message.chat.id,rem)
def second_step(mess):
    global rem
    rem +=mess.text
    bot.send_message(mess.chat.id, "отлично, а теперь напиши насколько минут запустить таймер")
    bot.register_next_step_handler(mess,third_step)
def third_step(mess):
    global rem
    global min
    min += int(mess.text)
    tm.sleep(min*60)
    bot.send_message(mess.chat.id,rem)
@bot.message_handler(commands=['history'])
def get_history(message):
    s="Список напоминаний:\n"+"\n\n".join(rems)
    bot.send_message(message.chat.id, s)
bot.polling()



