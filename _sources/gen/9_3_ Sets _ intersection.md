# 9.3. Sets : intersection

## Consignes

Étant données deux séries de nombres (séparés par des espaces) entrées l'une après l'autre au clavier, trouver tous les nombres qui apparaissent à la fois dans la première et dans la deuxième séries et les afficher par ordre croissant.

## Exemple d'entrée

```
1 3 2
4 3 2
```

## Exemple de sortie

```
2 3
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#set-types-set-frozenset

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '9.3.', 'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères au clavier :\n# s = input()\n# Afficher la valeur de s :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
first = set([int(s) for s in input().split()])
second = set([int(s) for s in input().split()])
print(*sorted(first & second))
```
````
