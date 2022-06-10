# A.1. Dicts: Nombre d'occurrences

## Consigne

Le texte, composé de mots séparés par un espace, est entré sur une seule ligne (et lu en une seule fois). Pour chaque mot du texte, il faut compter et afficher le nombre d'occurrences préalables de ce mot (i.e.,  le nombre de fois qu'il est déjà apparu à gauche, avant le mot courant).

## Exemple d'entrée

```
one two one two three two four three
```

## Exemple de sortie

```
0 0 1 1 0 2 0 1
```

## Aide

https://rtavenar.github.io/poly_python/content/dict.html

https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'A.1.', 'title': 'Testez votre solution ici', 'src': '# Read a string:\n# s = input()\n# Print a value:\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
text = input().split()
times_seen = {}
for word in text:
  if word not in times_seen:
    times_seen[word] = 0
  print(times_seen[word], end=' ')
  times_seen[word] += 1
```
````