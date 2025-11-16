class Grille:
    def __init__(self, nombre_lignes, nombre_colonnes):
        self.nombre_colonnes = nombre_colonnes
        self.vide = "~"
        self.tir_marqué = "x"
        self.matrice = [self.vide] * (nombre_lignes * nombre_colonnes)
