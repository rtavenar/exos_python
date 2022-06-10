# 3.1. If/else: Pair ou impair

## Consigne

Étant donné un entier, afficher "pair" s'il est pair ou "impair" sinon.

## Exemple d'entrée #1

```
5
```

## Exemple de sortie #1

```
impair
```

## Exemple d'entrée #2

```
6
```

## Exemple de sortie #2

```
pair
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '3.1.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier\n# a = int(input())\n# Afficher une valeur:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
if int(input()) % 2 == 0:
  print('pair')
else:
  print('impair')
```
````
