# 2.A. Nombres : jour de la semaine

## Consignes

Les jours de la semaine sont numérotés de la manière suivantes : 0 —Dimanche, 1 — Lundi, 2 — Mardi, ..., 6 — Samedi. Le programme reçoit un entier _K_ compris entre 1 et 365. Trouver et afficher le numéro du jour de la semaine du _K_-ième jour de l'année sachant que le 1er janvier de cette année est un jeudi.


## Exemple d'entrée

```
1
```

## Exemple de sortie

```
4
```

## Aide

https://docs.python.org/fr/3/reference/expressions.html#binary-arithmetic-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '2.A.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print((int(input()) + 3) % 7)
```
````
