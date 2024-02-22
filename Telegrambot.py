import telegram.ext 

def start(update, context):
    update.message.reply_text("Hello! Welcome to Vikash Code")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:
    
    /start -> Welcome to the channel
    /help -> This message
    /content -> vikash coders offers various courses free of course 
    /Python  -> The first video from Python Playlist
    /SQL -> The first video from SQL Playlist
    /Java -> The first video from Java Playlist
    /Skillup -> Free platform for certification by Simplilearn
    /contact -> contact information 
     """)
    
def content(update, context):
    update.message.reply_text("We have various playlists and articles available!")

def Python(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/7wnove7K-ZQ?si=5mId428e1XEj32Fd")

def SQL(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/pFq1pgli0OQ")
    
def Java(update, context):
    update.message.reply_text("tutorial link : https://youtu.be/ntLJmHOJ0ME?si=6NDmP107EFl1Y0HO")
    
def contact(update, context):
    update.message.reply_text("You can contact on the official mail id: vikashprofessional517@gmail.com")

def handle_message(update, context):
    update.message.reply_text(f"You said {update.message.text}, use the commands using /")


Token = ("7037423091:AAFAnNSlM_yNydPyK5ZZBul5K71XBg7znYk")
#print(bot.get_me())
updater = telegram.ext.Updater("7037423091:AAFAnNSlM_yNydPyK5ZZBul5K71XBg7znYk", use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.CommandHandler('content',content))
disp.add_handler(telegram.ext.CommandHandler('Python',Python))
disp.add_handler(telegram.ext.CommandHandler('SQL',SQL))
disp.add_handler(telegram.ext.CommandHandler('Java',Java))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()
