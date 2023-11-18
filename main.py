import telebot
import google.generativeai as palm
import os

palm.configure(api_key='AIzaSyAH2RdrYVfsoXHYTycFkf7tCODLw9R3mZw')

bot = telebot.TeleBot("6706341567:AAETyjnaiL0D7qfy7onS2EDeHCHIniaxPh4")

@bot.message_handler(content_types=['text'])
def echo(message):
  prompt = message.text
  response = palm.chat(messages = prompt)
  bot.send_message(message.chat.id, response.last)

bot.polling()
