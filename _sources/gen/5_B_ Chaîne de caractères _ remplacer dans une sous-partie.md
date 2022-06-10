# 5.B. Chaîne de caractères : remplacer dans une sous-partie

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins deux fois la lettre `h`, remplacer toutes les occurrences de `h` par `H`, sauf la première et la dernière.

## Exemple d'entrée

```
In the hole in the ground there lived a hobbit
```

## Exemple de sortie

```
In the Hole in tHe ground tHere lived a hobbit
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

https://docs.python.org/fr/3.6/library/stdtypes.html#str.find

https://docs.python.org/fr/3.6/library/stdtypes.html#str.rfind

https://docs.python.org/fr/3.6/library/stdtypes.html#str.replace

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '5.B.', 'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères au clavier :\n# s = input()\n# Afficher une chaîne de caractères :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
s = input()
first_pos, last_pos = s.find('h') + 1, s.rfind('h')
left, middle, right = s[:first_pos], s[first_pos:last_pos], s[last_pos:]
print(left + middle.replace('h', 'H') + right)
```
````
