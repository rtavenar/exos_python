# 6.A. While: Nombre d'éléments pairs

## **Énoncé**

Étant donnée une séquence d'entiers positifs, où chaque entier est écrit sur une ligne distincte, affichez le nombre de valeurs paires lues **avant** de rencontrer un 0.

## **Exemple d'entrée**

```
2
1
4
0
```

## **Exemple de sortie**

```
2
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
num_even = 0
while a != 0:
  if a % 2 == 0:
    num_even += 1
  a = int(input())
print(num_even)
```
````
