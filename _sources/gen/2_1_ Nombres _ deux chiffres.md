# 2.1. Nombres : deux chiffres

## Consignes

Étant donné un entier à deux chiffres, afficher son premier chiffre (dizaines) puis son deuxième chiffre (unités). Utiliser l'opérateur de division entière pour obtenir le chiffre des dizaines et l'opérateur de modulo (reste de la division entière) pour obtenir le chiffre des unités.

## Exemple d'entrée

```
79
```

## Exemple de sortie

```
7 9
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '2.1.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
print(a // 10, a % 10)
```
````