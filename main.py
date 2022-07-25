from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, Updater, CallbackContext, Filters


updater = Updater(token='5496542594:AAEyl5uRxzYpQqhzpW-4QDcO0G2eHeW729Q')

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Asslamu alaykum {update.effective_user.first_name},\nbotimizga xush kelibsiz!')


def reply_txt(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)


def send_audio(update: Update, context: CallbackContext):
    update.message.reply_audio(update.message.audio)


def send_voice(update: Update, context: CallbackContext):
    update.message.reply_voice(update.message.voice)


def send_photo(update: Update, context: CallbackContext):
    update.message.reply_photo(update.message.photo)


def send_video(update: Update, context: CallbackContext):
    update.message.reply_video(update.message.video)

updater.dispatcher.add_handler(CommandHandler('start', hello))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.text('matn'), callback = reply_txt))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.audio, callback=send_audio))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.voice, callback=send_voice))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.photo, callback=send_photo))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.video, callback=send_video))

updater.start_polling()
updater.idle()

