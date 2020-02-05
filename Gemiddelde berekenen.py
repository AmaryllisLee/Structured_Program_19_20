
#Schrijf een functie die het gemiddelde van een lijst met cijfers berkend
def gemiddelde(lst):
    'gemiddelde van een lijst berekenene'
    at= 0
    for i in lst:
        at = at + i
    gem = at//len(lst)
    print(gem)

gemiddelde([1,2,3])

#-------------------------------------------------------------------------------------
#Schrijf een functie die het gemiddelde berkenenen van een lijst die als input
#een lijst van lijstmet zijfers zijn

def gemiddelde_v2(lijst):
    at =0
    lengte = 0
    for i in lijst:
        for j in i:
            at = at  + j
            lengte+=1
    gem = at //lengte
    print(gem)

#controle
gemiddelde_v2([[1,2,3],[4,5,6],[7,8,9]])