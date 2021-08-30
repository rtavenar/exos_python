# D.5. Objet : utilisation d'une méthode sans paramètre

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle", avec un rayon de 20 et les valeurs par défaut pour les positions en X et Y du centre. Créer une variable "surface" contenant le résultat du calcul de la surface de l'objet "monCercle". Pour obtenir ce résultat vous devez utiliser uniquement l'objet monCercle créé sans écrire vous-même le calcul de la surface.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

## Squelette

```python
from math import pi

class Cercle:
  def __init__(self, r=15, posX=0, posY=0):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle
  
  def calculerSurface(self):
    return pi*self.rayon**2
  
# Écrire votre code ci-dessous

```

````{dropdown} Proposition de solution

```python
from math import pi

class Cercle:
  def __init__(self, r=15, posX=10, posY=10):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle
  
  def calculerSurface(self):
    return pi*self.rayon**2
    
# Écrire votre code ci-dessous
monCercle = Cercle(20)
surface = monCercle.calculerSurface()
```
````
