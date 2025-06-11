from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv
import os  

load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update, context):
    await update.message.reply_text("Hello! Welcome to the gym bot for gym information 😊. Type /information for details 💪")

async def information(update, context):
    await update.message.reply_text("""here the detail information 
 /machine type this for take detail about all machines 
 /exersises type this for take information about workout of body parts
 /homeworkout type this for home workout

 i hope it gona help you
 be stronger be powerfull💪 """)  # Add your actual info here
    
async def machine(update, context):
    await update.message.reply_text("""
flat bench - for bench press or dumbell press
incline bench - for incline bench press or incline dumbell press
latpull down - for lats and back
smith machine - for all exersise 
precher - for biceps 
dumbells
rods
leg press - for leg                                                                        
""" ) 

async def exersises(update, context):
    await update.message.reply_text("""
please specify the body part:
                                    
/arms
/leg
/chest
/back
/shoulder
/abs                                                                                                                                                                                                                        
    """)   

async def homeworkout(update, context):
        await update.message.reply_text("""
here are some home exersises!

pushup
crunches
squats
skipping                                                                                                                                                                  
        """)    

def main():
    # For modern versions (v20.0+)
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('information', information))
    application.add_handler(CommandHandler('machine', machine))
    application.add_handler(CommandHandler('homeworkout', homeworkout))
    application.add_handler(CommandHandler('exersises', exersises))
    application.run_polling()

if __name__ == '__main__':
    main()