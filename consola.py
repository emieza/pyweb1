#!/usr/bin/python3

# global vars
equips = [ "Cornellà", "Sant Boi", "Despí" ]
lliga = {}


def app():
	# entrem equips
	while True:
		equip = input("Introdueix nou equip: ")
		if equip == "":
			break
		equips.append(equip)
		print(equips)

	# iniciem lliga
	print("OK! Iniciem lliga")
	for local in equips:
		# creem diccionari
		lliga[local] = {}
		# omplim diccionari amb equips visitants
		for visitant in equips:
			# resultat buit, fins que no s'entri dades
			lliga[local][visitant] = None

	# introduim resultats
	while True:
		print("\n"+str(equips))
		local = input("Introdueix equip local")
		if local not in equips:
			print("ERROR en equip local. Torna a introduir")
			continue
		visitant = input("Introdueix equip visitant")
		if visitant not in equips:
			print("ERROR en equip visitant")
			continue
		gols_local = input("Gols equip local ("+local+")")
		gols_visitant = input("Gols equip visitant ("+visitant+")")
		# introduim punts
		lliga[local][visitant] = (gols_local,gols_visitant)

		# mostra resultats
		for local in lliga:
			for visitant in lliga[local]:
				if lliga[local][visitant] != None:
					print(local+" - "+visitant+" : "+str(lliga[local][visitant]))


# activem app
app()

