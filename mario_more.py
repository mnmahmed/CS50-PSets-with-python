Height=8
Height=int(Height)

if Height<1 or Height >8:
	Height=("Wrong! Input The Height again: ")


for i in range(Height):
	temp=Height-i-1
	for j in range(temp):
		print(" ", end="")
	for j in range(i):
		print("#", end="")
	print(" ", end="")
	for j in range(i):
		print("#", end="")
	print("\n")	
	'''temp=f-i
	for j in range(temp):
		print(" ")
	for k in range(i):
		print("#")	'''
