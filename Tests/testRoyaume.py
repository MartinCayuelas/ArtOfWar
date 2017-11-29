#!/usr/bin/python
#encoding: utf-8

def testCreerRoyaume():
	r = creerRoyaume()

	return royaumeVide(r)

def testAddRoyaumeCarte():
	r = creerRoyaume()
	c= creerCarte("Soldat")
	nb = getNbCarteRoyaume(r)
	addRoyaumeCarte(r,c)

	if getNbCarteRoyaume(r) == nb +1:
		return True
	else:
		return False

def testremoveRoyaumeCarte():
	r = creerRoyaume()
	c= creerCarte("Soldat")
	addRoyaumeCarte(r,c)
	nb = getNbCarteRoyaume(r)
	removeRoyaumeCarte(r,c)

	if getNbCarteRoyaume(r) == nb - 1:
		return True
	else:
		return False

def testgetNbSoldats():
	r = creerRoyaume()
	c= creerCarte("Soldat")
	addRoyaumeCarte(r,c)

	return getNbSoldats(r) == 1

def testgetNbArcher():
	r = creerRoyaume()
	c= creerCarte("Archer")
	addRoyaumeCarte(r,c)

	return getNbArchers(r) == 1

def testgetNbGardes():
	r = creerRoyaume()
	c= creerCarte("Garde")
	addRoyaumeCarte(r,c)

	return getNbSGardes(r) == 1