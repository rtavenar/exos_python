# 4.4. For: Somme de N nombres

## Consigne

N nombres sont donnés en entrés. Lire chaque nombre et afficher la leur somme.

Le premier nombre entré est un entier N, qui est le nombre d'entiers qui seront entrés. Chacune des N entrées contient un entier. Afficher la somme de ces N entiers.


## Exemple d'entrée

```
10
1
2
1
1
1
1
3
1
1
1
```

## Exemple de sortie

```
13
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#boucles-for

https://docs.python.org/fr/3/reference/compound_stmts.html#for

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '4.4.', 'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
result = 0
for i in range(int(input())):
  result += int(input())
print(result)
```
````
