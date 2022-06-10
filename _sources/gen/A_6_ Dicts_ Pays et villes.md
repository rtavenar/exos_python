# A.6. Dicts: Pays et villes

## Consigne

Soit une liste de pays contenant une liste de villes appartenant à ce pays. On commencera par préciser le nombre de pays dont on souhaite énumérer une liste de ville lui appartenant. Puis pour chaque pays on entrera sur une ligne le nom du pays puis la liste des villes.

On entrera ensuite le nombre de villes dont on souhaite connaître le pays, puis on entrera le nom de chaque ville sur une ligne. Le programme répondra en affichant le pays correspondant à chaque ville.

## Exemple d'entrée

```
2
USA Boston Pittsburgh Washington Seattle
UK London Edinburgh Cardiff Belfast
3
Cardiff
Seattle
London
```

## Exemple de sortie

```
UK
USA
UK
```

## Aide

https://rtavenar.github.io/poly_python/content/dict.html

https://docs.python.org/fr/3/tutorial/datastructures.html#dictionaries

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': 'A.6.', 'title': 'Testez votre solution ici', 'src': '# Read a string:\n# s = input()\n# Print a value:\n# print(s)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
city_country = {}
for _ in range(int(input())):
  country, *cities = input().split()
  for city in cities:
    city_country[city] = country
for _ in range(int(input())):
  print(city_country[input()])
```
````