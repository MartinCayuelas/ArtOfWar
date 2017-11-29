#!/usr/bin/python
#encoding: utf-8 

#------------------La main-----------------------#
#creerMain: -> Main 
#Résultat: Cette fonction crée une main de 3 cartes piochées dans la pioche ainsi qu'un roi 
#Post: La main contient un roi et 3 autres cartes. 3 cartes ont été piochées dans la pioche
def creerMain():

	return 0


#addMain: Main x Carte -> Main
#Resultat:Ajoute la carte c à la main m si elle contient 4 cartes ou moins, sinon mets la carte c en réserve.
#Post: une carte  est ajoutée à la main m
def addMain(m,c):
	#Pre: addMain(m,c) => piocher(p)
	#Pre: addMain(m,c) => (getNbCartesMain(m) <= 4)
	#Si getNbCartesMain(m) >=5 => addReserve(r,c)
	#Post: getNbCartesMain(m) = getNbCartesMain(m) +1

	return 0

#removeMain:  Main x Carte  -> Main
#Resultat: Supprime une carte c de la main m
#Post: une carte  est supprimée de la main m
def removeMain(m,c):
	#Pre: removeMain(c,m) => not(mainVide())
	#Post: getNbCartesMain(m) = getNbCartesMain(m) -1

	return 0


#mainVide: Main -> bool
#Resultat: Verifie si la main m est vide
def mainVide(m):
	return 0

#getNbCartesMain: Main -> Int
#Resultat: Retoune le nombre de cartes dans la main m
#Post: un entier est retourné
def getNbCartesMain(m):

	return 0

#appartientMainCarte: Main x Carte  -> bool
#Resultat: Verifie si la carte c est contenue dans la main m. True si elle contient la carte, False sinon
def appartientMainCarte(m,c):
	return 0

#getMainCarte : Main x Chaine de caractere -> Carte
#Resultat:cette fonction renvoie la carte (ou une des cartes si jamais il y en a plusieurs) correspondant à la chaine de caracteres si elle appartient à la main m
#Post: une Carte correspondant à la chaine de caractere est retournée
def getMainCarte(m,s):
	#Pre : La chaine reçue en paramètre doit être une des valeurs suivantes : "Archer", "Soldat", "Garde", "Roi1", "Roi2"

	return 0

#afficheMain: Main -> string
#Résultat: Renvoie une chaine de caractere avec le nombre d'archers, de gardes, de soldats et de roi contenu dans la main.
#Post: Une chaine de caractère est retournée avec le nombre d'archers, de gardes, de soldats et de roi contenu dans la main.
def affichageMain(m):

	return 0