import threading
import time

def welcome():
	for x in range(0, 10):
		print('welcome1')

def welcome2():
	for x in range(0, 10):
		print('welcome2')



threading.Thread(target=welcome ).start()
welcome2()

