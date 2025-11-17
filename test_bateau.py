from bateau import Bateau


def test_init():
    bateau = Bateau()
    assert isinstance(bateau, Bateau)
