class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical

    @property
    def positions(self):
        if self.vertical is False:
            return [(self.ligne, self.colonne + i) for i in range(self.longueur)]
        else:
            return [(self.ligne + i, self.colonne) for i in range(self.longueur)]

    def coulé(self, grille):
        for position in self.positions:
            if (
                grille.matrice[position[0] * grille.nombre_colonnes + position[1]]
                != "x"
            ):
                return False
        return True
