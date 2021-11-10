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

def mini(tab,rgDepart):


    return

def triSelect(tab):

    return

l = [5,7,1,9,11,2,4,15,3]

print(mini(l,3))





##Exercice 2

#2.1
def min(lst):


    return






#2.2
def suppr(val,lst):


    return




#2.3
def triSelect2(lst):


    return

lst = Cellule(5,Cellule(2,Cellule(7,Cellule(13,Cellule(1,None)))))

print(triSelect2(lst))

##Tri par insertion

#Exercice 3
l = [5,7,1,9,11,2,4,15,3]
def TriInsert(tab):


    return

print(TriInsert(l))

## Exercice 4


lst = Cellule(5,Cellule(2,Cellule(7,Cellule(13,Cellule(1,None)))))

def ranger(val,lst):

    return

def triInsert2(lst):

    return

##Exercice 5  Fusion de listes triées

def fusion(lst1,lst2):


    return

##Exercice 6 : Tri Fusion


lst = Cellule(5,Cellule(2,Cellule(7,Cellule(13,Cellule(1,None)))))


def triFusion(lst):

    return

print(triFusion(lst))

##Exercice 7

def fusion2(t1,t2):
    """fusionne deux tableaux dont les éléments sont ordonnés en un seul tableau ordonné formé des valeurs des deux tableaux"""

    return


tab1=[3,5,8,10]
tab2=[1,4,9,11,13,15]

print(fusion2(t1,t2))

def triFusion2(tab):
    """trie l'ensemble des valeurs de tab avec la méthode du tri fusion"""



    return

t=[5,1,9,14,7,3,4,12]
print(triFusion2(t))