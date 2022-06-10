# 9.2. Sets : nombre d'éléments communs

## Consignes

Étant données deux séries de nombres (séparés par des espaces) entrées au clavier l'une après l'autre, compter combien de nombres de la première série apparaissent dans la seconde et afficher ce comptage.

## Exemple d'entrée

```
1 3 2
4 3 2
```

## Exemple de sortie

```
2
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#set-types-set-frozenset

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '9.2.', 'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères au clavier :\n# s = input()\n# Afficher la valeur de s :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(len(set(input().split()) & set(input().split())))
```
````
