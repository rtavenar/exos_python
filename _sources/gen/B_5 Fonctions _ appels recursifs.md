# B.5 Fonctions : appels récursifs

**Énoncé**

Codez une fonction `somme_entiers` qui calcule la somme des `n` premiers entiers (`n` étant un paramètre de cette fonction) de manière récursive (c'est-à-dire que le calcul de `somme_entiers(n)` devra utiliser un (au moins) autre appel à `somme_entiers` avec un argument différent de `n`).

**Exemple d'appel de la fonction**

```
somme_entiers(10)
```

**Exemple de valeur de retour**

```
55
```

**Aide**

https://rtavenar.github.io/poly_python/content/struct.html#fonctions

## Codez votre solution ci-dessous

<py-config>
    [splashscreen]
        enabled = false
</py-config>
<py-repl>
    def somme_entiers(n):
  # Codez votre fonction ici (et changez sa valeur de retour !)
  return -1
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
def somme_entiers(n):
  if n == 0:
    return 0
  return n + somme_entiers(n-1)
```
````
