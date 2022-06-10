# 5.C. Chaînes de caractères : retirer un caractère tous les trois caractères

## Consignes

Étant donnée une chaîne de caractères entrée au clavier, retirer tous ses caractères dont les indices sont divisibles par 3.

## Exemple d'entrée

```
Python
```

## Exemple de sortie

```
yton
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '5.C.', 'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères :\n# s = input()\n# Afficher une chaîne de caractères :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
s = input()
t = ''
for i in range(len(s)):
  if i % 3 != 0:
    t += s[i]
print(t)
```
````
