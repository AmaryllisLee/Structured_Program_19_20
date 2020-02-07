#Bedenk en schrijf zelf een functie die een lijst met getallen op volgorde sorteert
def sorteren(lst):
    i = 0
    a = 0
    while a <= len(lst):
        if i >= len(lst):
            print(lst)
            break
        else:
            index_max = lst.index(max(lst))-i
            del lst[index_max]
            lst.insert(-1-i,lst[index_max])
            i = i +1
            a = a + 1



sorteren([5,8,2,10])

# kom tot nu nie uit