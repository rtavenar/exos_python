# 3.D. If/else: Échecs : case noire

## **Énoncé**

Étant donnés deux entiers indiquant une case de l'échiquier, affichez OUI si c'est une case noire (marron sur le dessin ci-dessous) ou NON sinon.



## **Exemple d'entrée** #1

```
1
1
```

## **Exemple de sortie** #1

```
OUI
```

## **Exemple d'entrée** #2

```
1
2
```

## **Exemple de sortie** #2

```
NON
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

if (x1 + y1) % 2 == 0:
  print('OUI')
else:
  print('NON')
```
````
