#!/usr/bin/python
#encoding: utf-8 

def testCreerMain():
	partie = creerPartie()
	joueur = joueurCourant(partie)

	m = getMain(joueur)
	carte = creerCarte("Roi1")

	if appartientMainCarte(m,carte):
		return True
	else:
		return False


def testCreerMain2():
	partie = creerPartie()
	joueur = joueurCourant(partie)
	joueur2 = joueurAdverse(partie,joueur)

	m = getMain(joueur2)
	carte = creerCarte("Roi2")

	if appartientMainCarte(m,carte):
		return True
	else:
		return False

def testAddMain():

	m = creerMain()
	carte = creerCarte("Soldat")
	nb = getNbCartesMain(m)
	addMain(m,carte)

	if getNbCartesMain(m) == nb +1:
		return True
	else:
		return False

def testRemoveMain():

	m = creerMain()
	carte = creerCarte("Soldat")
	addMain(m,carte)
	nb = getNbCartesMain(m)
	removeMain(m,carte)

	if getNbCartesMain(m) == nb - 1:
		return True
	else:
		return False

def testMainVide():
	
	m = creerMain()
	return not(mainVide(m))

def  testGetnbCartesMain():
	m = creerMain()

	return getNbCartesMain(m) == 4

def testGetMainCarte():
	m = creerMain()
	carte = creerCarte("Soldat")
	nb = getNbCartesMain(m)
	addMain(m,carte)
	c = getMainCarte("Soldat")

	return c == carte