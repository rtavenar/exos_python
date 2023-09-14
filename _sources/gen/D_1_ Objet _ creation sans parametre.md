# D.1. Objet : création sans paramètre

## Consignes

Écrire le code permettant de créer un objet de classe Cercle nommé "monCercle".

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    class Cercle:
  def __init__(self):
    self.rayon = 10		# attribut rayon du cercle
    self.x = 0			# attribut position en X du centre du cercle
    self.y = 0			# attribut position en Y du centre du cercle
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
  def __init__(self):
    self.rayon = 10		# attribut rayon du cercle
    self.x = 0			# attribut position en X du centre du cercle
    self.y = 0			# attribut position en Y du centre du cercle

# Écrire votre code ci-dessous
monCercle = Cercle()
```
````
