#bot = telegram.Bot('870389483:AAE6i7fBhPR88g_OL363CMx7_hp9KkUu3dQ')
#!/usr/bin/python3
import os
import sys
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
############################### Bot ############################################

onServer=True
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1572067631:AAH9Ubb4SZ9K-OJXyF3uUzrcvwxJeLe_8kU'


dolarValue = 40.0

creditsValues = {
    "magma": 41.75,
    "z3x":10.0
}

def calculate(box,value):
  return creditsValues[box]*value

def start(update: Update, context: CallbackContext):
  update.message.reply_text('hola')
  # update.message.reply_text(main_menu_message(),
  #                           reply_markup=main_menu_keyboard())

def help(update: Update, context: CallbackContext):
  text = "Los comandos disponibles son:\n"
  text = text + "\n/help para este menú"
  text = text + "\n/cred <servicio> <cantidad de creditos>"
  update.message.reply_text(text)

def calc(update: Update, context: CallbackContext):
  words = update.message['text'].split()
  message = "Comando incorrecto"
  if len(words)<2:
    update.message.reply_text(message)
  elif not words[1] in creditsValues:
    update.message.reply_text("no se ecuentra el servicio") #poner lista de servicios
  else:
    try:
        x = float(words[2])
        update.message.reply_text(str(calculate(words[1],x))+"CUP")
    except:
       update.message.reply_text(words[2]+' deberia ser un numero')

      
def main():
  ############################# Handlers #########################################
  updater = Updater(TOKEN, use_context=True)

  dp = updater.dispatcher

  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(CommandHandler('help', help))
  dp.add_handler(CommandHandler('cred', calc))

  updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
  updater.bot.setWebhook('https://vipcellcreditos-bot.herokuapp.com/' + TOKEN)

  updater.start_polling()
  updater.idle()
  ################################################################################

if __name__ == '__main__':
    main()