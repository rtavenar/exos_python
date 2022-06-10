# 6.F. While: nombres de Fibonacci

## Consignes



Les nombres de Fibonacci sont les nombres de la suite d'entiers commençant par `1,1` et où chaque nombre après ces deux premiers est la somme des deux précédents :

`1,1,2,3,5,8,13,21,34,...`

Étant donné un entier strictement positif `n` entré au clavier, calculer et afficher le `n`ième nombre de la suite de Fibonacci.

## Exemple d'entrée

```
6
```

## Exemple de sortie

```
8
```

## Aide

https://docs.python.org/fr/3.6/reference/compound_stmts.html#the-while-statement

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '6.F.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier au clavier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
prev, next = 1, 1
n = int(input())
for i in range(n - 2):
  prev, next = next, prev + next
print(next)
```
````
