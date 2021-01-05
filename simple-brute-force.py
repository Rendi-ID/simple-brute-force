#brute force
#Rendi Noober

print('\t[ 1 - 9999 ]')
password=str(input('Enter the password to crack: '))
guess=""
while(guess != password):
	guess=str(random.randint(0,9999))
	print('failed:', guess)
	if guess==password:
		print('password found:', guess)