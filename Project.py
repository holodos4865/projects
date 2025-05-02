import pprint
morse_code_dict = {
    'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..',
    'Е': '.', 'Ж': '...-', 'З': '--..', 'И': '..', 'Й': '.---',
    'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---',
    'П': '.--.', 'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-',
    'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.', 'Ш': '----',
    'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..',
    'Ю': '..--', 'Я': '.-.-',

    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.----.',
    '!': '-.-.--',
    '/': '-..-.',
    '(': '-.--.',
    ')': '-.--.-',
    '&': '.-...',
    ':': '---...',
    ';': '-.-.-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '_': '..--.-',
    '"': '.-..-.',
    '$': '...-..-',
    '@': '.--.-.',
    ' ': '/',
}
#morse_code_dict = {k: v.replace('-', '_') for k, v in morse_code_dict1.items()}
#morse_code_dict = {k: v.replace('.', '*') for k, v in morse_code_dict1.items()}
reverse_dict = {v: k for k, v in morse_code_dict.items()}
pprint.pprint(reverse_dict)
pprint.pprint(morse_code_dict)
history_list = []
import telebot
bot_token = ""
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет,это бот может конвертировать товй текст в азбуку морза по команде - /konv_to_morse также"
                                      "ты можешь конвертировать азбуку морсе в текст по команде - /know_to_text , а еще "
                                      "ты можешь посмотреть свою истроию конвертирования по команде - /history")
@bot.message_handler(commands=['know_to_text'])
def start_know_to_text(message):
    if message.text == "/start":
        start(message)
    else:
        bot.send_message(message.chat.id, "Напиши текст который вы хотите конвертировать в азбуку морза")
        bot.register_next_step_handler(message, know_to_text)
def know_to_text(message):
    global history_list
    result =""
    text = message.text.strip().split()
    result_1 = ""
    for i in text:
        result += reverse_dict[i]
        result+=' '
    bot.send_message(message.chat.id, result)
    bot.send_message(message.chat.id,
                     "если вы хотите остановить то напишите /start или чтобы продолжить напишите любой символ")
    bot.register_next_step_handler(message, start_know_to_text)
    for i in text:
        result_1+=i
        result_1+=' '
    history_list.append(f"{result_1} = {result}")
@bot.message_handler(commands=['konv_to_morse'])
def start_konv(message):
    if message.text == "/start":
        start(message)
    else:
        bot.send_message(message.chat.id,"Напиши текст который вы хотите конвертировать в азбуку морза")
        bot.register_next_step_handler(message,konv)
def konv(message):
    global history_list
    result = ""
    text = message.text.strip().upper()
    for i in text:
        result+=morse_code_dict[i]
        result+=' '
    bot.send_message(message.chat.id,result)
    bot.send_message(message.chat.id,"если вы хотите остановить то напишите /start или чтобы продолжить напишите любой символ")
    bot.register_next_step_handler(message,start_konv)
    history_list.append(f"{text} = {result}")
@bot.message_handler(commands=['history'])
def history(mess):
    global history_list
    res= ""
    for i in history_list:
        res+=i
    bot.send_message(mess.chat.id, res)
bot.polling()
