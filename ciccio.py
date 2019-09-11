import random 

numcasuale = random.randint(1,100)
for i in range(10):
	k = int(input("Prova a indovinare un numero da 1 a 100:"))
	if k == numcasuale:
		print("Bravo, hai indovinato!!!")
		break
	elif k >= numcasuale:
		print("Ci sei quasi, prova con un numero più piccolo")
	else:
		print("Io proverei con un numnero più grande")
