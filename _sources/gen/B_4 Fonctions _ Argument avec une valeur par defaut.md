# B.4 Fonctions : Argument avec une valeur par défaut

**Énoncé**

Codez une fonction somme qui permet d'ajouter au maximum 4 entiers. La fonction prend au minimum 1 entier en paramètre et 4 au maximum.

**Exemple d'appel de la fonction**

```
somme(1,2,3)
```

**Exemple de valeur de retour**

```
6
```

**Aide**

https://rtavenar.github.io/poly_python/content/struct.html#fonctions

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    def somme():
  # Codez votre fonction ici
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
def somme(entier1, entier2=0, entier3=0, entier4=0):
  # Codez votre fonction ici
  return entier1+entier2+entier3+entier4
```
````
