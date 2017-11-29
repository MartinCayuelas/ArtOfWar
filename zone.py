#!/usr/bin/python
#encoding: utf-8 


#-------Zones----------#
#creerZone: chaine de Caracteres -> Zone
#Resultat: Cette fonction crée une zone vide, "F1","F2", "F3", "A1","A2","A3"
#Post: Une zone vide est crée avec pour nom F1" ou "F2" ou "F3"ou "A1" ou "A2", ou "A3"
def creerZone(nomZone):
	return 0

#getZoneNom: Zone -> chaine de caracteres
#Resultat: Renvoi le nom de la Zone: exemple: A3
#Post: une chaine de caractere est retournée
def getZoneNom(z):

	return 0

#zoneVide: Zone -> bool 
#Resultat: Verifie si la zone z est vide 
def zoneVide(z):
	return 0

#addZoneCarte: Zone x Carte -> Zone
#Resultat: Ajoute une carte c sur la zone z
#Post: Une carte est ajoutée à la zone
def addZoneCarte(z,c):
#Pre: zoneVide(z) == True
#Post: la zone devient occupée
	return 0

#removeZoneCarte: Zone x Carte -> Zone
#Resultat: Supprime une carte c sur la zone z
#Post: une carte est supprimée d ela zone
def removeZoneCarte(z,c):
#Pre: zoneVide(z) == False
#Post: la zone devient Libre
	return 0

# getZoneCarte: Zone -> Carte
#Resultat: Renvoi la carte c contenu dans la zone
#Pre: !zoneVide(z)
#Post: Une carte est renvoyée
def getZoneCarte(z):
	return 0

#setZone: Zone -> Zone
#Resultat: Modifie la zone, si ajout d'une carte, zone devient occupée sinon devient libre
def setZone(z):
	return 0

#estDerriere: Zone -> bool
#Resultat: Verifie si la zone z est sur la ligne Arrière ("A1" ou ("A2" ou "A3")
def estDerriere(z):

	return 0

#estDevant: Zone -> bool
#Resultat: Verifie si la zone z est sur la ligne de Front ("F1" ou "F2" ou "F3")
def estDevant(z):

	return 0
#zoneDevant: Zone -> bool
#Resultat: Verifie si la zone devant z est libre
def zoneDevantVide(z):

	return 0