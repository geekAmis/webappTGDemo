import os

Photo_PATH = 'UserPhotos'

if not os.path.exists(Photo_PATH):
	os.mkdir(Photo_PATH)