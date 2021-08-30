# Écrire votre code ci-dessous
class Personne:
  def __init__(self, nom, age, poids, taille):
    self.nom = nom
    self.age = age
    self.poids = poids
    self.taille = taille
  
  def imc(self):
    return self.poids/(self.taille**2)