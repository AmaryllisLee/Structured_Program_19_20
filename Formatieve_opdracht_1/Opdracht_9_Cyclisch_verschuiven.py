'''
Functie met twee parameters, ch en n
ch: byte char
n : hoeveel posities de bitjes van ch opgeschoven moeten
    1.n > 0:
            ch schuift naar links met n posities
    2.n < 0:
            ch schuift naar rechts met n posities
    !. Bitjes die wegvallen wprden aan de andere kant van de byte teruggeplaats
'''

def bitjes_verschuiven (ch,n):
    'Schuif een byte met n posities'
    if n > 0 or n<0:
        ch = ch[n:] + ch[:n] 
        return ch
    else: # n == 0
        return ch

#Controle
print(bitjes_verschuiven('1011100',3))
'''
my_string = 'hello'
my_string = my_string[1:] + my_string[:1] #moves char to left with a position of 2

#mystring2 = my_string[-2:] + my_string[:-2]# moving char to the right with a position of 2
print(my_string)
#, mystring2)

'''


#Bron : https://stackoverflow.com/questions/33192395/python-how-to-move-characters-in-string-by-x-amount