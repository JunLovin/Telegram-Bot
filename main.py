from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6401158693:AAH5RusA3Er1GKlAvDJqo1F8XNLE0wOhCw0'
BOT_USERNAME: Final = '@Fuxionbot'


# Commands
async def iniciar_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('¡Bienvenido! Espero que mi ayuda sea de tu agrado. Si eres nuevo en el tema de FuXion déjame presentar a nuestra empresa rápidamente.\nFuxion es un empresa internacional la cual brinda de productos nutracéuticos, esto quiere decir que todos nuestros productos son totalmente orgánicos y no tienen ningún tipo de preservante o químico dañino para el cuerpo.\n\nPuedes escribir los siguientes comandos para saber más de los productos y de la empresa:\n\n/start - Te da una mini información de la empresa y te muestra todos los comandos existentes.\n/iniciar - Te da una bienvenida a FuXion y me presento.\n\n𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐜𝐢𝐨́𝐧\n/info - Te doy información acerca de mí, de mi propósito y de mi creador.\n/catalogo - Te manda un link de Google Drive en el cual está todo el catálogo de los productos FuXion con sus precios.\n/fuxion - Información acerca de la empresa y de cómo nuestros productos funcionan en el sistema humano.\n/nutraceutico - Te da un resumen de lo que son los productos nutracéuticos.')

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hola! Gracias por estar interesado en FuXion, espero que te sirva mi ayuda!')
    
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Soy el bot de Fuxion, pregunta algo para que pueda responder')
    
async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Este es un comando personalizado')


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
    app.add_handler(CommandHandler('start', iniciar_command))
    app.add_handler(CommandHandler('iniciar', start_command))
    app.add_handler(CommandHandler('ayuda', help_command))
    app.add_handler(CommandHandler('personalizado', custom_command))
    app.add_handler(CommandHandler('catalogo', catalogo_command))
    app.add_handler(CommandHandler('info', info_command))
    app.add_handler(CommandHandler('fuxion', fuxion_command))
    app.add_handler(CommandHandler('nutraceutico', nutraceutico_command))
    
    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Error
    app.add_error_handler(error)
    
    # Polls the bot
    print('Sondeando el bot...')
    app.run_polling(poll_interval=3)