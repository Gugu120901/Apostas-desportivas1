from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = "7992952243:AAFMQd0wmWrUe6eCCOPC9ZpRBvzebvDZLyg"

def start(update: Update, context: CallbackContext):
    update.message.reply_text("🤖 Bot de Apostas está online!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
