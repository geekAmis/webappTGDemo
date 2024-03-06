import os
import sys
import time
import tqdm
import paramiko
from tqdm import tqdm

class SSHManager:
	def __init__(self, settings):
		self.ssh_host = settings["ssh_host"]
		self.ssh_port = settings["ssh_port"]
		self.ssh_username = settings["ssh_username"]
		self.ssh_password = settings["ssh_password"]
		self.remote_directory = settings["remote_directory"]
		self._remote_directory = settings["remote_directory"]

	def check_connection(self):
		transport = paramiko.Transport((self.ssh_host, self.ssh_port))
		try:
			transport.connect(username=self.ssh_username, password=self.ssh_password)
			print(f"Подключились к {self.ssh_username}@{self.ssh_host}:{self.ssh_port}")
			transport.close()
			print("Подключение прошло успешно.")
			return True
		except paramiko.AuthenticationException:
			print("Ошибка авторизации. Проверьте логин и пароль.")
			return False
		except paramiko.SSHException:
			print("Ошибка подключения. Проверьте адрес сервера и порт.")
			return False
		except Exception as e:
			print(f"Ошибка: {str(e)}")
			return False

	def rootpath(self):
		self.remote_directory = self._remote_directory

	def UploadAllFromPath(self, path):
		self.files_to_send = [os.path.join(path, filename) for filename in os.listdir(path) if os.path.isfile(os.path.join(path, filename))]
		return self.upload_files()

	def UploadSingleFile(self, file_name):
		self.files_to_send = [file_name]
		if os.path.isfile(file_name):
			return self.upload_files()
		else:
			print(f"Файл {file_name} не найден.")
			return False

	def upload_files(self):
		if not self.files_to_send:
			print("Список файлов для отправки пуст.")
			return False

		transport = paramiko.Transport((self.ssh_host, self.ssh_port))
		try:
			transport.connect(username=self.ssh_username, password=self.ssh_password)
			sftp_client = paramiko.SFTPClient.from_transport(transport)

			with tqdm(total=len(self.files_to_send), unit=" файл", unit_scale=True, desc="Отправка файлов") as pbar:
				for file in self.files_to_send:
					file_name = os.path.basename(file)
					sftp_client.put(file, self.remote_directory + file_name)
					pbar.update(1)

			transport.close()
			print("Файлы успешно загружены на сервер.")
			return True

		except Exception as e:
			print(f"Ошибка: {str(e)}")
			transport.close()
			return False

	def create_directory_on_server(self, directory_name):
		transport = paramiko.Transport((self.ssh_host, self.ssh_port))
		try:
			transport.connect(username=self.ssh_username, password=self.ssh_password)
			ssh_client = paramiko.SSHClient()
			ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
			ssh_client.connect(hostname=self.ssh_host, port=self.ssh_port, username=self.ssh_username, password=self.ssh_password)

			stdin, stdout, stderr = ssh_client.exec_command(f"mkdir -p {self.remote_directory}{directory_name}")
			output_list = stdout.readlines()
			error_list = stderr.readlines()

			ssh_client.close()
			transport.close()

			if not output_list and not error_list:
				print(f"Каталог {directory_name} успешно создан на сервере.")
				return True
			else:
				print("Ошибка создания каталога на сервере.")
				return False

		except Exception as e:
			print(f"Ошибка: {str(e)}")
			return False

# Использование класса
server_settings = {
	"ssh_host": "",
	"ssh_port": 22,
	"ssh_username": "",
	"ssh_password": "",
	"remote_directory": "/var/www/fastuser/data/www/roadsafeai.ru/"
}

