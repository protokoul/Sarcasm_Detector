import os

path = str(os.getcwd())+"/ttt"

if os.path.isfile(path):
	size = os.path.getsize(path)
	print(size)
else:
	print("File does not exist")


