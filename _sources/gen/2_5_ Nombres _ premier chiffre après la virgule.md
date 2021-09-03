# 2.5. Nombres : premier chiffre après la virgule

## Consignes

Etant donné un nombre réel positif, afficher son premier chiffre après la virgule (point décimal).

## Exemple d'entrée

```
1.79
```

## Exemple de sortie

```
7
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = float(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(int(float(input()) * 10) % 10)
```
````
