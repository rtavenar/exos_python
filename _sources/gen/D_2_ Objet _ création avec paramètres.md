---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# D.2. Objet : création avec paramètres

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle", avec un rayon de 20, une position en X du centre de 5 et une position en Y du centre de 10.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

## Squelette

```{code-cell} ipython3

# class Cercle:
#   def __init__(self, r, posX, posY):
#     self.rayon = r		# attribut rayon du cercle
#     self.x = posX			# attribut position en X du centre du cercle
#     self.y = posY			# attribut position en Y du centre du cercle
# 
# # Écrire votre code ci-dessous
# 
```

````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
class Cercle:
  def __init__(self, r, posX, posY):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle

# Écrire votre code ci-dessous
monCercle = Cercle(20, 5, 10)
```
````
