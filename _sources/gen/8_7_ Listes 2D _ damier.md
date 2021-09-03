# 8.7. Listes 2D : damier

## Consignes

Étant donnés deux entiers positifs `n` et `m` entrés au clavier, créer une liste 2D de taille `n×m` et la remplir avec les caractères "`.`" et "`*`" alternés en ligne et en colonne afin d'obtenir un motif en damier. Le coin haut gauche du damier doit contenir le caractère "`.`" .

## Exemple d'entrée

```
6 8
```

## Exemple de sortie

```
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
. * . * . * . *
* . * . * . * .
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#lists

https://docs.python.org/fr/3.6/tutorial/datastructures.html#list-comprehensions

https://docs.python.org/fr/3.6/tutorial/datastructures.html#nested-list-comprehensions

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': "# Lire une liste d'entiers :\n# a = [int(s) for s in input().split()]\n# Afficher la valeure de a :\n# print(a)\n"})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
n, m = [int(s) for s in input().split()]
a = [['.' if (i + j) % 2 == 0 else '*']
     for i in range(n)
     for j in range(m)]
for line in a:
  print(*line)
```
````
