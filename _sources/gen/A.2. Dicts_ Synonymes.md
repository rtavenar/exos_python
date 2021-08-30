# A.2. Dicts: Synonymes

## Consigne

Soit un dictionnaire composé de paires de mots. Chaque mot est un synonyme de l'autre mot dans sa paire.

À partir d'une liste de paires de mots, vous devrez créer un tel dictionnaire.

À la suite du dictionnaire, l'utilisateur propose un mot en entrée pour obtenir le synonyme. La réponse sera la valeur correspondant à la clé (mot proposé en entrée).


## Exemple d'entrée

```
3
Hello Hi
Bye Goodbye
List Array
Goodbye
```

## Exemple de sortie

```
Bye
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

## Proposition de solution

```python
synonyms = {}
for i in range(int(input())):
  w1, w2 = input().split()
  synonyms[w1] = w2
  synonyms[w2] = w1
print(synonyms[input()])
```

