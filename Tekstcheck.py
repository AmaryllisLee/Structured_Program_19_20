'''
s1= "laala ik eet uil"
s2= "laala ik eet citroen s'\middag"
lst= []
lst2= []
for i in s1.strip():
    lst.append(i)
for j in s2.strip():
     lst2.append(j)
print(lst)
print(lst2)
print(len(lst), len(lst2))
'''

def string_strippen():
    s1 = input('Input a string: ')
    s2 = input('Input a string: ')
    l1 = []
    l2 = []
    index = 0

    for i in s1.strip():
        l1.append(i)
    for j in s2.strip():
        l2.append(j)

    print(l1)
    print(len(l1))
    print(l2)
    print(len(l2))

    i = 0
    j = 0
    index = 0
    while i <=len(l1) or j<= len(l2): # fout
            if l1[i] == l2[j]:
                index=+1
                i=+1
                j=+1
            else:
                i=+1
                j=+1
    return(index)



print(string_strippen())