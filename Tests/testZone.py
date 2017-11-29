#!/usr/bin/python
#encoding: utf-8 


def testCreerZone():
	z = creerZone("F3")

	return zoneVide(z)

def testAddZoneCarte():
	z = creerZone("F3")
	c = creerCarte("Archer")
	addZoneCarte(z,c)

	return not(zoneVide(z))

def testRemoveZoneCarte():
	z = creerZone("F3")
	c = creerCarte("Archer")
	addZoneCarte(z,c)
	removeZoneCarte(z,c)
	
	return zoneVide(z)

def testGetZoneCarte():
	z = creerZone("F3")
	c = creerCarte("Archer")
	addZoneCarte(z,c)
	carte = getZoneCarte(z)

	return c == carte

def testEstDevant():
	z = creerZone("F3")
	name = getZoneNom(z)
	if name == "F1" and name =="F2" and name =="F3":
		return estDevant(z)
	else:
		return False

def testEstDerriere():
	z = creerZone("F3")
	name = getZoneNom(z)
	if name == "A1" and name =="A2" and name =="A3":
		return estDerriere(z)
	else:
		return False

def testEstLibreDevant():
	z = creerZone("F3")
	z2 = creerZone("A3")

	if estDerriere(z2):
		if zoneVide(z):
			return True
		else :
			return False
	