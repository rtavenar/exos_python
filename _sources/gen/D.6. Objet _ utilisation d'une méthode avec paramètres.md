# D.6. Objet : utilisation d'une méthode avec paramètres

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle" avec une position du centre en X de 5, une position du centre en Y de 10 et la valeur par défaut pour le rayon.

Écrire ensuite le code permettant de déplacer le centre de l'objet "monCercle" de 5 en X et de -8 en Y. Pour faire se déplacement vous devez uniquement utiliser une méthode de l'objet "monCercle", avec des paramètres 5 et -8.

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
  
  def deplacerCentre(self, depX, depY):
    self.x += depX
    self.y += depY
  
# Écrire votre code ci-dessous
```

````{dropdown} Proposition de solution

```python
from math import pi

class Cercle:
  def __init__(self, r=15, posX=0, posY=0):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle
  
  def deplacerCentre(self, depX, depY):
    self.x += depX
    self.y += depY
  
# Écrire votre code ci-dessous
monCercle = Cercle(posX=5, posY=10)
monCercle.deplacerCentre(5, -8)
```
````
