import telebot

bot = telebot.TeleBot('xyz') # api key

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '������, �� ������� ��� /start')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == '������':
        bot.send_message(message.chat.id, '������, ��� ���������')
    elif message.text.lower() == '����':
        bot.send_message(message.chat.id, '������, ���������')

bot.polling()