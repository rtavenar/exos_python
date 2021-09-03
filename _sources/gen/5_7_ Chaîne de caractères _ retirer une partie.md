# 5.7. Chaîne de caractères : retirer une partie

## Consignes

Étant donnée une chaîne de caractères entrée au clavier contenant au moins deux fois la lettre `h`, retirer de cette chaîne la première et la dernière occurrence de la lettre `h` ainsi que tous les caractères se trouvant entre ces deux occurrences.

## Exemple d'entrée

```
In the hole in the ground there lived a hobbit
```

## Exemple de sortie

```
In tobbit
```

## Aide

https://docs.python.org/fr/3.6/library/stdtypes.html#common-sequence-operations

https://docs.python.org/fr/3.6/library/stdtypes.html#str.find

https://docs.python.org/fr/3.6/library/stdtypes.html#str.rfind


<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire une chaîne de caractères :\n# s = input()\n# Afficher une chaîne de caractères :\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
s = input()
print(s[:s.find('h')] + s[s.rfind('h') + 1:])
```
````
