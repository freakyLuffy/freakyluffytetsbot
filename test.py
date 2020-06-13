from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

    
def quote(bot, update):
    url = 'https://anime-chan.herokuapp.com/api/quotes/random'
    r = requests.get(url)
    data = r.json()[0]
    new_text="_{}_".format(data['quote'])
    new_char="*{}*".format(data['character'])
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text= "Quote: "+new_text+'\n'+'\n'+" "+"*-*"+new_char,parse_mode='Markdown')

def main():
    updater = Updater('1182634958:AAGxl0bLQoP13Jygje3k9KfyOYTbwf04RJM')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('quote',quote))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
