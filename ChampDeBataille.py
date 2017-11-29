#!/usr/bin/python
#encoding: utf-8 

#------------------Le champ de bataille----------#


#creerChampDeBataille: Zone x Zone x Zone x Zone x Zone x Zone -> ChampDeBataille
#Cette fonction crée un ChampDeBataille vide composé de 6 zones vides ("Sans cartes deployées dessus")
#"F1","F2","F3","A1","A2","A3"
#Post: un champdebataille est créé avec 6 zones vides nommées "F1","F2","F3","A1","A2","A3"
def creerChampDeBataille(z1,z2,z3,z4,z5,z6):

	return 0

#appartientCdB:  ChampDeBataille x Zone  -> bool
#Resultat: Verifie si la zone z est contenue dans le ChampDeBataille d'un joueur. True si vrai, False sinon
#Post: Un booleén est retourné
def appartientCdB(CdB,z):
	return 0

#champBatailleVide: ChampDeBataille -> bool
#Resultat: Verifie si le champ de bataille est vide. True si vide, False sinon
#Post: Un booleén est retourné
def champBatailleVide(CdB):
	return 0


#placementDebutTour : ChampDeBataille -> ChampDeBataille
#Resultat: cette fonction place toutes les unités du champ de bataille du joueur en position défensive
#Post: Toutes les unités du joueur sont maintenant en position defensive
def placementDebutTour(CdB):

	return 0


#getChampBatailleZone : ChampDeBataille x Chaine de caractere -> Zone
#Resultat:cette fonction renvoie la Zone correspondant à la chaine de caracteres s si elle appartient au ChampDeBAtaille CdB
#Post: une Zone correspondant à la chaine de caractere est retournée
def getChampBatailleZone(CdB,s):
	#Pre : La chaine reçue en paramètre doit être une des valeurs suivantes :  "A1""A2""A3""F1""F2""F3"

	return 0

#affichageChampDeBatille: ChampDeBataille -> chaine de Caracteres
#Resultat: affiche le champDe bataille avec les cartes qu'il contient: exemple: "A1: Archer", "A2: Vide", "A3: .."
def affichageChampDeBataille(Cdb):
	return 0

#attaquer: Carte x Carte -> Champ de Bataille
#Résultat: cette fonction permet d'appliquer une attaque d'une carte envers une autre si la portee le permet
#si l'attaque de l'unité du joueurcourant est strictement supérieure à la défense de l'unité du joueuradverse, alors l'unité du joueuradverse va dans son cimetière, et la zone qu'il occupait devient libre
#si l'attaque de l'unité du joueurcourant est égale à la défense de l'unité du joueuradverse, alors l'unité du joueuradverse va dans le royaume du joueurcourant, et la zone qu'il occupait devient libre
#si l'attaque de l'unité du joueurcourant est strictement inférieure à la défense de l'unité du joueuradverse, alors on affecte une nouvelle valeur à la défense de l'unité du joueuradverse, qui est égale à la valeur de sa défense d'origine-la valeur de l'attaque de l'unité du joueurcourant
#Post: Une attaque est effectuée et le champ de bataille est donc modifié
def attaquer(c1,c2):

	return 0

#finAttaque : ChampDeBataille -> ChampDeBataille
#Resultat: Cette fonction remet toutes les valeurs de défense de toutes les unités du Champdebataille du joueur à leur valeur d'origine
#Post: Chaque carte du ChampBataille a retrouvé sa valeur initiale pour ses caracteristiques deffensives
def finAttaque(CdB):

	return 0



