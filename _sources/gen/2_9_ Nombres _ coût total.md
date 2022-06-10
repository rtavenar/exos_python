# 2.9. Nombres : coût total

## Consignes

Un gâteau coûte _A_ euros et _B_ centimes. Déterminer combien d'euros et de centimes on doit payer pour _N_ gâteaux. Le programme reçoit trois nombres entrés au clavier : _A_, _B_, _N_. Il doit afficher deux nombres : le coût total en euros et centimes.

## Exemple d'entrées

```
10
15
2
```

## Exemple de sortie

```
20 30
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '2.9.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
item_dollars = int(input())
item_cents = int(input())
n = int(input())
total_cents = (item_dollars * 100 + item_cents) * n
print(total_cents // 100, total_cents % 100)
```
````
