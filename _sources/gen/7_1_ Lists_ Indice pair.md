# 7.1. Lists: Indice pair

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), trouver et afficher tous les éléments ayant un indice pair (i.e. `A[0]`, `A[2]`, `A[4]`, ...).

## Exemple d'entrée

```
5 6 7 8 9
```

## Exemple de sortie

```
5 7 9
```

## Aide

https://rtavenar.github.io/poly_python/content/listes.html

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Read a list of integers:\n# a = [int(s) for s in input().split()]\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = [int(s) for s in input().split()]
for i in a[::2]:
  print(i, sep=' ')
```
````
