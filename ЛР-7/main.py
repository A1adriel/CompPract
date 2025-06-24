import telebot
import os

bot = telebot.TeleBot(os.environ['BOT_TOKEN'])

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Бот работает!")

def handler(event, context):
    update = telebot.types.Update.de_json(event['body'])
    bot.process_new_updates([update])
    return {'statusCode': 200}