##A compiler avant (fonctions sur les listes chainées)
class Cellule:
    """ définit la classe Cellule"""
    def __init__(self,v,s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        return str(self.valeur)

def estVide(l):
    return l==None


def afficheListe(l):

    res = '| '
    while not estVide(l):
        res+=str(l.valeur)+' '
        l=l.suivante
    return res+'|'

def concatenerListe(l1,l2):

    if l1 is None:
        return l2
    return Cellule(l1.valeur,concatenerListe(l1.suivante,l2))


def reverse(l):
    if l is None:
        return None

    res = None
    while not l is None:

        res = Cellule(l.valeur,res)
        l=l.suivante

    return res
## Tri par selection avec tableaux dynamiques


#Exercice 1

def mini(l,nb):
  nb2 = 0
  a_parc = l[nb:]
  minim = a_parc[0]
  for a in range(len(a_parc)):
    if minim > a_parc[a]: 
      minim = a_parc[a]
      nb2 = a
      
    print(a,a_parc[a],minim,nb + nb2)
  return nb + nb2

liste = [2,3,4,9,5,2,7,6,2,87,6,2,87]

print(mini(liste,7))