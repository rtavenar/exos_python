# 2.3. Nombres : deux derniers chiffres

## Consignes

Étant donné un entier supérieur à 9, afficher ses deux derniers chiffres.

## Exemple d'entrée

```
1234
```

## Exemple de sortie

```
34
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
print(a % 100)
```
````
