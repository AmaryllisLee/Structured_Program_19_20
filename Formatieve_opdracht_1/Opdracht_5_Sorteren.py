#Bedenk en schrijf zelf een functie die een lijst met getallen op volgorde sorteert
def sorteren(lst):
    print(lst)
    a= 0
    for i in lst:
        if i == max(lst):
            lst.remove(i)
            #lst[len(lst)-a:]=i # TODO regel verbeteren: doel maximum van de lijst aan het eind van de lijst lst zetten
            #a+=1
        else:
            continue
    return lst


print(sorteren([1,4,5,2,3]))
