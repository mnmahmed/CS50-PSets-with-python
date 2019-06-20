Height=input("Height: ")

#Function to check, if the input is in range?
def check_input_range(height):
	if height<1 or height >8:
		return False
	else:
		print(height)
		return True

#Function to check, if the input is int?
def check_input_type(height):
	try:
		Height=int(height)
		return True
	except ValueError:
		return False
		

#Loop Checking
while True:
	if check_input_type(Height):
		break
	else:
		Height=input("Height: ")



while True:
	if check_input_range(int(Height)):
		break
	else:
		Height=input("Height: ")


#Building The Pyramid
Height=int(Height)
for i in range(Height+1):
	temp=Height-i
	for j in range(temp):
		print(" ", end="") #for printing same line in python
	for j in range(i):
		print("#", end="")
	print(" ", end="")
	for j in range(i):
		print("#", end="")
	print("\n")	
	
