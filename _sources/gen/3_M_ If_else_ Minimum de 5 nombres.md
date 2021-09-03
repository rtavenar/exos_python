# 3.M. If/else: Minimum de 5 nombres

## **Énoncé**

Étant donnés 5 nombres, afficher leur minimum.

## Exemple d'entrée

```
10
20
30
40
50
```

## Exemple de sortie

```
10
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher une valeur :\n# print(a)'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
least = int(input())

new_integer = int(input())
if new_integer < least:
  least = new_integer

new_integer = int(input())
if new_integer < least:
  least = new_integer
  
new_integer = int(input())
if new_integer < least:
  least = new_integer
  
new_integer = int(input())
if new_integer < least:
  least = new_integer
  
print(least)
```
````
