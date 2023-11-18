import telebot

bot = telebot.TeleBot("6706341567:AAETyjnaiL0D7qfy7onS2EDeHCHIniaxPh4")

@bot.message_handler(content_types=['text'])
def echo(message):
  bot.send_message(message.chat.id, "привет")

bot.polling()