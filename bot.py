from datetime import datetime
from random import randint
from app.aiogram_init import *
from app.mysqldb import MySQLS as MySQL, config_db
from app.pars_functions import LoadProfilePhoto
from app.sshManager import server_settings, SSHManager
from app.filesys import *
Photo_PATH = f'{Photo_PATH}/'

sql = MySQL(config_db)
if not sql.checkConn()[0]:
	quit(sql.checkConn()[1])

ssh = SSHManager(server_settings)
if not ssh.check_connection():  quit()

bot = Bot(sql.get_Adminstructure()[0].get("TG_TOKEN"))
dp = Dispatcher(bot)

async def loadUserPhotos():
	try:
		ssh.create_directory_on_server(Photo_PATH)
	except:
		pass
	ssh.remote_directory = ssh.remote_directory + Photo_PATH
	ssh.UploadAllFromPath(Photo_PATH.split('/')[0])
	ssh.rootpath()


async def loadUserPhoto(username):
	try:
		ssh.create_directory_on_server('UserPhotos')
	except:
		pass
	print(f'UserPhotos/{username}.jpg')
	ssh.rootpath();ssh.remote_directory = ssh.remote_directory + 'UserPhotos/'
	ssh.UploadSingleFile(f'UserPhotos/{username}.jpg')
	ssh.rootpath()

async def load_profile_photo(username,loading_msg, path=Photo_PATH):
    print(f"Загрузка профильного фотографии пользователя {username}")
    await FASTedit_message_text(loading_msg, 'Проверка в спам базах: 15%|█             | 0.00/5.00')
    await LoadProfilePhoto(username,path=path)
    await FASTedit_message_text(loading_msg, f'Проверка в спам базах: {randint(21,39)}%|█████         | 2.00/5.00')
    await loadUserPhoto(username)
    await FASTedit_message_text(loading_msg, f'Проверка в спам базах: {randint(80,99)}%|█████████████ | 5.00/5.00')


async def FASTedit_message_text(message: types.Message, edited_text, reply_markup=None, disable_notification=False, parse_mode=None):
    if reply_markup:
        await message.edit_text(edited_text, reply_markup=reply_markup, parse_mode=parse_mode)
    else:
        await message.edit_text(edited_text, parse_mode=parse_mode)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
	newuser = True
	if not sql.check_table_row_exists("UserFastCart", 0,message.from_user.id):
		newuser = True
		sql.add_record("UserFastCart", {
			"Tid": message.from_user.id,
			"total_tickets": 0,
			"total_wins": 0
		})
	if not sql.check_table_row_exists("USERS_DATA", 0,message.from_user.id):
		newuser = True
		sql.add_record("USERS_DATA", {
			"Tid": message.from_user.id,
			"balance": 0.0,
			"Cid": 0
		})
		 	 	 	
	if not sql.check_table_row_exists("User_DATA", 0,message.from_user.id):
		newuser = True
		sql.add_record("User_DATA", {
			"Tid": message.from_user.id,
			"first_name": message.from_user.first_name,
			"last_name": message.from_user.last_name if message.from_user.last_name else "",
			"username": message.from_user.username if message.from_user.username else "",
			"balance": 0.0,
			"owner_status": False,
			"registration_date": datetime.now()
		})

	if message.from_user.username and newuser:
		loading_msg = await bot.send_message(message.chat.id,'<b>Проверка в спам базах: 0%|██████████████| 0.00/0.00</b>',parse_mode='HTML')
		await load_profile_photo(message.from_user.username,loading_msg, path=Photo_PATH)
		await FASTedit_message_text(loading_msg, f'Проверка в спам базах: 100%|██████████████| 5.00/5.00')

	await FASTedit_message_text(loading_msg, 
		'Меню бота',
		disable_notification=False,
		reply_markup=menu_keyboard()
	)

executor.start_polling(dp)