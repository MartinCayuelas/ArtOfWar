#!/usr/bin/python
#encoding: utf-8 

def testCreerPartie():
	p = creerPartie()
	joueur = joueurCourant(p)
	m = getMain(joueur)
	nb = getNbCartesMain(m)

	return nb == 4

def testCreerPartie():
	p = creerPartie()
	joueur = joueurCourant(p)
	r = getRoyaume(joueur)

	return royaumeVide(r)

def testJoueur():
	p = creerPartie()
	j = joueurCourant(p)
	j2 = joueurAdverse(p, joueur)

	return j != j2