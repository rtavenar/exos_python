# D.4. Objet : utilisation d'un attribut

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle", avec un rayon de 10 et les valeurs par défaut pour les positions en X et Y du centre. Créer une variable "perimetre" contenant le résultat du calcul du périmètre de l'objet "monCercle". Pour ce calcul vous devez uniquement utiliser la constante `pi` importée au début du programme et l'objet monCercle créé.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

## Squelette

```{code-cell} python
from math import pi

class Cercle:
  def __init__(self, r=15, posX=0, posY=0):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle

# Écrire votre code ci-dessous
# Le périmètre d'un cercle de rayon R est égal à 2*pi*R

```

````{dropdown} Proposition de solution

```python
from math import pi

class Cercle:
  def __init__(self, r=15, posX=0, posY=0):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle
  
  
# Écrire votre code ci-dessous
# Le périmètre d'un cercle de rayon R est égal à 2*pi*R

monCercle = Cercle(10)
perimetre = 2*pi*monCercle.rayon
```
````
