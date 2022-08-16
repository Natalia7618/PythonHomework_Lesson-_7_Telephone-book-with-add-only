from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import data

TOKEN = '5680876713:AAFgIG0iM2ldyt0T_nQpCpvyU7F90l5O5qk'
bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

STATE = None
PERSON_NAME = 1
PERSON_SURNAME = 2
PERSON_PHONE = 3
PERSON_DESC = 4

def text(update, context):
    global STATE
    if STATE == PERSON_NAME:
        return received_person_name(update, context)
    if STATE == PERSON_SURNAME:
        return received_person_surname(update, context)
    if STATE == PERSON_PHONE:
        return received_person_phone(update, context)
    if STATE == PERSON_DESC:
        return received_person_desc(update, context)

def received_person_name(update, context):
    global STATE
    try:
        context.user_data['person_name'] = update.message.text
        update.message.reply_text(f"Отлично! А теперь вводи фамилию...")
        STATE = PERSON_SURNAME
    except:
        update.message.reply_text("Ошибка ввода имени...")

def received_person_surname(update, context):
    global STATE
    try:
        context.user_data['person_surname'] = update.message.text
        update.message.reply_text(f"Отлично! Теперь вводи телефон...")
        STATE = PERSON_PHONE
    except:
        update.message.reply_text("Ошибка ввода фамилии...")

def received_person_phone(update, context):
    global STATE
    try:
        context.user_data['person_phone'] = update.message.text
        update.message.reply_text(f"Ты молодец! Осталось добавить только краткое описание...")
        STATE = PERSON_DESC
    except:
        update.message.reply_text("Ошибка ввода телефона...")

def received_person_desc(update, context):
    global STATE
    try:
        context.user_data['person_desc'] = update.message.text
        STATE = None
        person_name = context.user_data['person_name']
        update.message.reply_text(f'Супер! {person_name} добавлен/а в записную книжку')
        
        surname = context.user_data['person_surname']
        phone = context.user_data['person_phone']
        desc = context.user_data['person_desc']

        data.add_member_txt(person_name, surname, phone, desc)
        data.add_member_csv(person_name, surname, phone, desc)
    except:
        update.message.reply_text("Ошибка ввода описания...")

def start(update, context):
    global STATE
    context.bot.send_message(update.effective_chat.id, "Привет! Я твой личный телефонный справочник. Давай добавим контакт!")

    STATE = PERSON_NAME
    update.message.reply_text(f"Итак, давай начнем! Вводи имя...")

start_handler = CommandHandler('start', start)
text_handler = MessageHandler(Filters.text, text)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(text_handler)

print('server started')
updater.start_polling()
updater.idle()