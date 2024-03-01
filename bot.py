from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import Update

import requests

TOKEN = "5955811135:AAGu7qDTCcz-ChbupcI-_CLiKxq2xjEj2OI"

bot = Bot(TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	markup = types.InlineKeyboardMarkup()
	markup.add(types.InlineKeyboardButton('Профиль',web_app=WebAppInfo(url='https://roadsafeai.ru/profile/')),types.InlineKeyboardButton('Админка*',web_app=WebAppInfo(url='https://roadsafeai.ru/bing/adminPage')))
	markup.add(types.InlineKeyboardButton('Категории',web_app=WebAppInfo(url='https://roadsafeai.ru/bing/categoryMenu')),types.InlineKeyboardButton('Билет в категории*',web_app=WebAppInfo(url='https://roadsafeai.ru/bing/search_buyTicket')))
	markup.add(types.InlineKeyboardButton('*Участие в билете',web_app=WebAppInfo(url='https://roadsafeai.ru/bing/currentLoteryJoin')),types.InlineKeyboardButton('*Лото билет',web_app=WebAppInfo(url='https://roadsafeai.ru/bing/ticket')))
	markup.add(types.InlineKeyboardButton('*Лото бочки',web_app=WebAppInfo(url='https://roadsafeai.ru/bing/bochki')))
	await message.answer('Меню бота',reply_markup=markup)

executor.start_polling(dp)