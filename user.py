import time
import numpy as np


def user_in_host(input):
	
	filepath = "users/"+input+".txt"
	
	f = open(filepath,"w+")

	f.close()
	
def write_data(input, search):
	
	filepath = "users/"+input+".txt"
	f = open(filepath,"a")
	
	#writing data
	f.write(search+"\n")
	
	#closing the file
	f.close() 

def read_data(input):
	
	filepath = "users/"+input+".txt"
	
	f = open(filepath, "r")
	# import from txt as a numpy array
	myarray = np.genfromtxt(filepath,dtype='str')
	unique, counts = np.unique(myarray, return_counts=True)
	print (unique)
	print (counts)
	
	#closing the file
	f.close()


def welcome(username_input):
	usernames = []
	numbers = [0,1,2,3,4,5,6,7,8,9]
	program_running = 0
	username_checker = True
	username_checker2 = True
	digits = 0
	count = 0
	number_checker = True
	while username_checker == True:
		if username_input.isdigit():
			program_running == 1
			print ('You cant use only numbers, you need to use letters as well!')
			username_input = input('Type your username : ') 
		elif len(username_input) < 4 or len(username_input) > 25:
			print ('Your username must be at least 5 characters long, or 25 characters long, maximum')
			username_input = input('Type your username : ') 
		else:
			program_running == 0
			username_checker = False
	while program_running == 0:
		if  username_input not in  usernames:
			len_username_input = len(username_input)
			listed_username_input = list(username_input)
			usernames.append(username_input)
			print ('Your username has been successfully saved')
			print (usernames)
			user_in_host(username_input)
			username_checker2 = False
			break

		elif username_checker2 == True:
			print  ('This username is already being used by an other user, please choose a different username!')
			username_input = input('Type your username : ')
			while len(username_input) < 4 or len(username_input) > 25:
				print ('Your username must be at least 5 characters long, or 25 characters, maximum')
				username_input = input('Type your username : ') 
			while username_input.isdigit():
				print ('You cant use only numbers, you need to use letters as well!')
				username_input = input('Type your username : ')
