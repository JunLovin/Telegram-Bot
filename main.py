from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6401158693:AAH5RusA3Er1GKlAvDJqo1F8XNLE0wOhCw0'
BOT_USERNAME: Final = '@Fuxionbot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hola! Gracias por estar interesado en FuXion, espero que te sirva mi ayuda!')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Soy el bot de Fuxion, pregunta algo para que pueda responder')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Este es un comando personalizado')
    
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Soy un bot creado por @junlovin y mi deber es ayudar a todas las personas que están interesadas en nuestra empresa!')
    
async def catalogo_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Puedes encontrar el catálogo de FuXion con todos los precios aquí: https://drive.google.com/file/d/1HZvBch3Uv7vLcS6ZhA-uExnKfbyL2Ivy/view')


# Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hola' in processed:
        return 'Holaaaaaaaa!'
    
    if 'como estas' in processed:
        return 'Excelente y tu'
    
    if 'amo python' in processed:
        return 'Yo estoy programado en python!'
    
    return 'No entiendo que quieres escribir...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
        
    print('Bot:', response)
    await update.message.reply_text(response)
    

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    
    
if __name__ == '__main__':
    print('Iniciando bot...')
    app = Application.builder().token(TOKEN).build()
    
    # Commands
    app.add_handler(CommandHandler('iniciar', start_command))
    app.add_handler(CommandHandler('ayuda', help_command))
    app.add_handler(CommandHandler('personalizado', custom_command))
    app.add_handler(CommandHandler('catalogo', catalogo_command))
    app.add_handler(CommandHandler('info', info_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Error
    app.add_error_handler(error)
    
    # Polls the bot
    print('Sondeando el bot...')
    app.run_polling(poll_interval=3)