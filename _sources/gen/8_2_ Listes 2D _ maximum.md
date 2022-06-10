# 8.2. Listes 2D : maximum

## Consignes

Étant donnés deux entiers entrés au clavier - le nombre de lignes `m` et de colonnes `n` d'une liste 2D `m×n` - suivis de la saisie de `m` lignes de `n` entiers, trouver l'élément maximum de cette liste 2D et afficher ses indices de ligne et de colonne. S'il y a plusieurs éléments maximum identiques sur des lignes différentes, afficher les indices pour celui se trouvant sur la ligne de plus petit indice. S'il y a plusieurs éléments maximum identiques sur une même ligne, afficher les indices pour celui se trouvant sur la colonne de plus petit indice.

## Exemple d'entrée

```
3 4
0 3 2 4
2 3 **5** 5
5 1 2 3
```

(l'élément maximum répondant aux règles énoncées est surligné)

## Exemple de sortie

```
1 2
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#lists

https://docs.python.org/fr/3.6/tutorial/datastructures.html#list-comprehensions

https://docs.python.org/fr/3.6/tutorial/datastructures.html#nested-list-comprehensions

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '8.2.', 'title': 'Testez votre solution ici', 'src': "# Lire une liste 2D d'entiers :\n# a = [[int(j) for j in input().split()] for i in range(NUM_ROWS)]\n# Afficher la valeur de a :\n# print(a)\n"})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
m, n = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(m)]
max_value, max_i, max_j = a[0][0], 0, 0
for i in range(m):
  for j in range(n):
    if a[i][j] > max_value:
      max_value, max_i, max_j = a[i][j], i, j
print(max_i, max_j)
```
````