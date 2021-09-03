# 1.7. Input/print: Deux horodatages

## Consigne

Soit deux horodatages dans la même journée : un nombre d'heures, de minutes et de secondes entrés l'un après l'autre pour chaque horodatage. L'instant du premier apparaît avant le second.
Calculer puis afficher le nombre de secondes entre les deux horodatages.

## Exemple d'entrée #1

```
1
1
1
2
2
2
```

## Exemple de sortie #1

```
3661
```

## Exemple d'entrée #2

```
1
2
30
1
3
20
```

## Exemple de sortie #2

```
50
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

https://docs.python.org/fr/3/tutorial/inputoutput.html

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
hours_1 = int(input())
minutes_1 = int(input())
seconds_1 = int(input())

hours_2 = int(input())
minutes_2 = int(input())
seconds_2 = int(input())

print((hours_2 - hours_1) * 3600 +
      (minutes_2 - minutes_1) * 60 +
      seconds_2 - seconds_1)
```
````
