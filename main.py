import random
import telebot
from MYtoken import token

bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
butn1 = telebot.types.KeyboardButton('Играть')
butn2 = telebot.types.KeyboardButton('Нет') 
keyboard.add(butn1,butn2)

@bot.message_handler(commands=['start'])
def start_messege(message):
    bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAI2y2S1PjexCKjjkxNeAAH_F97bDkM1qwACWgADRA3PF3ehkVXRsDZLLwQ')
    msg = bot.send_message(message.chat.id,f'Привет {message.chat.first_name} начнем игру?', reply_markup=keyboard)
    bot.register_next_step_handler(msg,check_answer)


def check_answer(message):
    if message.text=='Играть':
        bot.send_message(message.chat.id, 'Ок,тогда вот правила: Нужно угадать число от 1 до 10 за 3 попытки')
        random_number = random.randint(1,10)
        start_game(message, 3, random_number)    
    else:
        bot.send_message(message.chat.id, 'Ну и ладно!')


def start_game(message,attempts,random_number):
    msg = bot.send_message(message.chat.id, 'Введи число')
    bot.register_next_step_handler(msg, check_number, attempts -1, random_number)


def check_number(message,attempts ,random_number):
    if message.text == str(random_number):
        bot.send_message(message.chat.id, 'Ай маладес!')
        bot.send_photo(message.chat.id,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTlg6aaDQaMBtxGKxdXKbxRlXbqCsYAMUARrQ&usqp=CAU')
    elif attempts ==0:
        bot.send_message(message.chat.id,f'NO попытка! Число было -{random_number},   лоооооооох!')
    else:
        bot.send_message(message.chat.id,f'Попробуй ещё раз,у тебя осталось {attempts} попыток')
        start_game(message,attempts,random_number)


bot.polling()



