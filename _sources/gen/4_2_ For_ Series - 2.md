# 4.2. For: Series - 2

## Consigne

Soit deux entiers A et B donnés en entrée. Afficher tous les nombres de A à B bornes comprises, par ordre croissant, si A < B ou par ordre décroissant si A ≥ B.

## Exemple d'entrée

```
8
5
```

## Exemple de sortie

```
8 7 6 5
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '4.2.', 'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
b = int(input())

if a < b:
  for i in range(a, b + 1):
    print(i, end=' ')
else:
  for i in range(a, b - 1, -1):
    print(i, end=' ')
```
````
