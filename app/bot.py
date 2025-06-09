import os
import requests
from dotenv import load_dotenv
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

BOT_TOKEN =os.getenv('BOT_TOKEN')
API_URL = os.getenv('API_URL')
bot=telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id,f'Привет {message.from_user.first_name}. Добро пожаловать в бот для чтения статей. Наберите команду /posts, чтобы получить каталог',parse_mode='html')

@bot.message_handler(commands=['posts'])
def send_posts(message):
    response=requests.get(f'{API_URL}/posts')
    posts=response.json()

    if not posts:
        bot.send_message(message.chat.id, 'Постов нету')
        return
    markup=InlineKeyboardMarkup()
    for p in posts:
        markup.add(InlineKeyboardButton(p['title'],callback_data=str(p['id'])))
    bot.send_message(message.chat.id, 'Выберете пост',reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def send_details(call):
    post_id=call.data
    response=requests.get(f'{API_URL}/posts/{post_id}')
    post=response.json()

    text=f'{post['main_text']}\n\nДата: {post['date']}'
    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text)
bot.polling()