#!/usr/bin/python
#encoding: utf-8 

from zone import *
from main import *
from reserve import *
from carte import *
from cimetiere import *
from partie import *
from pioche import *
from joueur import *
from royaume import *
from ChampDeBataille import *
from string import *
#------------------------initialisation de la Partie-------------------------------#
P=creerPartie() #Creation de la partie
#Affecte le joueur courant (Actif)
joueur=joueurCourant(P)
#place la première carte de la pioche dans le royaume du joueur courant
addRoyaumeCarte(getRoyaume(joueur),getPiocheCarte(getPioche(joueur)))
#permet d’enlever la première carte de la pioche
piocher(getPioche(joueur))
#On change de joueur
joueur=joueurCourant(changerJoueurCourant(P))
addRoyaumeCarte(getRoyaume(joueur),getPiocheCarte(getPioche(joueur)))
piocher(getPioche(joueur))
#On repasse au joueur 1 pour commencer la partie
joueur=joueurCourant(changerJoueurCourant(P))

affichageMain(joueurCourant) #affiche la main du joueur1

zone=input("Choisissez la zone dans laquelle vous devez placer une de vos unites que vous avez en main (F1, F2 ou F3) ")
carte=input("Choisissez une carte de votre main a placer sur la ligne de front de votre champ de bataille" )
cart = getMainCarte(getMain(joueur),carte)
z = getChampBatailleZone(getChampBataille(joueur),zone)
addZoneCarte(z,cart)
removeMain(getMain(joueur),cart)
print
#Tour du joueur 2
joueurCourant(changerJoueurCourant(P))
affichageMain(joueurCourant)
zone=input("Choisissez la zone dans laquelle vous devez placer une de vos unites que vous avez en main (F1, F2 ou F3) ")
carte=input("Choisissez une carte de votre main a placer sur la ligne de front de votre champ de bataille" )
cart = getMainCarte(getMain(joueur),carte)
z = getChampBatailleZone(getChampBataille(joueur),zone)
addZoneCarte(z,cart)
removeMain(getMain(joueur),cart)
print
#Tour joueur 1
joueurCourant(changerJoueurCourant(P))
affichageMain(joueurCourant)
carte=input(" Choisissez une carte de votre main a place dans votre réserve : ")
cart = getMainCarte(getMain(joueur),carte)
addReserve(getReserve(joueur),carte)
removeMain(getMain(joueur),carte)
print
#Tour joueur 2
joueurCourant(changerJoueurCourant(P))
affichageMain(joueurCourant)
carte=input(" Choisissez une carte de votre main a place dans votre réserve :")
cart = getMainCarte(getMain(joueur),carte)
addReserve(getReserve(joueur),carte)
removeMain(getMain(joueur),carte)
print


#Tour de jeu
partieTermine = False
gagnant = None
while not(partieTermine) :
    joueur=joueurCourant(changerJoueurCourant(P))
    #Les différents affichages du début de tour
    print("ChampDeBataille JoueurActif")
    affichageChampDeBataille(getChampBataille(joueur))
    print
    print("ChampDeBataille JoueurAdverse")
    affichageChampDeBataille(getChampBataille(joueurAdverse(P,joueur)))
    print
    print("Royaume JoueurActif:")
    affichageRoyaume(getRoyaume(joueur))
    print
    print("Royaume JoueurAdverse:")
    affichageRoyaume(getRoyaume(joueurAdverse(P,joueur)))
    print
    print("Reserve JoueurActif:")
    affichagePremierReserve(getReserve(joueur))
    print
    print("ReserveJoueurActif:")
    affichagePremierReserve(getReserve(joueur))

    #Phase 1
    placementDebutTour(getChampBataille(joueur)) #place toutes les unités du champ de bataille du joueur en position défensive
    addMain(getMain(joueur),getPiocheCarte(getPioche(joueur)))
    piocher(getPioche(joueur))

    #Un des cas de fin de partie
    if piocheVide(getPioche(joueur)) and piocheVie(getPioche(joueurAdverse(P,joueur))):
    	if getNbCarteRoyaume(getRoyaume(joueurCourant(P))) > getNbCarteRoyaume(getRoyaume(joueurAdverse(P,joueur))):
    		partieTermine = True
    		gagnant = joueurCourant(P)
    	else:
    		partieTermine = True
    		gagnant = joueurAdverse(P,joueur)
    		
    if not(partieTermine):		
		#Phase 2
	    if not(mainVide(getMain(joueur))) :
	        print(" Que voulez-vous faire ? ")
	        print(" 1 : ne rien faire ")
	        print(" 2 : mettre en reserve ")
	        print(" 3 : déployer une unite ")
	        print(" 4 : attaquer ")
	        choisir=input(" indiquez votre choix : ")
	        if choisir==2 :
	            affichageMain(getMain(joueur))
	            carteType=input("Choisissez une carte dans votre main: ")
	            carte = getMainCarte(getMain(joueur),carteType)
	            while not(appartientMainCarte(getMain(joueur),carte)):
	            	carteType = input("Choisissez une carte dans votre main: ")
	            	carte = getMainCarte(getMain(joueur),carteType)
	        	addReserve(getReserve(joueur),carte)
	        	removeMain(getMain(joueur),carte)
	        if choisir==3 :
	        	if not(reserveVide(getReserve(joueur))):
	        		deployer = False
	        		while not(deployer):
						choix = input("Choisissez la zone dans laquelle déployer l'unité: ")
						z = getChampBatailleZone(getChampBataille(joueur),choix)
						while not(appartientCdB(getChampBataille(joueur),z)):
							choix = input("Choisissez la zone dans laquelle déployer l'unité: ")
							z = getChampBatailleZone(getChampBataille(joueur),choix)
						if estDerriere(z):
							if zoneDevantVide(z):
								print("Pas possible, choisissez une autre zone.")
							else:
								carte = getPremierReserve(getReserve(joueur))
								if zoneVide(z):
									addZoneCarte(z,carte)
									removeReserve(getReserve(joueur))
									deployer = True
									
								else:
									cart = getZoneCarte(z)
									addReserve(getReserve(joueur),cart)
									addZoneCarte(z,carte)
									removeReserve(getReserve(joueur))
									deployer = True
						else:
							carte = getPremierReserve(getReserve(joueur))
							if zoneVide(z):
								addZoneCarte(z,carte)
								removeReserve(getReserve(joueur))
								deployer = True
								
							else:
								cart = getZoneCarte(z)
								addReserve(getReserve(joueur),cart)
								addZoneCarte(z,carte)
								removeReserve(getReserve(joueur))
						deployer = True
	        	else:
					affichageMain(getMain(joueur))
					carteType = input("Choisissez une carte dans votre main: ")
					carte = getMainCarte(getMain(joueur),carteType)
					while not(appartientMainCarte(getMain(joueur),carte)):
						carteType = input("Choisissez une carte dans votre main: ")
						carte = getMainCarte(getMain(joueur),carteType)

					deployer = False
					while not(deployer):
						choix = input("Choisissez la zone dans laquelle déployer l'unité: ")
						z = getChampBatailleZone(getChampBataille(joueur),choix)

						while not(appartientCdB(getChampBataille(joueur),z)):
							choix = input("Choisissez la zone dans laquelle déployer l'unité: ")
							z = getChampBatailleZone(getChampBataille(joueur),choix)

						if estDerriere(z):
							if zoneDevantVide(z):
								print("Pas possible, choisissez une autre zone.")
							else:
								if zoneVide(z):
									addZoneCarte(z,carte)
									removeMain(getMain(joueur),carte)
									
								else:
									cart = getZoneCarte(z)
									addReserve(getReserve(joueur), cart)
									addZoneCarte(z,carte)
									removeMain(getMain(joueur),carte)

								deployer = True
						else: 
							if zoneVide(z):
								addZoneCarte(z,carte)
								removeMain(getMain(joueur),carte)		
							else:
								cart = getZoneCarte(z)
								addReserve(getReserve(joueur), cart)
								addZoneCarte(z,carte)
								removeMain(getMain(joueur),carte)

							deployer = True

				
	        if choisir==4 :
	           	affichageMain(joueur)
	    		for i in (getChampBataille(joueur)):
					if not(zoneVide(i)):
						carte1=getZoneCarte(i)
						getCaracAttaque(carte1)
						getCaracDefOffensive(carte1)
						getCaracDefDefensive(carte1)
						getChampBataille(joueurAdverse(P,joueur))
						for j in (getChampBataille(joueurAdverse(P,joueur))): #permet de déterminer le nombre de carte que carte1 peut attaquer
							a=0
							zone=0
							if portee(carte1,getZoneCarte(j)) and not(zoneVide(getZoneCarte(j))):
								a=a+1
								zone=zone+","+getZoneNom(getZoneCarte(j))
								if zone!=0:
									print("Les zones {0} peuvent être attaquées.".format(zone)) #{0} permet d'afficher les zones qui peuvent être attaquées.
								else:
									print("Tu ne peux pas attaquer avec cette carte.")
						if a!=0:
							print("Vous pouvez attaquer"+a+"cartes. Voulez-vous attaquer avec votre carte une de ces cartes? Répondez par True si oui, sinon par False.")
							rep=input()
							if rep:
								res=False
								while not(res):
									choix=input("Choisissez une zone dans laquelle vous pouvez attaquer l'unité de votre adversaire :")
									choixZone=getChampBatailleZone(getChampBataille(joueur),choix)
									while not(appartientCdB(getChampBataille(joueurAdverse(P,joueur)),choixZone)) and not(choix in zone):
										print("Votre carte ne peut pas attaquer sur cette zone. Il faut rechoisir une zone.")
										choix=input("Choisissez une zone dans laquelle vous pouvez attaquer l'unité de votre adversaire :")
										choixZone=getChampBatailleZone(getChampBataille(joueur),choix)
									setPosition(carte1)
									attaquer(carte1,getZoneCarte(choixZone))
									res=True
							if getTypeCarte(getZoneCarte(choixZone))=='Roi1' or getTypeCarte(getZoneCarte(choixZone))=='Roi2':
								if (getTypeCarte(getZoneCarte(choixZone)) in getCimetiere(joueurAdverse(P,joueur))) or (getTypeCarte(getZoneCarte(choixZone)) in getRoyaume(joueur)):
									gagnant=joueurgagnant(joueur)
									partieTermine=True

					if champBatailleVide(getChampBataille(joueurAdverse(P,joueur))):
						#Conscription
						joueur=joueurCourant(changerJoueurCourant(P))
						#le joueurAdverse joue juste pour sa conscription, donc on change de joueur courant au début de la conscription, et on rechange à la fin
						if getNbCarteReserve(getReserve(joueur)) < 2:
							conscription=False
							while not(conscription) and not(partieTermine):
								if getNbCarteReserve(getReserve(joueur))==1:
									if getNbCarteRoyaume(getRoyaume(joueur))<1:
										gagnant=joueurAdverse(P,joueur) #du coup ici, le joueurAdverse est celui qui ne joue pas la conscription
										partieTermine = True
									else:
										position1=False
										while not(position1):
											choix1=input("Choisissez la zone dans laquelle déployer la première unité de votre réserve : ")
											z = getChampBatailleZone(getChampBataille(joueur),choix1)
											while not(appartientCdB(getChampBataille(joueur), z)):
												choix1=input("Choisissez la zone dans laquelle déployer la première unité de votre réserve : ")
												z = getChampBatailleZone(getChampBataille(joueur),choix1)
											if estDerriere(z):
												print("Pas possible, choisissez une autre zone.")
											else: 
												carte=getPremierReserve(getReserve(joueur))
												if zoneVide(z):
													addZoneCarte(z,carte)
													removeReserve(getReserve(joueur))
													position1=True		
												else:
													cart=getCarteZone(z)
													addReserve(getReserve(joueur),cart)
													addZoneCarte(z,carte)
													removeReserve(getReserve(joueur))
													position1=True
										position2=False
										while not(position2):
											choix2=input("Choisissez la zone dans laquelle déployer une unité de votre royaume : ")
											z = getChampBatailleZone(getChampBataille(joueur),choix2)
											while not(appartientCdB(getChampBataille(joueur),z)):
												choix2=input("Choisissez la zone dans laquelle déployer une unité de votre royaume : ")
												z = getChampBatailleZone(getChampBataille(joueur),choix2)
											if estDerriere(z):
												if zoneDevantVide(z):
													print("Pas possible, choisissez une autre zone.")
											else:
												afficheRoyaume(getRoyaume(joueur))
												carteType=input("Choisissez une carte de votre royaume: ")
												carte=getRoyaumeCarte(carteType)
												if zoneVide(z):
													addZoneCarte(z,carte)
													removeReserve(getReserve(joueur))
												else:
													cart=getCarteZone(choix2)
													addReserve(getReserve(joueur),cart)
													addZoneCarte(z,carte)
													removeReserve(getReserve(joueur))
													position2=True
										conscription=True
								if getNbCarteReserve(getReserve(joueur))==0:
									if getNbCarteRoyaume(getRoyaume(joueur))<2:
											gagnant=joueurAdverse(P,joueur)
											partieTermine = True #Fin de partie
									else:
										position1=False
										while not(position1):
											choix1=input("Choisissez la zone dans laquelle déployer la première unité de votre royaume : ")
											z = getChampBatailleZone(getChampBataille(joueur),choix1)
											while not(appartientCdB(getChampBataille(joueur),z)):
												choix1=input("Choisissez la zone dans laquelle déployer la première unité de votre royaume : ")
												z = getChampBatailleZone(getChampBataille(joueur),choix1)
											if estDerriere(z):
												print("Pas possible, choisissez une autre zone.")
											else: 
												afficheRoyaume(getRoyaume(joueur))
												carteType=input("Choisissez une carte de votre royaume: ")
												carte=getRoyaumeCarte(carteType)
												addZoneCarte(z,carte)
												removeRoyaumeCarte(getRoyaume(joueur),carte)
												position1=True
										position2=False
										while not(position2):
											choix2=input("Choisissez la zone dans laquelle déployer la deuxième unité de votre royaume : ")
											z = getChampBatailleZone(getChampBataille(joueur),choix2)
											while not(appartientCdB(getChampBataille(joueur),z)):
												choix2=input("Choisissez la zone dans laquelle déployer la deuxième unité de votre royaume : ")
												z = getChampBatailleZone(getChampBataille(joueur),choix2)
											if estDerriere(z):
												if zoneDevantVide(z):
													print("Pas possible, choisissez une autre zone.")
											else: 
												afficheRoyaume(getRoyaume(joueur))
												carteType=input("Choisissez une carte de votre royaume: ")
												carte=getRoyaumeCarte(carteType)
												if zoneVide(z):
													addZoneCarte(z,carte)
													removeRoyaumeCarte(getRoyaume(joueur),carte)
													position2=True
												else:
													print("Pas possible, choisissez une autre zone. ")
						else:
							position1=False
							while not(position1):
								choix1=input("Choisissez la première zone dans laquelle déployer la première unité de votre réserve : ")
								z = getChampBatailleZone(getChampBataille(joueur),choix1)
								while not(appartientCdB(getChampBataille(joueur),z)):
									choix1=input("Choisissez la zone dans laquelle déployer la première unité de votre réserve : ")
									z = getChampBatailleZone(getChampBataille(joueur),choix1)
								if estDerriere(z):
									print("Pas possible, choisissez une autre zone.")
								else:
									carte=getPremierReserve(getReserve(joueur))
									addZoneCarte(z,carte)                    #première carte à poser de la réserve, pas de condition car CdB vide
									removeReserve(getReserve(joueur))
									position1=True

							position2=False
							while not(position2):
								choix2=input("Choisissez la deuxième zone dans laquelle déployer la seconde unité de votre réserve : ")
								z = getChampBatailleZone(getChampBataille(joueur),choix2)
								while not(appartientCdB(getChampBataille(joueur),z)):
									choix2=input("Choisissez la zone dans laquelle déployer la seconde unité de votre réserve : ")
									z = getChampBatailleZone(getChampBataille(joueur),choix2)
								if estDerriere(z):
									if zoneDevantVide(z):
										print("Pas possible, choisissez une autre zone.")
								else: 
									carte=getPremierReserve(getReserve(joueur))
									if zoneVide(z):
										addZoneCarte(z,carte)
										removeReserve(getReserve(joueur))
										position2=True		
									else:
										print(" Pas possible de placer une carte sur une zone déjà occupée, choisissez une autre zone non occupée. ")

						joueur=joueurCourant(changerJoueurCourant(P)) #On change le joueur pour qu'il puisse reprendre son tour de jeu
			finAttaque(getChampBataille(joueurAdverse(P,joueur)))
			

			#Phase 3 ----------Developpement
		
		print(" Voulez-vous mettre une de vos unites de votre main dans votre royaume ?")
		print(" répondre par ‘True’ ou ‘False’ ")
		developpement=input()
		if developpement :
			affichageMain(getMain(joueur))
			carteType=input("Choisissez une carte dans votre main: ")
			carte = getMainCarte(getMain(joueur),carteType)
			while not(appartientMainCarte(getMain(joueur),carte)):
				carteType = input("Choisissez une carte dans votre main: ")
				carte = getMainCarte(getMain(joueur),carteType)
			addRoyaumeCarte(getRoyaume(joueur),carte)
			removeMain(getMain(joueur),carte)

		if getNbCartesMain(getMain(joueur))==6:
			affichageMain(getMain(joueur))
	        carteType=input("Choisissez une carte dans votre main: ")
	        carte = getMainCarte(getMain(joueur),carteType)
	        while not(appartientMainCarte(getMain(joueur),carte)):
	        	carteType = input("Choisissez une carte dans votre main: ")
	        	carte = getMainCarte(getMain(joueur),carteType)
	       	addRoyaumeCarte(getRoyaume(joueur),carte)
	        removeMain(getMain(joueur),carte)

print("Partie Terminée")
print("Le gagnant est "+ gagnant)