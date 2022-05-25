# -*- coding: utf-8 -*-
import numpy as np #numpy privilégie l'utilisation de matrices
"""
Created on Mon May 16 09:20:00 2022

@author: Adrian
"""
# on déclare le tableau et on l'initialise à zéro
matrice = np.zeros((8, 9))

cycle_rangée = True
cycle_sièges = True
sortie = "s"
rangées = [0,0,0,0,0,0,0,0]

while (sortie != "N"):
    # nous sélectionnons la rangée
    while cycle_rangée:
        try:
            rangée = int(input(" A quelle rangee voulez vous aller: "))
            if (rangée < 9 and rangée > 0):
                cycle_rangée = False
        except ValueError or (rangée < 1 or rangée > 8):
            print(" Vous devez écrire un nombre entre 1 et 8. ")
            
    # nous sélectionnons le nombre de places
    while cycle_sièges:
        try:
            sièges = int(input(" Combien de places voulez vous acheter: "))
            if (sièges <10 and sièges > 0):
                cycle_sièges = False
        except ValueError or (sièges < 1 or sièges > 9):
            print(" Vous devez écrire un nombre entre 1 et 9. ")
            continue
            
    # nous vérifions s'il y a ce nombre de sièges dans cette rangée
    disponible = 9 - np.count_nonzero(matrice[rangée-1,:])

    if (disponible >= sièges):
        initial = rangées[rangée -1]
        matrice[rangée -1, range(initial, initial + sièges)] = 1
        rangées[rangée-1] = rangées[rangée -1] + sièges
        print(matrice)
        print (" Bravo, votre achat a bien été éffectué ")
    else:
        print(" Il n'y a pas assez d'espaces dans cette rangée ")
        
    cycle_rangée = True;
    cycle_sièges = True;
    sortie = str(input(" Tapez N si vous ne voulez pas continuer "))

