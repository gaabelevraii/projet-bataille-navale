from bateau import Bateau, PorteAvion, Croiseur, Torpilleur, SousMarin


class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_colonnes = nombre_colonnes
        self.vide = "~"
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)

    def tirer(self, x, y, touche="x"):
        self.matrice[x * self.nombre_colonnes + y] = touche

    def __str__(self):
        grille_string = ""
        nombre_lignes = len(self.matrice) // self.nombre_colonnes
        for i in range(nombre_lignes):
            for j in range(0, self.nombre_colonnes):
                grille_string += self.matrice[i * self.nombre_colonnes + j]
            if i < nombre_lignes - 1:
                grille_string += "\n"
        return grille_string

    def ajoute(self, bateau):
        if isinstance(bateau, PorteAvion) is True:
            for position in bateau.positions:
                self.matrice[position[0] * self.nombre_colonnes + position[1]] = "🚢"
        elif isinstance(bateau, Croiseur) is True:
            for position in bateau.positions:
                self.matrice[position[0] * self.nombre_colonnes + position[1]] = "⛴"
        elif isinstance(bateau, Torpilleur) is True:
            for position in bateau.positions:
                self.matrice[position[0] * self.nombre_colonnes + position[1]] = "🚣"
        elif isinstance(bateau, SousMarin) is True:
            for position in bateau.positions:
                self.matrice[position[0] * self.nombre_colonnes + position[1]] = "🐟"

    def chevauchement(self, bateau):
        if (
            bateau.vertical is False
            and bateau.colonne + bateau.longueur - self.nombre_colonnes > 0
        ) or (
            bateau.vertical is True
            and bateau.ligne
            + bateau.longueur
            - len(self.matrice) // self.nombre_colonnes
            > 0
        ):
            return False
        for position in bateau.positions:
            if self.matrice[position[0] * self.nombre_colonnes + position[1]] != "~":
                return False
        return True

    def positions_possibles_bateau(self, longueur_bateau):
        positions_possibles = []
        for i in range(len(self.matrice) // self.nombre_colonnes):
            for j in range(self.nombre_colonnes):
                if (
                    self.chevauchement(
                        Bateau(i, j, longueur=longueur_bateau, vertical=False)
                    )
                    is True
                ):
                    positions_possibles.append((i, j))
                if (
                    self.chevauchement(
                        Bateau(i, j, longueur=longueur_bateau, vertical=True)
                    )
                    is True
                ):
                    positions_possibles.append((i, j))
        return positions_possibles
