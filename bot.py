from dataclasses import replace
import telebot
import os
bot = telebot.TeleBot("5464291860:AAFZxdeOeVqAuURdqZbw3O4oLfT5mOISFag")

def response(message, _msg):
    bot.reply_to(message, _msg)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # print(message.content_type)
    _message = message.text.replace('/start ','')
    # print(repl)
    if _message == 'container':
        command = os.popen("sudo docker ps -a --format 'table {{.Names}}\t{{.Status}}'")
        output = command.read()
        response(message, output)
    
    if _message == 'deploy':
        command = os.popen("sh /root/deploy_frontend.sh")  
        output = command.read()
        response(message, output)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

print('run bot telegram')
bot.infinity_polling()