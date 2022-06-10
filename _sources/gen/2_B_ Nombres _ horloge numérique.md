# 2.B. Nombres : horloge numérique

## Consignes

Étant donné un entier _N_ représentant le nombre de minutes passées depuis minuit, combien d'heures et de minutes sont affichées sur une horloge numérique 24h ?

Le programme doit afficher deux nombres : le nombre d'heures (entre 0 et 23) et le nombre de minutes (entre 0 et 59).

Par exemple, si _N = 150_, alors 150 minutes se sont déroulées depuis minuit, et il est donc maintenant 2h30. Le programme doit dans ce cas afficher `2 30`.


## Exemple d'entrées

```
150
```

## Exemple de sortie

```
2 30
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '2.B.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
n = int(input())
print(n // 60, n % 60)
```
````
