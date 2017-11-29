#!/usr/bin/python
#encoding: utf-8 

def testCreerChampDeBataille():
	z = creerZone("F1")
	z2 = creerZone("F2")
	z3 = creerZone("F3")
	z4 = creerZone("A1")
	z5 = creerZone("A2")
	z6 = creerZone("A3")
	CdB = creerChampDeBataille(z,z2,z3,z4,z5,z6)

	return champBatailleVide(CdB)

def testappartienCDB():
	z = creerZone("F1")
	z2 = creerZone("F2")
	z3 = creerZone("F3")
	z4 = creerZone("A1")
	z5 = creerZone("A2")
	z6 = creerZone("A3")
	CdB = creerChampDeBataille(z,z2,z3,z4,z5,z6)

	return appartientCdB(CdB,z4)

def testgetChampDeBatailleZone():
	z = creerZone("F1")
	z2 = creerZone("F2")
	z3 = creerZone("F3")
	z4 = creerZone("A1")
	z5 = creerZone("A2")
	z6 = creerZone("A3")
	CdB = creerChampDeBataille(z,z2,z3,z4,z5,z6)

	zest = creerZone("F3")
	zest2 = getChampBatailleZone(Cdb,"F3")
	return zest == zest2