#!/usr/bin/python
#encoding: utf-8 

#Creation

def testCreerCarte():
	c = creerCarte("Archer")
	return getTypeCarte == "Archer"

#Carac Attaque
def testCaracAttaqueArcher():
	c = creerCarte("Archer")
	return getCaracAttaque(c) == 1

def testCaracAttaqueGarde():
	c2 = creerCarte("Garde")
	return getCaracAttaque(c2) == 1

def testCaracAttaqueRoi1():
	r1 = creerCarte("Roi1")
	return getCaracAttaque(r1) == 1

def testCaracAttaqueRoI2():
	r2 = creerCarte("Roi2")
	return getCaracAttaque(r2) == 1

#Carac DefDefensive	

def testCaracDefDefArcher():
	c = creerCarte("Archer")
	return getCaracDefDefensive(c) == 2

def testCaracDefDefGarde():
	c = creerCarte("Garde")
	return getCaracDefDefensive(c) == 3

def testCaracDefDefSoldat():
	c = creerCarte("Soldat")
	return getCaracDefDefensive(c) == 2

def testCaracDefDefRoi1():
	c = creerCarte("Roi1")
	return getCaracDefDefensive(c) == 4

def testCaracDefDefRoI2():
	c = creerCarte("Roi2")
	return getCaracDefDefensive(c) == 5

#Carac DefOffensive

def testCaracDefOffArcher():
	c = creerCarte("Archer")
	return getCaracDefOffensive(c) == 1

def testCaracDefOffGarde():
	c = creerCarte("Garde")
	return getCaracDefOffensive(c) == 2

def testCaracDefOffSoldat():
	c = creerCarte("Soldat")
	return getCaracDefOffensive(c) == 1

def testCaracDefOffRoi1():
	c = creerCarte("Roi1")
	return getCaracDefOffensive(c) == 4

def testCaracDefOffRoI2():
	c = creerCarte("Roi2")
	return getCaracDefOffensive(c) == 4

#getPosition

def testGetPosition():
	c = creerCarte("Roi1")
	return getPosition(c) == 2

#setPosition
def testSetPosition():
	c = creerCarte("Roi2")
	setPosition(c)
	return getPosition(c) == 1

def testPouvoirAttaquer():
	c = creerCarte("Roi1")

	if getPosition(c) == 1 :
		return False
	else:
		return True
