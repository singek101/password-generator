import random


def password(length):
	passwrd = str()
	password_characters = 'abcdefghijklmnopqrstuvwxyz1234567890/<>#&?^%$'
	for i in range(length):
		passwrd = passwrd + random.choice(password_characters)
	print(passwrd)
	return passwrd

password() #input the password length inside the parenthesis
