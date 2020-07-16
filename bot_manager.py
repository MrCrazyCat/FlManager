import telebot
from main import massage_for_bot

bot = telebot.TeleBot('1395464452:AAHqhQz-86sz5okudmwkuHaXa5WYBEGDqa8')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Manual: name: выводит список заказчиков, account - выводит список аккаунтов из БД')

@bot.message_handler(content_types=['text'])
def send_uname(massage):
	if massage.text == 'name':
		bot.send_message(massage.chat.id, massage_for_bot)
	elif massage.text == 'account'


bot.polling()