# 3.L. If/else: Équation linéaire

## **Énoncé**

Écrivez un programme qui résout une équation linéaire _ax = b_ pour des entiers.

Étant donné deux entiers _a_ et _b_ (_a_ pouvant valoir 0), affichez l'entier racine de l'équation s'il existe, "pas de solution" ou "multiples solutions" sinon.

## Exemple d'entrée #1

```
1
-2
```

## Exemple de sortie #1

```
-2
```

## Exemple d'entrée #2

```
2
-1
```

## Exemple de sortie #2

```
pas de solution
```

## Aide

https://rtavenar.github.io/poly_python/content/struct.html#structures-de-controle

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '3.L.', 'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher une valeur :\n# print(a)'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
b = int(input())

if a == 0:
  if b == 0:
    print('multiples solutions')
  else:
    print('pas de solution')
elif b % a == 0:
  print(b // a)
else:
  print('pas de solution')
```
````
