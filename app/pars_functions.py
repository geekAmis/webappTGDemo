from bs4 import BeautifulSoup as bs
import requests

async def LoadProfilePhoto(username,path="./"):
	with open(f'{path}{username}.jpg','wb') as f:  f.write(requests.get(bs(requests.get(f'https://t.me/{username}').content,'html5lib').find('img',class_='tgme_page_photo_image').get('src')).content)

if __name__ == '__main__':
	LoadProfilePhoto('qurmancrypto')