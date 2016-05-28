# -*- coding: utf-8 -*-
import config
import telebot
import time

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['test'])
def mes (message):
        f = open('../../../Camera/telegram/text1.txt')
        bot.send_message(message.chat.id, f.read())
        return 0

@bot.message_handler(commands=['photo'])
def photo (message):
        photo = open('../../../Camera/telegram/image/ny.jpg', 'rb')
        print(message.chat.id)
        bot.send_photo(message.chat.id, photo)

if __name__ == '__main__':
        bot.polling(none_stop=True)

