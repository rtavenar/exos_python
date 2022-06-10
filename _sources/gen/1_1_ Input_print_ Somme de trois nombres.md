# 1.1. Input/print: Somme de trois nombres

## Consigne

Écrire un programme qui prend 3 nombres et affiche leur somme. Chaque nombre sera entré séparément.

## Exemple d'entrée

```
2
3
6
```

## Exemple de sortie

```
11
```

## Aide

https://rtavenar.github.io/poly_python/content/intro.html

https://docs.python.org/fr/3/tutorial/inputoutput.html

<div id="pad"></div>
            <script>Pythonpad('pad', {'id': '1.1.', 'title': 'Testez votre solution ici', 'src': '# Ce programme lit 2 nombres et affiche leur somme :\na = int(input())\nb = int(input())\nprint(a + b)\n\n# Vous pouvez modifier ce programme pour lire et faire la somme de 3 nombres'})</script>


````{admonition} Cliquez ici pour voir la solution
:class: tip, dropdown

```python
a = int(input())
b = int(input())
c = int(input())
print(a + b + c)
```
````
