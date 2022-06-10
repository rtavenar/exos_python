# 2.7. Nombres : parcours d'une voiture

## Consignes

Une voiture peut parcourir une distance de _N_ kilomètres par jour. Combien de jours faudra-t-il pour parcourir une distance de _M_ kilomètres avec cette voiture ? Le programme reçoit deux nombres tapés au clavier : _N_ et _M_.

## Exemple d'entrée

```
700
750
```

## Exemple de sortie

```
2
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '2.7.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
from math import ceil

n = int(input())
m = int(input())
print(ceil(m / n))
```
````
