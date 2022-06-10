# 6.3. While: Puissances de 2

## **Énoncé**

Étant donné un entier X, on cherche le plus grand entier **n** pour lequel **2ⁿ** est inférieur ou égal à X. Affichez **n** et **2ⁿ**.


## **Exemple d'entrée**

```
50
```

## **Exemple de sortie**

```
5 32
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-while

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '6.3.', 'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
x = int(input())
n = 1
while 2 ** n <= x:
  n += 1
print(n - 1, 2 ** (n - 1))
```
````
