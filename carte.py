#!/usr/bin/python
#encoding: utf-8 

#creerCarte: Chaine de caracteres -> Carte
#Resultat: Cette fonction créer une carte à partir du nom de la carte souhaitée reçu en paramètre typeCarte (: "Archer", "Soldat", "Garde", "Roi1", "Roi2") 
#Post: Une carte est créée suivant le typeCarte choisi avec une force d'attaque (un entier), une force de defense en mode Defensif (entier), une force de defence en mode Offensiff (entier) , une portée et une position (int: 2 car en mode defensif de base)
def creerCarte(typeCarte):
	#Pre: La chaine reçue en paramètre doit être une des valeurs suivantes : "Archer", "Soldat", "Garde", "Roi1", "Roi2"
	#La Position est soit un entier égal à 1 ou un entier égal à 2. De base à la création la carte est en mode defensif donc à position = 2

	return 0

#getCaracAttaque: Carte -> Int
#Resultat: Cette fonction renvoie la caractéristique "Attaque" d'une carte c passée en paramètre
#Post: La force de d'attaque est renvoyée
def getCaracAttaque(c):

	return 0

#getTypeCarte: Carte -> Chaine de caracteres
#Résultat: renvoie le type de la carte parmi "Archer", "Soldat", "Garde", "Roi1", "Roi2"
#Post: une chaine de caractère est renvoyée et elle est parmi "Archer", "Soldat", "Garde", "Roi1", "Roi2"
def getTypeCarte(c):
	
	return 0

#getCaracDefDefensive: Carte -> Int
#Resultat: Cette fonction renvoie la caractéristique "Defense en position défensive" d'une carte c passée en paramètre
#Post: La force de defense en mode defensif est renvoyée
def getCaracDefDefensive(c):

	return 0

#getCaracDefOffensive: Carte -> Int
#Cette fonction renvoie la caractéristique "Defense en position offensive" d'une carte c passée en paramètre
#Post: La force de defense en mode offensif est renvoyée
def getCaracDefOffensive(c):

	return 	0

#setCaracDefDefensive: Carte x Int -> Carte
#Resultat: Cette fonction modifie la caractéristique "Defense en position défensive" d'une carte c passée en paramètre
#Post: La force de defense en mode defensif est modifiée
def setCaracDefDefensive(c,i):

	return 0

#setCaracDefOffensive: Carte x Int -> Carte
#Cette fonction modifie la caractéristique "Defense en position offensive" d'une carte c passée en paramètre avec l'entier i
#Post: La force de defense en mode offensif est modifiée
def setCaracDefOffensive(c,i):

	return 	0

#portee: Carte x Carte -> bool
#Resultat: Cette fonction compare la position d'une carte c1 avec celle d'une carte c2, renvoie True si la carte c1 (attaquante) peut attaquer
#Post: Un booléen est renvoyé
def portee(c1,c2):

	return 0

#getPosition: Carte -> Int
#Resultat: Cette fonction renvoie la position de la carte c (passée en paramètre) soit defensive soit offensive (1 pour offensive, 2 pour deffensive)
#Post: Une position (defensive ou offensive) est renvoyée. cela doit être 1 ou 2
def getPosition(c):
	#Pre: La carte c est présente sur le Champ de bataille
	return 0

#setPosition: Carte -> Carte
#Resultat: Permet de modifier la position de la carte c sur le champ de bataille soit defensive soit offensive. Defensive devient offensive et vice-versa
#Post: La position est modifée
def setPosition(c):
	#Pre: La carte c est présente sur le Champ de bataille
	return 0





