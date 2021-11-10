## Exercice 1

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