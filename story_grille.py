# from grille import Grille

# # 1. Créer grille de 5 lignes et 8 colonnes
# grille = Grille(5, 8)

# while True:
#     # 2. Afficher la grille
#     grille.afficher()
#     # 3. Demander à l'utilisateur les coordonnées x et y du tir
#     coordonnées = input("Entrez une coordonnée sous la forme (x,y): ")
#     coordonnées = coordonnées.strip.replace("(", "").replace(")", "")
#     x_str, y_str = coordonnées.split(",")
#     x = int(x_str)
#     y = int(y_str)
#     # 4. Tirer à l'endroit indiqué sur la grille
#     grille.tirer(x, y)
#     # 5. Retour en 2. par while(True)
