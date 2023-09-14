# B.2 Fonctions : passage d'un paramètre

**Énoncé**

Codez une fonction affichage_bienvenue qui affiche le message "Bienvenue XXX" et ajoute le prénom d'une personne ('XXX'). La fonction prend en paramètre le prénom de la personne.

**Exemple d'appel de la fonction**

```
affichage_bienvenue('Régis')
```

**Exemple de sortie**

```
Bienvenue Régis
```

**Aide**

https://rtavenar.github.io/poly_python/content/struct.html#fonctions

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    def affichage_bienvenue():
  # Codez votre fonction ici (et affichez le message de bienvenue !)
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
def affichage_bienvenue(prenom):
  # Codez votre fonction ici (et affichez le message de bienvenue !)
  print('Bienvenue '+ prenom)
```
````
