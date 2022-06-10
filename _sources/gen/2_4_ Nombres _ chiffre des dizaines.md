# 2.4. Nombres : chiffre des dizaines

## Consignes

Étant donné un entier, afficher son chiffre des dizaines.

## Exemple d'entrée

```
1234
```

## Exemple de sortie

```
3
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '2.4.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(int(input()) % 100 // 10)
```
````
