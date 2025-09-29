'''Imports et définition des variables globales'''
# Mandatory for the recursive solution to work on large inputs
import sys
sys.setrecursionlimit(2000)


#### Fonctions secondaires


def artcode_i(s,):
    """
    liste de tuple
    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    #votre code ici
    n=len(s)
    c=[s[0]]
    occ=[1]
    k=1
    while  n>k:
        if s[k]==s[k-1]:
            occ[-1] += 1          
        else:
            occ.append(1)
            c.append(s[k])
        l=list(zip(c,occ))
        k+=1
    return l


def artcode_r(s):
    """
    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
        """
    #haut du code
    n=len(s)
    # cas de base
    occ=[1]
    k=1
    if s=="":
        return []
    if k<n :
        occ[-1] += 1
    occ.insert(0, 1)  
    return [(s[0],1)]+artcode_r(s[k:],)
    #recherche nombre de caractères identiques au premier
    #appel récursif
""" Fonction principale"""
def main():
    "afficher le résultat souhaité avec les deux fonctions"
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))

if __name__ == "__main__":
    main()
