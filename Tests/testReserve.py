#!/usr/bin/python
#encoding: utf-8 

def testCreerReserve():

	r = creerReserve()

	return reserveVide(r)

def testAddReserve():
	r = creerReserve()
	c = creerCarte("Soldat")
	
	nb = getNbCarteReserve(r)

	addReserve(r,c)
	if getNbCarteReserve(r) == nb +1:
		return True
	else :
		return False

def testremoveReserve():
	r = creerReserve()
	c = creerCarte("Soldat")
	addReserve(r,c)
	nb = getNbCarteReserve(r)
	removeReserve(r)
	if getNbCarteReserve(r) == 0:
		return True
	else :
		return False

def testGetNbCartesReserve():
	r = creerReserve()
	c = creerCarte("Soldat")
	c2 = creerCarte("Soldat")
	addReserve(r,c)
	addReserve(r,c2)
	nb = getNbCarteReserve(r)
	
	if getNbCarteReserve(r) == 2:
		return True
	else :
		return False

def testgetPremierReserve():
	r = creerReserve()
	c = creerCarte("Soldat")
	addReserve(r,c)

	carte = getPremierReserve(r)
	if getTypeCarte(carte) == "Soldat" :
		return True
	else :
		return False