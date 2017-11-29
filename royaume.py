#!/usr/bin/python
#encoding: utf-8 
#------------------Le Royaume--------------------#

#creerRoyaume: -> Royaume
#Cette fonction crée un royaume vide 
#Post: un royaume est créée et il est vide
def creerRoyaume():

	return 0

#royaumeVide: Royaume -> bool
#Resultat: Verifie si le royaume r passé en paramètre est vide
def royaumeVide(r):

	return 0

#addCarteRoyaume: Royaume x Carte  -> Royaume
#Resultat: Cette fonction ajoute une carte au royaume r passé en paramètre, post : cette fonction incrémentera également le total des cartes du royaume r mais 
# aussi le total des cartes du type de carte en question
#Post: une carte est ajouté au royaume et le nombre du "typeCarte" contenu dans le royaume est incrémenté de 1
def addRoyaumeCarte(r,c):
	
	#Post: getNbCarteRoyaume(r) = getNbCarteRpyaume(r) + 1

	return 0

#removeCarteRoyaume: Royaume x Carte -> Royaume
#Cette fonction supprime  une carte c du royaume r 
def removeRoyaumeCarte(r,c):
	#Post: getNbCarteRoyaume(r) = getNbCarteRpyaume(r) - 1

	return 0

#getRoyaumeCarte : Royaume x Chaine de caractere -> Carte
#Resultat:cette fonction renvoie la carte (ou une des cartes si jamais il y en a plusieurs) correspondant à la chaine de caracteres si elle appartient au royaume r
#Post: une Carte correspondant à la chaine de caractere est retournée
def getRoyaumeCarte(m,s):
	#Pre : La chaine reçue en paramètre doit être une des valeurs suivantes : "Archer", "Soldat", "Garde", "Roi1", "Roi2"

	return 0

#getNbCarteRoyaume: Royaume -> Int
#Resultat: Retourne le nombre total de carte présente :O si vide, >=1 si non vide
def getNbCarteRoyaume(r):

	return 0

#getNbSoldats: Royaume -> Int
#Resultat: Retourne le nombre de carte de type Soldats dans le royaume r:O si vide, >=1 si non vide
def getNbSoldats(r):

	return 0

#getNbGardes: Royaume -> Int
#Resultat: Retourne le nombre de carte de type Gardes dans le royaume r:O si vide, >=1 si non vide
def getNbGardes(r):

	return 0

#getNbArchers: Royaume -> Int
#Resultat: Retourne le nombre de carte de type Archers dans le royaume r:O si vide, >=1 si non vide
def getNbArchers(r):

	return 0


#affichageRoyaume: Royaume -> chaine de caractere
#Résultat: Renvoie une chaine de caractere avec le nombre d'archers, de gardes, de soldats et de roi dans le royaume.
def affichageRoyaume(r):
	return 0
