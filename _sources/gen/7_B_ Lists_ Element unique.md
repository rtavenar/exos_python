# 7.B. Lists: Element unique

## Consigne

À partir d'une liste de nombres entiers donnés en entrée (chaque nombre est séparé par un espace), trouver et afficher les éléments qui n'apparaissent qu'une seule fois. De tels éléments devront être affiché dans l'ordre dans lequel ils apparaissent dans la liste originale. Vous pouvez utiliser la méthode count() (Cf. deuxième lien de l'aide ci-dessous).

## Exemple d'entrée

```
4 3 5 2 5 1 3 5
```

## Exemple de sortie

```
4 2 1
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
  if a.count(i) == 1:
    print(i, end=' ')
```
````
