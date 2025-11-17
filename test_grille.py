from grille import Grille
from random import randrange


def test_init():
    grille = Grille(1, 2)
    assert isinstance(grille, Grille)


def test_nombre_colonnes():
    grille = Grille(3, 6)
    assert grille.nombre_colonnes == 6


def test_vide():
    grille = Grille(4, 7)
    assert grille.vide == "~"


def test_tir_marqué():
    grille = Grille(5, 8)
    assert grille.tir_marqué == "x"


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
