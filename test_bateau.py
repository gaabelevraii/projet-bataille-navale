from bateau import Bateau, PorteAvion, Croiseur, Torpilleur
from grille import Grille


def test_init():
    bateau = Bateau(2, 3, 4, True)
    assert isinstance(bateau, Bateau)


def test_ligne():
    bateau = Bateau(2, 3, 4, True)
    assert bateau.ligne == 2


def test_colonne():
    bateau = Bateau(2, 3, 4, True)
    assert bateau.colonne == 3


def test_longueur():
    bateau1 = Bateau(2, 3, 4, True)
    assert bateau1.longueur == 4
    bateau2 = Bateau(2, 3)
    assert bateau2.longueur == 1
    bateau3 = Bateau(2, 3, vertical=True)
    assert bateau3.longueur == 1


def test_positions_vertical():
    bateau = Bateau(2, 3, longueur=3, vertical=True)
    assert bateau.positions == [(2, 3), (3, 3), (4, 3)]


def test_positions_horizontal():
    bateau = Bateau(2, 3, longueur=3)
    assert bateau.positions == [(2, 3), (2, 4), (2, 5)]


def test_coulé():
    grille = Grille(2, 3)
    bateau = Bateau(1, 0, 2, False)
    grille.tirer(1, 0)
    grille.tirer(1, 1)
    assert bateau.coulé(grille) is True


def test_init_porteavions():
    pa = PorteAvion(2, 3)
    assert isinstance(pa, PorteAvion)
    assert isinstance(pa, Bateau)


def test_longueur_porteavions():
    pa = PorteAvion(2, 3)
    assert pa.longueur == 4


def test_vertical_porteavions():
    pa1 = PorteAvion(2, 3, False)
    assert pa1.vertical is False
    pa2 = PorteAvion(2, 3)
    assert pa2.vertical is False
    pa3 = PorteAvion(2, 3, True)
    assert pa3.vertical is True


def test_init_croiseur():
    c = Croiseur(2, 3)
    assert isinstance(c, Croiseur)
    assert isinstance(c, Bateau)


def test_longueur_croiseur():
    c = Croiseur(2, 3)
    assert c.longueur == 3


def test_vertical_croiseur():
    c1 = Croiseur(2, 3, False)
    assert c1.vertical is False
    c2 = Croiseur(2, 3)
    assert c2.vertical is False
    c3 = Croiseur(2, 3, True)
    assert c3.vertical is True


def test_init_torpilleur():
    t = Torpilleur()
    assert isinstance(t, Torpilleur)
