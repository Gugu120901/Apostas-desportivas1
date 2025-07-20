from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = '7992952243:AAFMQd0wmWrUe6eCCOPC9ZpRBvzebvDZLyg'
CHANNEL_ID = '@apostasdesportivas123'

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🤖 Bot de Apostas está online!")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
