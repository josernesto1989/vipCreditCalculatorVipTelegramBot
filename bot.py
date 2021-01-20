#bot = telegram.Bot('870389483:AAE6i7fBhPR88g_OL363CMx7_hp9KkUu3dQ')
#!/usr/bin/python3
import os
import sys
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from dbhelper import DBHelper
############################### Bot ############################################

onServer=True
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1572067631:AAH9Ubb4SZ9K-OJXyF3uUzrcvwxJeLe_8kU'

db = DBHelper()

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
  if len(words)>3:
    update.message.reply_text(message)
  elif not words[1] in creditsValues:
    update.message.reply_text("no se ecuentra el servicio") #poner lista de servicios
  else:
    try:
        x = float(words[2])
        update.message.reply_text(str(calculate(words[1],x))+"CUP")
    except:
       update.message.reply_text(words[2]+' deberia ser un numero')

        



########################### GESTION DE USUARIOS #################################
def addUser(update: Update, context: CallbackContext):
  words = update.message['text'].split()
  message = "Debe insertar el nombre del usuario"
  if len(words)>1:    
    x, words = words
    words = ''.join(words)
    if findInAsist(words):
      message = "Ya existe el usuario \""+words+"\""
    else:
      asistencia.append([words,'A'])
      db.add_item(words)
      message = "El usuario \""+words+"\" ha sido agregado"
  update.message.reply_text(message)

def findInAsist(user):
  for i in asistencia:
    if i[0] == user:
      return True
  return False

def removeUser(update: Update, context: CallbackContext):
  words = update.message['text'].split()
  message = "Debe insertar el nombre del usuario"
  if len(words)>1:    
    x, words = words
    words = ''.join(words)
    if findInAsist(words):
      for i in range(len(asistencia)):
        if asistencia[i][0] == words:
          asistencia.pop(i)
          db.delete_item(words)
          message = "El usuario \""+words+"\" fue eliminado"
    else:
      message = "El usuario \""+words+"\" no existe"
  update.message.reply_text(message)
  


def main():
  ############################# Handlers #########################################
  updater = Updater(TOKEN, use_context=True)

  dp = updater.dispatcher

  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(CommandHandler('help', help))
  dp.add_handler(CommandHandler('credit', calc))

  updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
  updater.bot.setWebhook('https://vipcellcreditos-bot.herokuapp.com/' + TOKEN)

  updater.start_polling()
  updater.idle()
  ################################################################################

if __name__ == '__main__':
    main()