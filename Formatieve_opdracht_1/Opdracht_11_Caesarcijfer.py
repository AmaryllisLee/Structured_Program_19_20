'''
# 1.ask user to cipher or decipher a text
    Cipher:
        Ask for key
        Ask for text
        obtain index of each char in de text
        shift a lst of letters A-Z to the right with key
        for each index --> lst[index)m with lst being shifted letters A-Z
        join together
    Decipher:
        Ask for key
        Ask for text
        shift a lst of letters A-Z to the right with key -> shifted_lst
        obtain index of each chr of text in shifted_list
        for each index --> lst[index)m with lst being shifted letters A-Z



# 2.Enter a key number
# 3. Give translated text
'''


def caesar_translator():
    while True:
        keuze = input('Would you like to cipher or decipher  a text? ')
        if keuze == 'cipher':
            key = input('Enter the key number 1-26: ')
            text= input('what would you like to translate?: ')

             for i in text:

        elif keuze == 'decipher':
            key = input('Enter the key number 1-26: ')
            text = input('what would you like to translate?: ')
            break
        else:
            print('choose between cipher or decipher')



caesar_translator()