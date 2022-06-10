# 4.5. For: Somme des cubes

## Consigne

Pour un entier N donné en entrée, calculer la somme suivante :

1³ + 2³ + ... + N³

## Exemple d'entrée

```
3
```

## Exemple de sortie

```
36
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '4.5.', 'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
result = 0
for i in range(1, int(input()) + 1):
  result += i ** 3
print(result)
```
````
