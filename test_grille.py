from random import randrange

from grille import Grille
from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


def test_init():
    grille = Grille(1, 2)
    assert isinstance(grille, Grille)


def test_nombre_colonnes():
    grille = Grille(3, 6)
    assert grille.nombre_colonnes == 6


def test_vide():
    grille = Grille(4, 7)
    assert grille.vide == "~"


def test_matrice():
    grille1 = Grille(2, 8)
    assert grille1.matrice == ["~"] * 16
    grille2 = Grille(8, 2)
    assert grille2.matrice == ["~"] * 16
    grille3 = Grille(4, 4)
    assert grille3.matrice == ["~"] * 16


def test_tirer():
    grille = Grille(5, 8)
    x = randrange(0, 5)
    y = randrange(0, 8)
    grille.tirer(x, y)
    assert grille.matrice[x * grille.nombre_colonnes + y] == "x"


def test___str__():
    grille = Grille(6, 5)
    assert grille.__str__() == "~~~~~\n~~~~~\n~~~~~\n~~~~~\n~~~~~\n~~~~~"


def test_ajoute_valide():
    grille1 = Grille(2, 4)
    grille1.ajoute(PorteAvion(1, 0, vertical=False))
    assert grille1.matrice == ["~", "~", "~", "~", "🚢", "🚢", "🚢", "🚢"]
    grille2 = Grille(2, 4)
    grille2.ajoute(Croiseur(1, 0, vertical=False))
    assert grille2.matrice == [
        "~",
        "~",
        "~",
        "~",
        "⛴",
        "⛴",
        "⛴",
        "~",
    ]
    grille3 = Grille(2, 4)
    grille3.ajoute(Torpilleur(1, 0, vertical=False))
    assert grille3.matrice == ["~", "~", "~", "~", "🚣", "🚣", "~", "~"]
    grille4 = Grille(2, 4)
    grille4.ajoute(SousMarin(1, 0, vertical=False))
    assert grille4.matrice == ["~", "~", "~", "~", "🐟", "🐟", "~", "~"]


def test_ajoute_invalide():
    grille = Grille(2, 3)
    grille.ajoute(Bateau(1, 0, longueur=2, vertical=True))
    assert grille.matrice == [
        "~",
        "~",
        "~",
        "~",
        "~",
        "~",
    ]
    grille.ajoute(Bateau(1, 0, longueur=4, vertical=True))
    assert grille.matrice == [
        "~",
        "~",
        "~",
        "~",
        "~",
        "~",
    ]
