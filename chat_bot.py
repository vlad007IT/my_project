import telebot, wikipedia, re
import random
from telebot import types


bot = telebot.TeleBot('5169126482:AAHbUpWVZN6qMU9dRb4e0K5joOSXMbluSEA')
wikipedia.set_lang("ru")

file = open('facts.txt', 'r', encoding='UTF-8')
facts = file.read().split('\n')
file.close()


@bot.message_handler(commands=["start"])
def start(m, res=False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    markup.add(item1)
    bot.send_message(m.chat.id, 'Нажми кнопку Факт или отправть любое слово', reply_markup=markup)

# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break

        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)

        return wikitext2

    except Exception as e:
        return 'к сожалению этого я не знаю'


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
        bot.send_message(message.chat.id, answer)
    elif message.text.strip():
        bot.send_message(message.chat.id, getwiki(message.text))


#features = "html.parser"
# Запускаем бота
bot.polling(none_stop=True, interval=0)
