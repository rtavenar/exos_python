# D.3. Objet : création avec paramètres facultatifs

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle", avec une position en X du centre de 5 et une position en Y du centre de -5. Vous devez utiliser uniquement ces deux valeurs pour la construction de l'objet et ne rien renseigner pour le rayon afin de laisser la valeur par défaut.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

## Squelette

```python
class Cercle:
  def __init__(self, r=15, posX=0, posY=0):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle

# Écrire votre code ci-dessous
```

## Proposition de solution

```python
class Cercle:
  def __init__(self, r=15, posX=0, posY=0):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle

# Écrire votre code ci-dessous
monCercle = Cercle(posX=5, posY=-5)
```

