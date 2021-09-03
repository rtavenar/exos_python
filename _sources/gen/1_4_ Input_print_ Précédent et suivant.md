# 1.4. Input/print: Précédent et suivant

## Consigne

Écrire un programme qui lit un nombre entier et affiche le nombre précédent et le nombre suivant (Cf. exemple ci-dessous).

## Exemple d'entrée

```
179
```

## Exemple de sortie

```
Le nombre suivant 179 est 180
Le nombre précédant 179 est 178
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

https://docs.python.org/fr/3/tutorial/inputoutput.html

<div id="pad"></div>
            <script>Pythonpad('pad', {'title': 'Testez votre solution ici', 'src': '# Lire un entier :\n# a = int(input())\n# Afficher la valeur de a :\n# print(a)\n'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
n = int(input())
print('Le nombre suivant ' + str(n) + ' est ' + str(n + 1))
print('Le nombre précédant ' + str(n) + ' est ' + str(n - 1))
```
````
