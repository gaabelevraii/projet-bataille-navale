from grille import Grille


def test_init():
    grille = Grille()
    assert isinstance(grille, Grille)
