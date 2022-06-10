# 2.2. Nombres : échanger les chiffresdigits

## Consignes

Étant donné un entier à deux chiffres, échanger ses chiffres et afficher le résultat.

## Exemple d'entrée

```
79
```

## Exemple de sortie

```
97
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '2.2.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
print(a % 10 * 10 + a // 10)
```
````
