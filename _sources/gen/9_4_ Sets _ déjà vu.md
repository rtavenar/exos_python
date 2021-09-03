# 9.4. Sets : déjà vu

## Consignes

Étant donnée une série de nombres (séparés par des espaces) entrée au clavier, les analyser de gauche à droite et pour chaque nombre, afficher `YES` si ce nombre a déjà été rencontré dans la série, et `NO` s'il apparaît pour la première fois

## Exemple d'entrée

```
1 2 3 2 3 4
```

## Exemple de sortie

```
NO
NO
NO
YES
YES
NO
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#set-types-set-frozenset

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères au clavier :\n# s = input()\n# Afficher la valeur de s :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = [int(s) for s in input().split()]
seen = set()
for i in a:
  if i in seen:
    print('YES')
  else:
    print('NO')
  seen.add(i)
```
````
