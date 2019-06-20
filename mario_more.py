Height=input("Height:")
Height=int(Height)

if Height<1 or Height >8:
	Height=("Wrong! Input The Height again: ")
elif type(Height)!=int:
	Height=("Wrong! Input The Height again: ")
		


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
	
