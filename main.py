import telebot
from telebot import types
from sql import *

bot = telebot.TeleBot('5426760478:AAFaaDf7G9X421DPaqCNwuTWmwN_tA_xm1E')
record = []


@bot.message_handler(commands=['start'])
def start_message(message):
  mess = ' '+f'<b>{message.from_user.first_name}</b>  Добро пожаловать в наш магазин👋\n' \
         f'⬇️В левом нижнем углу ты можешь воспользоваться меню↙️'
  bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['add'])
def add_cmd(message):
  global record
  msg = bot.send_message(message.chat.id,
                         'Введите название товара⬇️')
  bot.register_next_step_handler(msg, process_link_step)


def process_link_step(message):
  global record
  record.append(message.text)
  msg = bot.send_message(message.chat.id, 'Вставте ссылку на товар⬇️')
  bot.register_next_step_handler(msg, process_price_step)


def process_price_step(message):
  global record
  record.append(message.text)
  msg = bot.send_message(message.chat.id,
                         'Введите стоимость товара⬇️')
  bot.register_next_step_handler(msg, process_adding_data_in_db_step)


def process_adding_data_in_db_step(message):
  global record
  record.append(message.text)
  add(record)
  record = None
  bot.send_message(message.chat.id, 'Запись успешно добавлена!✅')


@bot.message_handler(commands=['view'])
def view_products(message):
  markup = types.InlineKeyboardMarkup()
  links = get_links()
  names = get_names()
  prices = get_prices()
  for i in range(len(names)):
    markup.add(types.InlineKeyboardButton(f'{names[i]} - {prices[i]}руб',
                                          url=links[i]))
  bot.send_message(message.chat.id, '📜Перед вами список доступных товаров📜',
                   reply_markup=markup)


@bot.message_handler(commands=['delete'])
def start_message(message):
  msg = bot.send_message(message.chat.id,
                         'Напишите название товара, который хотите удалить 🗑')
  bot.register_next_step_handler(msg, process_deleting_data_in_db_step)


def process_deleting_data_in_db_step(message):
  delete(message.text)
  bot.send_message(message.chat.id, 'Запись успешно удалена!✅')


bot.polling(none_stop=True)
