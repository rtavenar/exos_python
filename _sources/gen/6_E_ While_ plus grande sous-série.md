# 6.E. While: plus grande sous-série

## Consignes

Étant données une série d'entiers non négatifs entrés au clavier un par un (un entier par ligne) et se terminant par `0`,  déterminer et afficher la longueur de la plus grande sous-série de nombres identiques à l'intérieur de la série saisie.

## Exemple d'entrée

```
1
**7**
**7**
**7**
9
1
1
0
```

(les nombres appartenant à la sous-série maximale sont soulignés)

## Exemple de sortie

```
3
```

## Aide

https://docs.python.org/fr/3.6/reference/compound_stmts.html#the-while-statement

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '6.E.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier au clavier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
next = int(input())
length = 1
max_length = 1
while next != 0:
  prev, next = next, int(input())
  if prev == next:
    length += 1
  else:
    length = 1
  max_length = max(length, max_length)
print(max_length)
```
````
