import telebot

bot = telebot.TeleBot('1676501133:AAE3PILf55H9AWs0YvFCcFmpYdQuFuPnM6w')


@bot.message_handler(commands=['start'])
def start_welcome(message):
    bot.send_message(message.chat.id, 'Бот стартовал!')


@bot.message_handler(commands=['help'])
def start_welcome(message):
    bot.send_message(message.chat.id, "Вам нужна помощь? По всем вопросам можно обратиться к админу бота @SamTonck")
    # bot.send_message(message.chat.id, "Вам нужна помощь? По всем вопросам можно обратиться к")


# @bot.message_handler(func=lambda message: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


bot.polling()
