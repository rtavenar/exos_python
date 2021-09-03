# 3.H. If/else: Échecs : mouvements de reine

## **Énoncé**

Aux échecs, une reine peut se déplacer horizontalement, verticalement et en diagonale d'un nombre quelconque de cases.

Votre programme recevra une position de départ (une valeur pour la colonne, une pour la ligne) et une position d'arrivée (une valeur pour la colonne, une pour la ligne) et devra afficher OUI si une reine peut se déplacer de la position de départ à celle d'arrivée et NON sinon.






## Exemple d'entrée

```
1
1
2
2
```

## Exemple de sortie

```
OUI
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher une valeur :\n# print(a)'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
  print('OUI')
else:
  print('NON')
```
````
