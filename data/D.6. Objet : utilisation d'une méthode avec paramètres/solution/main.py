from math import pi

class Cercle:
  def __init__(self, r=15, posX=0, posY=0):
    self.rayon = r		# attribut rayon du cercle
    self.x = posX			# attribut position en X du centre du cercle
    self.y = posY			# attribut position en Y du centre du cercle
  
  def deplacerCentre(self, depX, depY):
    self.x += depX
    self.y += depY
  
# Écrire votre code ci-dessous
monCercle = Cercle(posX=5, posY=10)
monCercle.deplacerCentre(5, -8)