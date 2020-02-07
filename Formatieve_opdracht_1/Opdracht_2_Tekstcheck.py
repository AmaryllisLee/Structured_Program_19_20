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

    for let in s1.strip():
        l1.append(let)
    for letter in s2.strip():
        l2.append(letter)

    # print(l1)
    # print(len(l1))
    # print(l2)
    # print(len(l2))

    i = 0
    j = 0
    index = 0
    while i <=len(l1) or j<= len(l2): # TODO regel verbeteren. Doel:
            if l1[i] == l2[j]:
                index = index + 1
                i = i +1
                j = j+ 1
            else:
                break
    return(index)



print(string_strippen())