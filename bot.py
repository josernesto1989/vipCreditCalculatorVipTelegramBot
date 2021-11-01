#bot = telegram.Bot('870389483:AAE6i7fBhPR88g_OL363CMx7_hp9KkUu3dQ')
#!/usr/bin/python3
import os
import sys
import math
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from DBFirebaseManager import DBFirebaseManager
############################### Bot ############################################

onServer=True
PORT = int(os.environ.get('PORT', 5000))
TOKEN = '1572067631:AAHPjo2HgBnfPKIii7zg9Q63YHTPEt5OKsg'
#1572067631:AAHPjo2HgBnfPKIii7zg9Q63YHTPEt5OKsg

#db = DBFirebaseManager()


dolarValue = 69.0

creditsValues = {
    "magma": 1.00,
    "z3x": 1.145,
    "oct":0.115,
    "chim": 0.122,
    "samst":1.47,
    "samcr":1.47,
    "tunlock":0.42,
    "tmbk":0.69,
    "motokey":1.11,
    "laelo":0.07,
    "suprogen": 1.24,
    "suprospr": 1.24,
    "magict":1.1,
    "samhub":1       
}

# def initializeDB():
#       for key in creditsValues:
#             val = db.getCredByModel(key)
#             if val is None:
#                   db.update(key,0)
      
      

def calculate(box,value):
  #return math.ceil(creditsValues[box]*value*dolarValue)
  return math.ceil(creditsValues[box]*value*dolarValue)

def start(update: Update, context: CallbackContext):
  update.message.reply_text('hola')
  # update.message.reply_text(main_menu_message(),
  #                           reply_markup=main_menu_keyboard())

def help(update: Update, context: CallbackContext):
  text = "Version: 2.0\nLos comandos disponibles son:\n"
  text = text + "\n/help para este menú"
  text = text + "\n/cred <servicio> <cantidad de creditos>"
  text = text + "\n/dolar para saber el precio del dolar"
  # text = text + "\n/rest <servicio> <cantidad de cred> <creditos restantes> resta creditos a un servicio y compara"
  # text = text + "\n/set <servicio> <cantidad de cred> cambia la cantidad creditos a un servicio"
  # text = text + "\n/sum <servicio> <cantidad de cred> adiciona creditos a un servicio"
  text = text + "\nLos servicios disponibles son:"
  for key in creditsValues:
    text = text + "\n"+key
  update.message.reply_text(text)

def calc(update: Update, context: CallbackContext):
  words = update.message['text'].split()
  message = "Comando incorrecto"
  if len(words)<3:
    update.message.reply_text(message)
  elif (words[1] in creditsValues):
    try:
        x = float(words[2])
        update.message.reply_text(str(calculate(words[1],x))+"CUP")
    except:
       update.message.reply_text(words[2]+' deberia ser un numero')    
  else:
    update.message.reply_text("no se ecuentra el servicio") #poner lista de servicios
    

def dolar(update: Update, context: CallbackContext):
  update.message.reply_text("El precio del dolar es "+str(dolarValue)+"cup")

# def rest(update: Update, context: CallbackContext):
#       words = update.message['text'].split()
#       message = "Comando incorrecto"
#       if len(words)<4:
#         update.message.reply_text(message)
#       elif (words[1] in creditsValues):
#         credO = db.getCredByModel(words[1])
#         try:
#             credc = float(words[2])
#             credr = float(words[3])
#             if credr == float(credO)-credc:
#               db.update(words[1],credr)
#               update.message.reply_text("ACTUALIZADO CON EXITO")
#             else:
#               y =str(float(credO)-credc)
#               update.message.reply_text("🚨🚨🚨🚨🚨 los creditos no coinciden("+y+")")

#         except:
#           update.message.reply_text(words[2]+" y "+words[3]+' deberia ser un numero')    
#       else:
#         update.message.reply_text("no se ecuentra el servicio") #poner lista de servicios

# def sum(update: Update, context: CallbackContext):
#       words = update.message['text'].split()
#       message = "Comando incorrecto"
#       if len(words)<3:
#         update.message.reply_text(message)
#       elif (words[1] in creditsValues):
#         credO = db.getCredByModel(words[1])
#         try:
#             credc = float(words[2])
#             y=str(float(credO)+credc)
#             db.update(words[1],float(credO)+credc)
#             update.message.reply_text("quedan "+y+' creditos')
#         except:
#           update.message.reply_text(words[2]+" y "+words[3]+' deberia ser un numero')    
#       else:
#         update.message.reply_text("no se ecuentra el servicio") #poner lista de servicios


# def set(update: Update, context: CallbackContext):
#       words = update.message['text'].split()
#       message = "Comando incorrecto"
#       if len(words)<3:
#         update.message.reply_text(message)
#       elif (words[1] in creditsValues):
#         try:
#             x = float(words[2])
#             db.update(words[1],x)
#             update.message.reply_text("Actualizado correctamente")
#         except:
#           update.message.reply_text(words[2]+' deberia ser un numero')    
#       else:
#         update.message.reply_text("no se ecuentra el servicio") #poner lista de servicios
      
      
def main():
  ############################# Handlers #########################################
  updater = Updater(TOKEN, use_context=True)

  dp = updater.dispatcher

  dp.add_handler(CommandHandler('start', start))
  dp.add_handler(CommandHandler('help', help))
  dp.add_handler(CommandHandler('cred', calc))
  dp.add_handler(CommandHandler('dolar', dolar))
  # dp.add_handler(CommandHandler('rest', rest))
  # dp.add_handler(CommandHandler('set', set))
  # dp.add_handler(CommandHandler('sum', sum))
  # initializeDB()

  updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
  updater.bot.setWebhook('https://vipcellcreditos-bot.herokuapp.com/' + TOKEN)

  updater.start_polling()
  updater.idle()
  ################################################################################

if __name__ == '__main__':
    main()
