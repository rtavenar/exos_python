# A.4. Dicts: Mot le plus fréquent

## Consigne

À partir d'un texte contenant n lignes, la première entrée correspondra au nombre de lignes n puis chaque ligne du texte sera entrée l'une après l'autre.

Affichez le mot le plus fréquent du texte. Si plusieurs mots ont la même fréquence, on choisira le premier du classement alphabétique.

## Exemple d'entrée

```
2
apple orange banana
```

```
banana orange
```

## Exemple de sortie

```
banana
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#les-dictionnaires

https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries

## Squelette

```python
# Read a string:
# s = input()
# Print a value:
# print(s)
```

````{dropdown} Proposition de solution

```python
words_count = {}
for i in range(int(input())):
  words = input().split()
  for word in words:
    if word not in words_count:
      words_count[word] = 0
    words_count[word] += 1
max_frequency = max(words_count.values())
for word in sorted(words_count):
  if words_count[word] == max_frequency:
    print(word)
    break
```
````
