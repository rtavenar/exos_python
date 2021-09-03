# 6.2. While: Plus petit diviseur

## **Énoncé**

Étant donné un entier strictement plus grand que 1, afficher son plus petit diviseur strictement supérieur à 1.

## **Exemple d'entrée**

```
15
```

## **Exemple de sortie**

```
3
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
i = 2
while a % i != 0:
  i += 1
print(i)
```
````
