# Saisie des données
alpha = int(input())
# En une heure, l'aiguille des heures se déplace de 30°.
# Un déplacement de cette aiguille de 1° représente 2 minutes

# Calcul des minutes correspondant à la position de l'aiguille
nbminutes = (alpha % 30) * 2

# L'aiguille des minutes se déplace de 6° en une minutes

# Calcul de l'angle de l'aiguille des minutes

anglemin = nbminutes*6

print("{0:d}".format(anglemin))

