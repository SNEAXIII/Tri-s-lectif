class Cellule:
    """ définit la classe Cellule
    valeur : attribut qui contient le premier élément
    suivante : attribut qui contient la suite de la liste"""
    def __init__(self,v,n):
        self.valeur = v
        self.suivante = n

    def __str__(self):
        return str(self.valeur)

    def print_lstc(l,rez=""):
        """fonction qui renvoie une chaine de caractères avec les éléments de la liste"""
        while not l is None: rez, l = rez + str(f"[{l.valeur}] "), l.suivante
        return rez

    def concatenerListe(self, l2):
        if self is None :
            return l2
        return Cellule(self.valeur, self.concatenerListe(self.suivante, l2))


class Liste:
    """ Liste des attributs :
    tete -> élément par défaut de la liste étudié
        Liste des méthodes :
    estVide() -> méthode qui teste si la liste est vide ou non
    ajoute() -> méthode qui ajoute un élément à gauche de la liste
    __len__() -> méthode qui calcul le nombre de valeur dans la liste chaînée
    empty_lstc() -> méthode qui teste si la liste l est vide
    __repr__() -> méthode qui renvoie une chaîne de caractères avec les éléments de la liste chaîne
    __getitem__() -> méthode qui permet d'accéder à un élément de la liste
    reverse() -> méthode qui retourne la liste à l'envers
    __add__() -> méthode qui renvoie la concaténation de deux listes l'une derrière l'autre
    listeN() -> méthode qui renvoie les n premiers éléments de la liste
    occurence() -> méthode qui renvoie le nombre d'occurences de la valeur x dans la liste
    trouve() -> méthode qui renvoie le rang de la première occurrence de x dans la liste
    egalite() -> méthode qui regarde si deux listes sont identiques
    suppr() -> méthode qui renvoie un tuple, dont le premier élément est la liste entrée en paramètre, ôtée de l’élément de rang rg, et le deuxième élément est la valeur qui a été supprimée"""

    def __init__(self, *args):
        self.tete = None
        for a in args: self.ajoute(a)

    def estVide(self): return self.tete is None

    def ajoute(self, x): self.tete = Cellule(x, self.tete)

    def empty_lstc(self,l): return l is None


    def __len__(self):
        l=self.tete
        rez = 0
        while not estVide(l):
            l = l.suivante
            rez += 1
        return rez

    def __str__(self,rez=""):
        l = self.tete
        while not self.empty_lstc(l): rez, l = rez + str(f"[{l.valeur}] "), l.suivante
        return rez

    def __getitem__(self,k):
        l = self.tete
        assert (type(k)==int), "index en dehors du rang"
        if k < 0: return self.__getitem__(k%self.__len__())
        while k >= 1 or empty_lstc(l):
            l = l.suivante
            k -= 1 
        return l.valeur

    def reverse(self):
        l = self.tete
        rez = None
        while not l is None:
            rez = Cellule(l.valeur, rez)
            l = l.suivante
        return rez

    def __add__(self,l2):
        
        lst1 = self.tete
        lst2 = l2.tete
        l = concatenerListe(lst1,lst2)
        rez = Liste()
        while l != None:
            rez.ajoute(l)


    def print_lstc(l,rez=""):
        """fonction qui renvoie une chaine de caractères avec les éléments de la liste"""
        while not empty_lstc(l): rez, l = rez + str(f"[{l.valeur}]"), l.suivante
        return rez

    def empty_lstc(l):
        """fonction qui teste si une liste est vide """
        return l is None