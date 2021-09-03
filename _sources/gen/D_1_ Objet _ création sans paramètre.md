# D.1. Objet : création sans paramètre

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle".

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': 'class Cercle:\n  def __init__(self):\n    self.rayon = 10\t\t# attribut rayon du cercle\n    self.x = 0\t\t\t# attribut position en X du centre du cercle\n    self.y = 0\t\t\t# attribut position en Y du centre du cercle\n\n# Écrire votre code ci-dessous\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

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
