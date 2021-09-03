# 7.C. Lists: Huit reines

## Consigne

Il est possible de placer 8 reines sur un échiquier de 8x8 cases de telle sorte qu'aucune reine n'en menace une autre. Il faut pour cela qu'aucune reine ne partage la même ligne colonne ou diagonale avec une autre reine.


Sois une disposition de 8 reines sur un échiquier. Si une paire de reines ne respecte pas la règle ci-dessus, afficher "YES", sinon afficher "NO". L'entrée correspond aux coordonnées sur l'échiquier des huit reines. Chaque coordonnée correspondra à une ligne d'entrée. Les coordonnées des reines seront représentées par le numéro de la colonne puis le numéro de la ligne d'un échiquer standard.






## Exemple d'entrée

```
1 5
2 3
3 1
4 7
5 2
6 8
7 6
8 4
```

(exemple de la figure ci-dessus)

## Exemple de sortie

```
NO
```

## Aide

https://rtavenar.github.io/poly_python/content/listes.html

https://docs.python.org/fr/3/tutorial/datastructures.html#more-on-lists

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Read a list of integers:\n# a = [int(s) for s in input().split()]\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x = []
y = []
for i in range(8):
  a = [int(s) for s in input().split()]
  x.append(a[0])
  y.append(a[1])
answer = 'NO'
for i in range(8):
  for j in range(i + 1, 8):
    if ((x[i] == x[j]) or
        (y[i] == y[j]) or
        (abs(x[i] - x[j]) == abs(y[i] - y[j]))):
      answer = 'YES'
print(answer)
```
````
