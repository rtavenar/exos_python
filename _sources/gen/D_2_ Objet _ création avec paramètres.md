# D.2. Objet : création avec paramètres

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle", avec un rayon de 20, une position en X du centre de 5 et une position en Y du centre de 10.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': 'class Cercle:\n  def __init__(self, r, posX, posY):\n    self.rayon = r\t\t# attribut rayon du cercle\n    self.x = posX\t\t\t# attribut position en X du centre du cercle\n    self.y = posY\t\t\t# attribut position en Y du centre du cercle\n\n# Écrire votre code ci-dessous\n'})</script>


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
