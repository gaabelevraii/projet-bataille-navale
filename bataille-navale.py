from random import randrange

from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin
from grille import Grille

grille = Grille(8, 10)
liste_bateaux = ["porteavion", "croiseur", "sousmarin", "torpilleur"]
liste_bateaux_placés = []
while len(liste_bateaux) != 0:
    i = randrange(0, len(liste_bateaux))
    match liste_bateaux[i]:
        case "porteavion":
            positions = grille.positions_possibles_bateau(4)
            x, y, vertical = positions[randrange(len(positions))]
            porteavion = PorteAvion(x, y, vertical=vertical)
            grille.ajoute(porteavion)
            liste_bateaux.remove("porteavion")
            liste_bateaux_placés.append(porteavion)
        case "croiseur":
            positions = grille.positions_possibles_bateau(3)
            x, y, vertical = positions[randrange(len(positions))]
            croiseur = Croiseur(x, y, vertical=vertical)
            grille.ajoute(croiseur)
            liste_bateaux.remove("croiseur")
            liste_bateaux_placés.append(croiseur)
        case "torpilleur":
            positions = grille.positions_possibles_bateau(2)
            x, y, vertical = positions[randrange(len(positions))]
            torpilleur = Torpilleur(x, y, vertical=vertical)
            grille.ajoute(torpilleur)
            liste_bateaux.remove("torpilleur")
            liste_bateaux_placés.append(torpilleur)
        case "sousmarin":
            positions = grille.positions_possibles_bateau(2)
            x, y, vertical = positions[randrange(len(positions))]
            sousmarin = SousMarin(x, y, vertical=vertical)
            grille.ajoute(sousmarin)
            liste_bateaux.remove("sousmarin")
            liste_bateaux_placés.append(sousmarin)
grille.matrice = [grille.vide] * (
    (len(grille.matrice) // grille.nombre_colonnes) * grille.nombre_colonnes
)

while len(liste_bateaux_placés) != 0:
    print(grille)
    coordonnées_valides = False
    while coordonnées_valides is False:
        coordonnées = input(
            "Entrez une coordonnée sous la forme (n° de ligne, n° de colonne): "
        )
        coordonnées = coordonnées.strip().replace("(", "").replace(")", "")
        x_str, y_str = coordonnées.split(",")
        x = int(x_str) - 1
        y = int(y_str) - 1
        if (
            x >= 0
            and x < len(grille.matrice) // grille.nombre_colonnes
            and y >= 0
            and y < grille.nombre_colonnes
        ):
            coordonnées_valides = True
    i = 0
    touché = False
    while touché is False and i < len(liste_bateaux_placés):
        if (x, y) in liste_bateaux_placés[i].positions:
            grille.tirer(x, y, "💣")
            touché = True
            if liste_bateaux_placés[i].coulé(grille) is True:
                grille.ajoute(liste_bateaux_placés[i])
                liste_bateaux_placés.pop(i)
        i += 1
    if touché is False:
        grille.tirer(x, y)
print(grille)
print("Vous avez gagné!")
