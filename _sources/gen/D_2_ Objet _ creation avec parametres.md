# D.2. Objet : création avec paramètres

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle", avec un rayon de 20, une position en X du centre de 5 et une position en Y du centre de 10.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    class Cercle:
  def __init__(self, r, posX, posY):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle
# Écrire votre code ci-dessous
</py-repl>
<py-terminal id="my-terminal"></py-terminal>
<py-script>
from js import document as _DOC
def clear_term():
    ter = _DOC.getElementById("my-terminal").firstChild
    ter.innerHTML = ''
</py-script>
<button py-click="clear_term()" id="clear-terminal" class="py-button">Nettoyer la console de sortie</button>


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
