# 7.9. Lists: Inversion du min et du max

## Consigne

À partir d'une liste de nombres entiers distincts donnés en entrée (chaque nombre est séparé par un espace), inverser le minimum et le maximum et afficher la liste résultat.

## Exemple d'entrée

```
3 4 5 2 1
```

## Exemple de sortie

```
3 4 1 2 5
```

## Aide

https://rtavenar.github.io/poly_python/content/listes.html

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '7.9.', 'title': 'Testez votre solution ici', 'src': '# Read a list of integers:\n# a = [int(s) for s in input().split()]\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = [int(s) for s in input().split()]
pos_min = a.index(min(a))
pos_max = a.index(max(a))
a[pos_min], a[pos_max] = a[pos_max], a[pos_min]
print(*a)
```
````
