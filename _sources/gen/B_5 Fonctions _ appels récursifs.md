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

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': 'def somme_entiers(n):\n  # Codez votre fonction ici (et changez sa valeur de retour !)\n  return -1'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
def somme_entiers(n):
  if n == 0:
    return 0
  return n + somme_entiers(n-1)
```
````
