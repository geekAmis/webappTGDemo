from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types import Update
import mysql.connector
import requests

db_config = {
    "host": "localhost",
    "user": "",
    "password": "",
    "database": ""
}
connection = mysql.connector.connect(**db_config)

if connection.is_connected():
    cursor = connection.cursor()

    # Запрос данных из таблицы Adminstructure с указанными столбцами
    query = "SELECT TG_TOKEN, Balance, PAY_API, WebURL, Owners_Tids FROM Adminstructure"
    cursor.execute(query)

    # Чтение данных из курсора и формирование JSON-строки
    result = cursor.fetchall()
    data = []
    for row in result:
        data.append({
            "TG_TOKEN": row[0],
            "Balance": row[1],
            "PAY_API": row[2],
            "WebURL": row[3],
            "Owners_Tids": row[4]
        })

    print("JSON-строка:", data)

else:
    print("Ошибка подключения к базе данных MySQL.")
    quit()

connection.close()

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
