# 4.3. For: Somme de 10 nombres

## Consigne

10 nombres sont donnés en entrée. Lire chaque nombre et afficher leur somme. Utiliser le moins de variable possible.

## Exemple d'entrée

```
0
1
2
3
4
5
6
7
8
9
```

## Exemple de sortie

```
45
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '4.3.', 'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
result = 0
for i in range(10):
  result += int(input())
print(result)
```
````
