# my_project
telegram_bot
import telebot, wikipedia, re
import random
from telebot import types
file = open(r'C:\Users\User\PycharmProjects\wlan\my_project\facts.txt', 'r', encoding='UTF-8')
facts = file.read().split('\n')



bot = telebot.TeleBot('5169126482:AAHbUpWVZN6qMU9dRb4e0K5joOSXMbluSEA')
wikipedia.set_lang("ru")


# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext = ny.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split('.')
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ''
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not('==' in x):
                    # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if(len((x.strip()))>3):
                   wikitext2 = wikitext2+x+'.'
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return 'к сожалению этого я не знаю'

# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Приветсвую тебя мой дорогой друг! ')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("факт")
    item2 = types.KeyboardButton("всезнайка")
    bot.send_message(m.chat.id,'Нажми: \nФакт:- для получения интересного факта\n '
                               'Всезнайка: - для получения любого определения',
                     reply_markup = markup)
    markup.add(item1)
    markup.add(item2)

# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))
    if message.text.strip() == 'факт':
        answer = random.choice(facts)


        # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == 'всезнайка':
        bot.send_message(message.chat.id, getwiki(message.text))
        # Отсылаем юзеру сообщение в его чат


file.close()
features = "html.parser"
# Запускаем бота
bot.polling(none_stop=True, interval=0)
