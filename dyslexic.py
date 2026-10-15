from math import*
from random import*
Dys = ["dyslexique", "dysorthographique", "dyscalculique", "dysgraphique", "dyspraxique", "dysphasique"]
Noms = ["Axel","Julien Code", "Enzo", "Hannae", "Jonathan", "Mathys", "Timeo", "Tanguy", "Hoffmann", "Gremont"] 
faireSesLacets = True

for i in range(len(Noms)):
    a = randint(0,20)
    if a == 20:
        faireSesLacets = False
        print(Noms[i], "est", Dys[4], "et a du mal à faire ses lacets")
    else:
        b = randint(0,len(Dys))
        if b == len(Dys):
            c = randint(0,3)
            if c == 0:
                print(Noms[i], "est neurotypique, il n'a aucun trouble Dys")
            elif c == 1:
                print(Noms[i], "est autiste")
            elif c == 2:
                print(Noms[i], "est TDAH")
            else:
                print(Noms[i], "est HPI")
        else:
            print(Noms[i], "est ", Dys[b])