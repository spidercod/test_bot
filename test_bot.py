from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

Token: Final= '6462721211:AAFZML_6fjlj2ahSfd2QZ_666dihMqY0KlE'
BOT_USERNAME: Final = '@hzed_bot'


#Command
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello!Thanks for chatting with me! I am a HZ!')



async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a HZ!Pleae type something so i can respond')



async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!')



#Responses
    
def handle_reponse(text: str) -> str:
    processed: str = text.lower()


    if 'hello' in processed:
        return 'Hey there!'
    if 'how are you' in processed:
        return 'I am good!'
    if 'crypto' in processed:
        return '''
Bitcoin : $42,155.45 
Ethereum: $2,267.11
Solona: $97.22
'''
    return 'I do not undestand what you wrote...' 



async def handle_massage(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type:str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"') 

    if message_type== 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_reponse(new_text)
        else:
            return
    else:
        response:str= handle_reponse(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(Token).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))


    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_massage))


    #Errors
    app.add_error_handler(error)


    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)