from bateau import Bateau

# Cas 1 : deux bateaux se chevauchent

# 1. Créer un bateau b1
b1 = Bateau(2, 3, 4)
# 2. Créer un bateau b2 qui chevauche b1
b2 = Bateau(2, 3, 3, True)
# 3. Vérifier qu'ils se chevauchent
chevauchement = False
for pos in b1.positions:
    if pos in b2.positions:
        chevauchement = True
print(chevauchement)

# Cas 2 : deux bateaux ne se chevauchent pas

# 1. Créer un bateau b1
b1 = Bateau(2, 3, 4)
# 2. Créer un bateau b2 qui chevauche b1
b2 = Bateau(3, 3, 3, True)
# 3. Vérifier qu'ils se chevauchent
chevauchement = False
for pos in b1.positions:
    if pos in b2.positions:
        chevauchement = True
print(chevauchement)
