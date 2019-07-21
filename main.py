import time
import numpy as np
import os.path

import user
import intro

AllSearch=[]
AllSearch=np.array(AllSearch)
menu_checker = True
valid_answer = False
def menu():
	intro.firstime()
	global menu_checker
	global valid_answer
	while menu_checker == True:
		print ('[1] Search')
		print ('[2] Statistics')
		print ('[3] About')
		print ('[4] Contact Us')
		print ('[5] Exit')
		x = input ('Choose a number or type the word that represents the action you want to take! : ')
		xupper = x.upper()
		if x == '1' or xupper == 'SEARCH':
			username = input('Type your username : ')
			if os.path.exists(username+".txt"):
				user.welcome(username)
			search = input('Who is your favorite singer?')
			user.write_data(username, search)
			np.append(AllSearch, search)
			menu_checker = False
		elif x == '2' or xupper == 'STATISTICS':
			username = input('Type your username : ')
			user.read_data(username)
			menu_checker = False
		elif x == '3' or xupper == 'ABOUT':
			menu_checker = False
			print  ('This program has been created by : George, Alex and Nick. ')
			print ('© 2019 George,Alex and Nick All Rights Reserved.')
			time.sleep(1)
			print ('Returning to menu in 3 seconds!')
			time.sleep(1)
			print ('Returning to menu in 2 seconds!')
			time.sleep(1)
			print ('Returning to menu in 1 second!')
			time.sleep(1)
			menu_checker = True
		elif x == '4' or xupper == 'CONTACT US':
			print ('If you have any questions about this project feel free to contact us at : (email!)') 
			time.sleep(1)
			print ('Returning to menu in 3 seconds!')
			time.sleep(1)
			print ('Returning to menu in 2 seconds!')
			time.sleep(1)
			print ('Returning to menu in 1 second!')
			time.sleep(1)
		elif x == '5' or xupper == 'EXIT':
			menu_checker = False
			print ('Are you sure you want to exit? [Yes/No] ')
			z = input()
			zupper = z.upper()
			if zupper == 'YES':
				print ('Thank you for using our program we hope to see you again soon!')
				time.sleep(1)
				print('Exiting in 3 seconds!')
				time.sleep(1)
				print('Exiting in 2 seconds!')
				time.sleep(1)
				print('Exiting in 1 second!')
				time.sleep(1)
				exit()
			elif zupper == 'NO':
				print ('Returning to menu in 3 seconds!')
				time.sleep(1)
				print ('Returning to menu in 2 seconds!')
				time.sleep(1)
				print ('Returning to menu in 1 second!')
				time.sleep(1) 
				menu_checker = True
			else:
				valid_answer = True
				while valid_answer == True:
					print ('You can either answer with Yes or No.')
					z = input('Please give a valid answer! : ')
					zupper = z.upper()
					if zupper == 'YES':
						print ('Thank you for using our program we hope to see you again soon!')
						time.sleep(1)
						print('Exiting in 3 seconds!')
						time.sleep(1)
						print('Exiting in 2 seconds!')
						time.sleep(1)
						print('Exiting in 1 second!')
						time.sleep(1)
						exit()
					elif zupper == 'NO':
						print ('Returning to menu in 3 seconds!')
						time.sleep(1)
						print ('Returning to menu in 2 seconds!')
						time.sleep(1)
						print ('Returning to menu in 1 second!')
						time.sleep(1)
						menu_checker = True
						valid_answer = False
		
menu()