# 1.6. Input/print: Heures et minutes

## Consigne

Soit un entier N, représentant le nombre de secondes écoulées depuis minuit, calculer le nombre d'heures entières et le nombre de minutes entières écoulées depuis minuit.


Le programme devra afficher les deux nombres : le nombre d'heures (entre 0 et 23) et le nombre de minute (entre 0 et 1339).


Par exemple, si N = 3900, alors 3900 secondes se sont écoulées depuis minuit (il est donc 1h05). Le programme devra afficher **1 65** ( 1 heure entière depuis minuit, 65 minutes entières depuis minuit).

## Exemple d'entrée

```
3900
```

## Exemple de sortie

```
1 65
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '1.6.', 'title': 'Testez votre solution ici', 'src': '# Read an integer:\n# a = int(input())\n# Print a value:\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
num_seconds = int(input())
print(num_seconds // 3600, num_seconds // 60)
```
````
