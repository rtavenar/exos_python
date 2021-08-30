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

http://rtavenar.github.io/teaching/python_poly/html/poly.html#fonctions

## Squelette

```{code-cell} python
def somme_entiers(n):
  # Codez votre fonction ici (et changez sa valeur de retour !)
  return -1
```

````{dropdown} Proposition de solution

```python
def somme_entiers(n):
  if n == 0:
    return 0
  return n + somme_entiers(n-1)
```
````
