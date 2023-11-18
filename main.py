import telebot
import google.generativeai as palm
import os

palm.configure(api_key='AIzaSyAH2RdrYVfsoXHYTycFkf7tCODLw9R3mZw')
response = palm.generate_text(prompt='name 3 usa states')
answer = response.result


bot = telebot.TeleBot("6706341567:AAETyjnaiL0D7qfy7onS2EDeHCHIniaxPh4")

@bot.message_handler(content_types=['text'])
def echo(message):
  bot.send_message(message.chat.id, answer)

bot.polling()
