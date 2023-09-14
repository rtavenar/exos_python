# D.7. Objet : définition d'une classe et de son initialisateur

## Consignes

Écrire le code permettant de définir une classe Personne et son initialisateur. Les objets de classe Personne possèderont un attribut "`nom`" dont la valeur sera passée en paramètre à la construction de l'objet.

## Aide

https://docs.python.org/fr/3.6/tutorial/classes.html#a-first-look-at-classes

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
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
# Écrire votre code ci-dessous
class Personne:
  def __init__(self, nom):
    self.nom = nom
```
````
