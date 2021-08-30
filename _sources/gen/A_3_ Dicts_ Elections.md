---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# A.3. Dicts: Elections

## Consigne

La première ligne contient le nombre d'enregistrements. Ensuite, chaque entrée contient le nom du candidat et le nombre de voix qu'il a obtenu dans les différents états. Dénombrer le nombre de voix pour chaque candidat et afficher les candidats et le nombre total des voix qu'ils ont obtenues, dans l'ordre.

## Exemple d'entrée

```
5
McCain 10
McCain 5
Obama 9
Obama 8
McCain 1
```

## Exemple de sortie

```
McCain 16
Obama 17
```

## Aide

http://rtavenar.github.io/teaching/python_poly/html/poly.html#les-dictionnaires

https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries

## Squelette

```{code-cell} python
# Read a string:
# s = input()
# Print a value:
# print(s)
```

````{dropdown} Proposition de solution

```python
n = int(input())
votes_total = {}
for i in range(n):
  candidate, num_votes = input().split()
  if candidate not in votes_total:
    votes_total[candidate] = 0
  votes_total[candidate] += int(num_votes)
for candidate in sorted(votes_total):
  print(candidate, votes_total[candidate])
```
````
