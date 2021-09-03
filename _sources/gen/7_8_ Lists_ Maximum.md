# 7.8. Lists: Maximum

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), trouver le premier élément maximum de la liste. Afficher sa valeur et son index (le premier élément porte l'index 0).

## Exemple d'entrée

```
1 2 3 2 1
```

## Exemple de sortie

```
3 2
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
print(max(a), a.index(max(a)))
```
````
