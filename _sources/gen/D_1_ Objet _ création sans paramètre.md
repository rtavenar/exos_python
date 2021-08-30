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

# D.1. Objet : création sans paramètre

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle".

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

## Squelette

```{code-cell} python
class Cercle:
  def __init__(self):
    self.rayon = 10		# attribut rayon du cercle
    self.x = 0			# attribut position en X du centre du cercle
    self.y = 0			# attribut position en Y du centre du cercle

# Écrire votre code ci-dessous
```

````{dropdown} Proposition de solution

```python
class Cercle:
  def __init__(self):
    self.rayon = 10		# attribut rayon du cercle
    self.x = 0			# attribut position en X du centre du cercle
    self.y = 0			# attribut position en Y du centre du cercle

# Écrire votre code ci-dessous
monCercle = Cercle()
```
````
