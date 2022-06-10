# 3.J. If/else: Année bissextile

## **Énoncé**

Étant donné une année, votre programme devra afficher `BISSEXTILE` s'il s'agit d'une année bissextile et  `NORMALE` sinon.

https://fr.wikipedia.org/wiki/Année_bissextile

**Attention.** Les mots `BISSEXTILE` et `NORMALE` devront être écrits en majuscules.

## Exemple d'entrée

```
2012
```

## Exemple de sortie

```
BISSEXTILE
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '3.J.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher une valeur :\n# print(a)'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
  print('BISSEXTILE')
else:
  print('NORMALE')
```
````
