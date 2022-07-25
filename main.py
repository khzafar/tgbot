import datetime
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Updater, CallbackContext, Filters

updater = Updater(token='')

reppy = ReplyKeyboardMarkup([
    [KeyboardButton('malumot')],
    [KeyboardButton('kontakt', request_contact=True), KeyboardButton('lokatsiya', request_location=True)],
    [KeyboardButton('profil foto'), KeyboardButton('vaqt')]
], resize_keyboard=True)

def start(update: Update, context: CallbackContext):
    update.message.reply_text(f'Asslamu alaykum {update.effective_user.first_name},\nbotimizga xush kelibsiz!', reply_markup=reppy)

def send_data(update: Update, context: CallbackContext):
    update.message.reply_text(f'Ism: {update.effective_user.first_name}\nFamiliya: {update.effective_user.last_name}\nUsername: {update.effective_user.username}')

def reply_txt(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)

def send_audio(update: Update, context: CallbackContext):
    update.message.reply_audio(update.message.audio)

def send_voice(update: Update, context: CallbackContext):
    update.message.reply_voice(update.message.voice)

def send_photo(update: Update, context: CallbackContext):
    update.message.reply_photo(update.message.photo[0].file_id)

def get_profile(update: Update, context: CallbackContext):
    update.message.reply_photo(update.effective_user)

def send_video(update: Update, context: CallbackContext):
    update.message.reply_video(update.message.video)

def send_animation(update: Update, context: CallbackContext):
    update.message.reply_animation(update.message.animation)

def send_sticker(update: Update, context: CallbackContext):
    update.message.reply_sticker(update.message.sticker)

def send_gif(update: Update, context: CallbackContext):
    update.message.reply_game(update.message.game)

def send_contact(update: Update, context: CallbackContext):
    update.message.reply_contact(update.message.contact)

def send_location(update: Update, context:CallbackContext):
    update.message.reply_location(update.message.location)

def send_date(update: Update, context: CallbackContext):
    d = datetime.datetime.now()
    update.message.reply_text(f'Ayni vaqtdagi taqvim(Grigorian)\n\n<b>{d.strftime("%c")}</b>\n', parse_mode='html')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.text('malumot'), callback=send_data))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.text('rasm'), callback=get_profile))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.text('vaqt'), callback=send_date))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback = reply_txt))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.audio, callback=send_audio))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.voice, callback=send_voice))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.photo, callback=send_photo))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.animation, callback=send_animation))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.sticker, callback=send_sticker))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.game, callback=send_gif))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.text('kontakt'), callback=send_contact))
updater.dispatcher.add_handler(MessageHandler(filters=Filters.text('lokatsiya'), callback=send_location))
updater.start_polling()
updater.idle()

