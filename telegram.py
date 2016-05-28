# -*- coding: utf-8 -*-
import config
import telebot
import time
#import cv

bot = telebot.TeleBot(config.token)

def mes ():
        f = open('../../../Camera/telegram/text1.txt')
        bot.send_message( , f.read()) # впишите первым аргументом идентификатор оператора
        return 0

def photo ():
        photo = open('../../../Camera/telegram/image/ny.jpg', 'rb')
        bot.send_photo(, photo) # впишите первым аргументом идентификатор оператора
        return 0
mes()
photo()
#if __name__ == '__main__':
#        bot.polling(none_stop=True)

