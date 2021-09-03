# 7.2. Lists: Element pair

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), afficher tous les éléments pairs. Utiliser une boucle for qui va itérer sur la liste et pas sur les indices. Autrement dit, ne pas utiliser range( )

## Exemple d'entrée

```
1 2 2 3 3 3 4
```

## Exemple de sortie

```
2 2 4
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
for i in a:
  if i % 2 == 0:
    print(i, end=' ')
```
````
