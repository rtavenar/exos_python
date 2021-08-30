# B.4 Fonctions : Argument avec une valeur par défaut

**Énoncé**

Codez une fonction somme qui permet d'ajouter au maximum 4 entiers. La fonction prend au minimum 1 entier en paramètre et 4 au maximum.

**Exemple d'appel de la fonction**

```
somme(1,2,3)
```

**Exemple de valeur de retour**

```
6
```

**Aide**

http://rtavenar.github.io/teaching/python_poly/html/poly.html#fonctions

## Squelette

```{code-cell} python
def somme():
  # Codez votre fonction ici
```

````{dropdown} Proposition de solution

```python
def somme(entier1, entier2=0, entier3=0, entier4=0):
  # Codez votre fonction ici
  return entier1+entier2+entier3+entier4
```
````
