'''
Method to reverse a string

This technique reverses a string using reverse iteration with the reversed() built-in function to cycle through the elements in the string in reverse order
and then use .join() method to merge all of the characters resulting from the reversed iteration into a new string.

https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python

--Eigen manier om join() method te uitleggen !
str = 'Python'
reversed =''.join(reversed(str))
print(reversed)
'''

def palindroom_versie_1(str):
     'Bepaal of str een palindroom is'
     reversed_str = ''.join(reversed(str))
     print(str, reversed_str)
     if reversed_str == str:
         return ('{} is een palindroom'.format(str))
     else:
         return('{} is geen palindroom'.format(str))

#controle versie 1

#print(palindroom_versie_1('contents'))
#print(palindroom_versie_1('racecar'))

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Versie 2


def palindroom_versie_2(str):
    'Bepaal of een str een palindroom is'
    reverse_str = str[::-1]
    print(str,reverse_str)
    if reverse_str == str:
        return 'palindroom'
    return 'geen palindroom'



#Controle
print(palindroom_versie_2('content'))
print(palindroom_versie_2('racecar'))