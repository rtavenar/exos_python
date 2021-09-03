# 3.2. If/else: Minimum de deux nombres

## Consigne

Étant donnés 2 entiers, affichez le plus petit des deux

## Exemple d'entrée

```
3
7
```

## Exemple de sortie

```
3
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher une valeur :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
b = int(input())
if a < b:
  print(a)
else:
  print(b)
```
````
