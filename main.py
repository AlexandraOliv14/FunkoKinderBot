import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from config import TOKEN
from db.consultas import getCodeBackNumByCodes, getCodeBackByFront, getBackCodesByBackCodeNumber, getBackCodesCode, getFunkos, getcodesByNameVersion, getVersions, getFrontCodes, getCodesNamesByFrontCode, getBackCodes, getCodesNamesByBackCode, nameByCodes

bot = telebot.TeleBot(token=TOKEN)

# Manejador correspondiente al comando /inicio o /start
@bot.message_handler(commands=['start','inicio'])
def start(message):
    response = """ 
    ¡Bienvenido! :3

    🔹 **Comandos disponibles**:
    - `/start` o `/inicio`: Muestra un mensaje de bienvenida.
    - `/search` o `/busqueda`: Realiza una busqueda completa.
    - `/funkos`: Muestra una lista de Funkos disponibles junto con sus versiones como botones interactivos.
    - `/versions` o `/versiones`: Muestra una lista de versiones disponibles.
    - `/frontcode` o `/codigofrontal`: Muestra una lista de códigos frontales disponibles como botones interactivos.
    - `/backcode` o `/codigotrasero`: Muestra una lista de códigos traseros disponibles como botones interactivos.

    Si se escribe un mensaje con "codigo_frontal codigo_trasero" entregara los funkos que esta asociado al conjunto de los codigos.

    """
    bot.reply_to(message,response) # Respondemos al comando con el mensaje
    print('start')

# Manejador correspondiente al comando /versions o /versiones
@bot.message_handler(commands=['versions','versiones'])
def versions(message):
    response ="";
    list = getVersions()
    for i in list:
        response +=  f"version {i[0]} : {i[1]}\n"

    bot.reply_to(message,response) # Respondemos al comando con el mensaje
    print('versions')

# Manejador correspondiente al comando /frontcode o /codigofrontal
@bot.message_handler(commands=['frontcode','codigofrontal'])
def codeFront(message):
    list = getFrontCodes()
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(i[0], callback_data=f"frontcode_{i[0]}") for i in list]
    
    # Añadir botones al markup en filas de 3
    markup.add(*buttons)

    bot.reply_to(message,"Elige un comando para ejecutar:",reply_markup=markup) # Respondemos al comando con el mensaje
    print('frontcode')

@bot.callback_query_handler(func=lambda call: call.data.startswith('frontcode_'))
def handle_codefront_callback(call):
    code = call.data.split('frontcode_')[1]
    list = getCodesNamesByFrontCode(code)
    response = ""
    for item in list:
        response += f"funko {item[0]} : codigo {item[1]}{item[2]} \n"
    bot.send_message(call.message.chat.id, response)

@bot.message_handler(commands=['backcode','codigotrasero'])
def codeback(message):
    list = getBackCodesCode()
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(i[0], callback_data=f"backcode_{i[0]}") for i in list]
    markup.add(*buttons)

    bot.reply_to(message,"Elige un comando para ejecutar:",reply_markup=markup) # Respondemos al comando con el mensaje
    print('backcode')

@bot.callback_query_handler(func=lambda call: call.data.startswith('backcode_'))
def handle_codeback_callback(call):
    code = call.data.split('backcode_')[1]
    list = getBackCodesByBackCodeNumber(code)
    markup = InlineKeyboardMarkup(row_width=6)
    buttons = [InlineKeyboardButton(i[0], callback_data=f"backcodeName_{code}:{i[0]}") for i in list]
    markup.add(*buttons)
    bot.send_message(call.message.chat.id,text='Seleccione el codigo numerico', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('backcodeName_'))
def handle_codeback_callback(call):
    code = call.data.split('backcodeName_')[1]
    code = code.split(':')
    list = getCodesNamesByBackCode(code[1],code[0])
    response = ""
    for item in list:
        response += f"funko {item[0]} : codigo {item[1]} \n"
    bot.send_message(call.message.chat.id,response)

@bot.message_handler(commands=['funkos','funkos'])
def funkos(message):
    list = getFunkos()
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(f"{i[0]} - v{i[1]}", callback_data=f"funkos_{i[0]}_v{i[1]}") for i in list]
    markup.add(*buttons)

    bot.reply_to(message,"Elige un comando para ejecutar:",reply_markup=markup) # Respondemos al comando con el mensaje
    print('funkos')

@bot.callback_query_handler(func=lambda call: call.data.startswith('funkos_'))
def handle_funkos_callback(call):
    code = call.data.split('funkos_')[1]
    codeList = code.split('_v')
    list = getcodesByNameVersion(codeList[0],codeList[1])
    response = f"{code} \n"
    for item in list:
        response += f"codigo frontal {item[0]}; codigo trasero {item[1]}{item[2]}  \n"
    bot.send_message(call.message.chat.id, response)

@bot.message_handler(commands=['search','busqueda'])
def search(message):
    list = getFrontCodes()
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(i[0], callback_data=f"search1_{i[0]}") for i in list]
    
    # Añadir botones al markup en filas de 3
    markup.add(*buttons)

    bot.reply_to(message,"Elige un codigo frontal:",reply_markup=markup) # Respondemos al comando con el mensaje
    print('search')

@bot.callback_query_handler(func=lambda call: call.data.startswith('search1_'))
def handle_search1_callback(call):
    code = call.data.split('search1_')[1]
    list =  getCodeBackByFront(code)
    markup = InlineKeyboardMarkup(row_width=3)
    buttons = [InlineKeyboardButton(i[0], callback_data=f"search2_{code},{i[0]}") for i in list]
    
    # Añadir botones al markup en filas de 3
    markup.add(*buttons)

    bot.reply_to(call.message,"Elige un codigo trasero:",reply_markup=markup) # Respondemos al comando con el mensaje
    print('search1')

@bot.callback_query_handler(func=lambda call: call.data.startswith('search2_'))
def handle_search2_callback(call):
    code = call.data.split('search2_')[1]
    codeSep = code.split(',')
    list =  getCodeBackNumByCodes(codeSep[0],codeSep[1])
    markup = InlineKeyboardMarkup(row_width=6)
    buttons = [InlineKeyboardButton(i[0], callback_data=f"search3_{code},{i[0]}") for i in list]
    
    # Añadir botones al markup en filas de 3
    markup.add(*buttons)

    bot.reply_to(call.message,"Elige el numero del codigo trasero:",reply_markup=markup) # Respondemos al comando con el mensaje
    print('search2')

@bot.callback_query_handler(func=lambda call: call.data.startswith('search3_'))
def handle_search3_callback(call):
    code = call.data.split('search3_')[1]
    codeSep =code.split(',')
    list= nameByCodes(codeSep[0], codeSep[2], codeSep[1])
    if(len(list)==0):
        bot.reply_to(call.message, "El codigo no se encuentra en la base de datos")
    else:
        response = ""
        for item in list:
            response += f"funko {item[0]}, version {item[1]}  \n"
            
        bot.reply_to(call.message, response)
    print('search3')

@bot.message_handler(func=lambda message: True)
def handle_text_message(message):
    codes = message.text.lower().split(' ')

    if(len(codes)==2):
        list= nameByCodes(codes[0], codes[1][1:-2], codes[1][-2:])
        if(len(list)==0):
            bot.reply_to(message, "El codigo no se encuentra en la base de datos")
        else:
            response = ""
            for item in list:
                response += f"funko {item[0]}, version {item[1]}  \n"
                
            bot.reply_to(message, response)
    else:
        bot.reply_to(message,"codigos no validos")


while True:
    try:
        bot.polling(none_stop=True, interval=0, timeout=20)
        time.sleep(60)
    except Exception as e:
        print(f"Error: {e}")
        time.sleep(15)
