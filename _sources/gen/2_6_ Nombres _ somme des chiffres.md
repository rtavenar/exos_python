# 2.6. Nombres : somme des chiffres

## Consigne

Étant donné un entier à trois chiffres, calculer et afficher la somme de ses chiffres.

## Exemple d'entrée

```
123
```

## Exemple de sortie

```
6
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
print(a // 100 + a // 10 % 10 + a % 10)
```
````
