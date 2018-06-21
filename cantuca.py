def cantuca(nparticipantes):
	recoleccion=0
	costocantuca=3.25
	for i in range(nparticipantes):
		recoleccion+=float(input("Cuanto tienes: "))
	if(recoleccion>0):
		if((recoleccion/costocantuca)>=1):
			print("tenemos para ",int(recoleccion/costocantuca)," botellas y nos sobra ",(recoleccion/costocantuca)-int(recoleccion/costocantuca)," centavos")
		else:
		 print("será que venden la boteela por partes?")
	else:
		print("pta que sad")