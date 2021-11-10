class Cellule:
    """ définit la classe Cellule"""
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s

    def __str__(self):
        return str(self.valeur)


def estVide(l):
    return l == None


def afficheListe(l):

    res = '| '
    while not estVide(l):
        res += str(l.valeur) + ' '
        l = l.suivante
    return res + '|'


def concatenerListe(l1, l2):

    if l1 is None:
        return l2
    return Cellule(l1.valeur, concatenerListe(l1.suivante, l2))


def reverse(l):
    if l is None:
        return None

    res = None
    while not l is None:

        res = Cellule(l.valeur, res)
        l = l.suivante

    return res


## Exercice 2
from TPrep import *

def min(lst):
  """fonction qui renvoit la valeur minimale d'une liste chainée"""
  