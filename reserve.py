#!/usr/bin/python
#encoding: utf-8 

#------------------La réserve--------------------#

#creerReserve: -> Reserve
#Resultat: Cette fonction crée une reserve vide 
#Post: une reserve vide est crée
def creerReserve():

	return 0

#reserveVide: Reserve -> bool
#Resultat: Verifie si la réserve r est vide. True si vide, False sinon
def reserveVide(r):

	return 0
	
#addReserve: Reserve x Carte -> Reserve
#Resultat: Ajoute la carte c dans la reserve r à la fin de la réserve
#Post: une cart est ajoutée à la reserve
def addReserve(r,c):
	#Post: getNbCarteReserve(r) = getNbCarteReserve(r) +1

	return 0

#removeReserve: Reserve -> Reserve
#Resultat: Retourne la reserve en ayant supprimer le premier element de la reserve
#Post: la premiere carte de la reserve est retirée
def removeReserve(r):
	#Pre: removeReserve() => not(reserveVide())
	#Post: getNbCarteReserve(r) = getNbCarteReserve(r) -1

	return 0

#getPremierReserve: Reserve -> Carte
#Resultat: Retourne le prmeier élément de la réserve, Erreur si vide
#Post: Une carte est retournée
def getPremierReserve(r):

	return 0


#getNbCarteReserve: Reserve -> Int
#Resultat: Retourne le nombre de carte contenu dans la réserve: O si vide, >=1 si non vide
def getNbCarteReserve(r):

	return 0

#affichagePremierReserve: Reserve -> chaine de caractere
#Résultat: Renvoie une chaine de caractere avec la prmeière carte de la réserve.
#Post: une chaine de caractère est renvoyée similaire à : "Reserve : 'typeCarte'"
def affichagePremierReserve(r):
	return 0