# 9.1. Sets : nombre d'éléments distincts

## Consignes

Étant donnée une série d'entiers (séparés par des espaces) entrée au clavier, compter combien de nombres différents elle contient et afficher ce comptage. Ce problème peut être résolu en une seule ligne.

## Exemple d'entrée

```
1 2 3 2 1
```

## Exemple de sortie

```
3
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#set-types-set-frozenset

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères au clavier :\n# s = input()\n# Afficher la valeur de s :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
print(len(set(input().split())))
```
````
