# 7.3. Lists: Plus grand que le voisin de gauche

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), trouver et afficher tous les éléments qui sont plus grand que leur voisin de gauche.

## Exemple d'entrée

```
1 5 2 4 3
```

## Exemple de sortie

```
5 4
```

## Aide

https://rtavenar.github.io/poly_python/content/listes.html

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '7.3.', 'title': 'Testez votre solution ici', 'src': '# Read a list of integers:\n# a = [int(s) for s in input().split()]\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = [int(s) for s in input().split()]
for i in range(1, len(a)):
  if a[i - 1] < a[i]:
    print(a[i], end=' ')
```
````
