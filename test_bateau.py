from bateau import Bateau


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
