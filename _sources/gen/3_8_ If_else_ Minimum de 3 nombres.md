# 3.8. If/else: Minimum de 3 nombres

## **Énoncé**

Étant donnés trois entiers, affichez le plus petit des 3.

## Exemple d'entrée

```
5
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
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher une valeur :\n# print(a)'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
b = int(input())
c = int(input())

if a < b and a < c:
  print(a)
elif b < a and b < c:
  print(b)
else:
  print(c)
```
````
