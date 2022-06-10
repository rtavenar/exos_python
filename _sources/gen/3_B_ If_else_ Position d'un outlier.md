# 3.B. If/else: Position d'un outlier

## **Énoncé**

Étant donnés 3 entiers dont deux sont égaux entre eux affichez la position de celui qui est différent des autres (1, 2 ou 3).

## Exemple d'entrée #1

```
10
5
10
```

## Exemple de sortie #1

```
2
```

## Exemple d'entrée #2

```
10
10
5
```

## Exemple de sortie #2

```
3
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '3.B.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher une valeur :\n# print(a)'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
b = int(input())
c = int(input())

if b == c:
  print(1)
elif a == c:
  print(2)
else:
  print(3)
```
````
