from telebot import TeleBot
from telebot.types import Message

app = TeleBot('5355299294:AAFu1ZtX4bwfYMgLQbVbfuHdy9fBRhgnVxI',parse_mode='HTML')

@app.message_handler(commands=['start'])
def new_member(m: Message):
    app.send_message(m.chat.id,f"Assalomu Alaykum <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a>!",)


@app.message_handler(content_types=['new_chat_members'])
def new_member(m: Message):
    app.send_message(m.chat.id,f"Assalomu Alaykum  Xush kelibsiz <a href='tg://user?id={m.from_user.id}'>{m.new_chat_members[-1].first_name}</a>!",)


app.infinity_polling()
