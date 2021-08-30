from math import pi

class Cercle:
  def __init__(self, r=15, posX=0, posY=0):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle
  
  def calculerSurface(self):
    return pi*self.rayon**2
  
# Écrire votre code ci-dessous
monCercle = Cercle(r=20)
surface = monCercle.calculerSurface()
print(surface)
