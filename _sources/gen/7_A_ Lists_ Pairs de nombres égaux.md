# 7.A. Lists: Pairs de nombres égaux

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), compter le nombre de pairs de nombres égaux. Chaque pair de deux nombres égaux devra être compté exactement une fois.

## Exemple d'entrée #1

```
1 2 3 2 3
```

## Exemple de sortie #1

```
2
```

## Exemple d'entrée #2

```
1 1 1 1 1
```

## Exemple de sortie #2

```
10
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
counter = 0
for i in range(len(a)):
  for j in range(i + 1, len(a)):
    if a[i] == a[j]:
      counter += 1
print(counter)
```
````
