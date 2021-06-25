# -*- coding: utf-8 -*-
import os 
import ctypes
from sys import exit
import json
import traceback
import sys
import logging
import shutil
import time


def show_msgbox(text, title):
	ctypes.windll.user32.MessageBoxW(0, text, title, 0)
	exit(0)

def get_version(path):
	for file in os.listdir(path):
		if 'version' in file.lower():
			return f'{path}/{file}/content/fonts'
	#if version not found
	logging("Get Version Error\n"+traceback.format_exc())
	show_msgbox('Version Not Found\nContact The Developer', 'Version Not Found')

def getall_dir(path):
	files = os.listdir(path)
	#return [files.lower() for files in files if os.path.isdir(f'{path}\\{files.lower()}')]
	return [files for files in files if '.ttf' in files or '.otf' in files]


def check_fonts():
	curdir = os.listdir(os.getcwd())   #[dirs.lower() for dirs in os.listdir(os.getcwd())]
	if 'font.ttf' not in curdir:
		logging("Font.ttf file in script directory not found")
		show_msgbox('Font.ttf file in script directory not found', 'Font.ttf not found')
	if 'font.otf' not in curdir:
		logging("Font.otf file in script directory not found")
		show_msgbox('Font.otf file in script directory not found', 'Font.otf not found')
	return f'{os.getcwd()}/font.ttf', f'{os.getcwd()}/font.otf', 


if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG, filename='error.log', format='%(asctime)s %(levelname)s:%(message)s', filemode="w")
	logging.info("Applicationg Run")
	current_username = os.getlogin()
	version_path = f'C:/Users/{current_username}/AppData/Local/Roblox/Versions'
	path = get_version(version_path)
	ttf, otf = check_fonts()
	fonts = getall_dir(path)
	for font in fonts:
		if '.otf' in font:
			shutil.copy(otf, path)
			os.remove(f'{path}/{font}')
			os.rename(f'{path}/Font.otf',f'{path}/{font}')
		if '.ttf' in font:
			shutil.copy(ttf, path)
			os.remove(f'{path}/{font}')
			os.rename(f'{path}/Font.ttf',f'{path}/{font}')
	show_msgbox('Font were changed successful', 'Success')




