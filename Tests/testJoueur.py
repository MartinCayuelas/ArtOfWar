#!/usr/bin/python
#encoding: utf-8 

def testCreerJoueur():
	
	j = creerJoueur()


	return getRoyaume(j) == None

def testgetPioche():

	j = creerJoueur()
	return getPioche(j)!= None

def testgetReserve():

	j = creerJoueur()
	return getReserve(j) == None

def testgetMain():

	j = creerJoueur()
	return getMain(j)== None

def testgetChampBataille():

	j = creerJoueur()
	return getChampBataille(j)== None

def testgetCimetiere():

	j = creerJoueur()
	return getCimetiere(j)== None
	