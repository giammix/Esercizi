class Tris:
	def __init__(self):
	 	self.l = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

	def pieno(self, x, y):
		return self.l[(x - 1) * 3 + y - 1] != " "
	
	def inserisci_la_giocata(self, x, y, g):
		self.l[(x - 1) * 3 + y - 1] = g

	def stampa_il_campo(self):
		print(self.l[0] + "|" + self.l[1] + "|" + self.l[2])
		print(self.l[3] + "|" + self.l[4] + "|" + self.l[5])
		print(self.l[6] + "|" + self.l[7] + "|" + self.l[8])
	
	def vittoria(self):
		if ((self.l[0] == self.l[1] and self.l[1] == self.l[2] and self.l[1] != " ") or
		(self.l[3] == self.l[4] and self.l[4] == self.l[5] and self.l[3] != " ") or
		(self.l[6] == self.l[7] and self.l[7] == self.l[8] and self.l[6] != " ") or
		(self.l[0] == self.l[3] and self.l[6] == self.l[3] and self.l[3] != " ") or
		(self.l[1] == self.l[4] and self.l[4] == self.l[7] and self.l[1] != " ") or
		(self.l[2] == self.l[5] and self.l[5] == self.l[8] and self.l[2] != " ") or
		(self.l[0] == self.l[4] and self.l[4] == self.l[8] and self.l[0] != " ") or
		(self.l[2] == self.l[4] and self.l[4] == self.l[6] and self.l[2] != " ")):
			return True
		else:
			return False






tris = Tris()	 	


for i in range(9):
	
	if i % 2 == 0:
		giocatore = "X"
	else:
		giocatore = "O" 
	#il giocatore sceglie la giocata
	mossa = input("Dove vuoi mettere la "+ giocatore +" (riga-colonna):")
	riga = int(mossa[0])
	colonna = int(mossa[1])
	
	while True:
		#controllo se è piena la casella
		if tris.pieno(riga, colonna) == True:
			print("posizione non disponibile!")
			mossa = input("Dove vuoi mettere la "+ giocatore +" (riga-colonna):")
			riga = int(mossa[0])
			colonna = int(mossa[1])
		else:
			break
	
	tris.inserisci_la_giocata(riga, colonna, giocatore)
	
	tris.stampa_il_campo()
	
	#controllo vittoria
	tris.vittoria()
	if tris.vittoria() == True:
		print("Bravo ha vinto " + giocatore + " !")
		exit()
		
print("Bel pareggio!!!")


