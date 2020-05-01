from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import setings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                     level=logging.INFO,
                     filename=r'D:\ProjectCoursera\projects\simplebot\bot.log')

def greet_user(update, context):
    text = "\start"
    logging.info(text)
    update.message.reply_text(text=text)

def talk_me(update, context):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info('User: %s, Chat id: %s, Message: %s', update.message.chat.first_name,
                                    update.message.chat.id,update.message.text
                                    )
    update.message.reply_text(text=user_text)

def main():
    mybot = Updater(setings.API_KEY, use_context=True, request_kwargs=setings.PROXY)
    
    logging.info('Bot strated')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_me))


    mybot.start_polling() #говорим слушать сервер
    mybot.idle() #не отключать до отмены





if __name__=="__main__":
    main()



