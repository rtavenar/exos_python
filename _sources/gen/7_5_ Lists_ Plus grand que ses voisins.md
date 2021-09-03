# 7.5. Lists: Plus grand que ses voisins

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), déterminer et afficher le nombre d'éléments plus grands que leurs deux voisins.

Le premier et le dernier éléments de  la liste ne doivent pas être considérés car ils n'ont qu'un seul voisin.

## Exemple d'entrée

```
1 5 1 5 1
```

## Exemple de sortie

```
2
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
for i in range(1, len(a) - 1):
  if a[i - 1] < a[i] > a[i + 1]:
    counter += 1
print(counter)
```
````
