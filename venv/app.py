import telebot
from config import TOKEN, exchanger
from extenxions import Converter, ConverterException

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start(message: telebot.types.Message):
    text = r'''Введите запрос в форме 
<переводимая валюта> <необходимая валюта> <количество>
/values - список доступных валют'''
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in exchanger.keys():
        text = '\n'.join((text, i))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def converter(message: telebot.types.Message):
    values = message.text.split()
    values = list(map(str.lower, values))
    try:
        result = Converter.get_price(values)
    except ConverterException as e:
        bot.reply_to(message, f'Ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду \n{e}')
    else:
        text = f'Цена {values[2]} {values[0]} в {values[1]} -- {result}{exchanger[values[1]]}'
        bot.reply_to(message, text)




bot.polling()