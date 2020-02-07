'''
Programma dat de getalleb van 1 tot 100 print.
1. print voor veelvouden van 3 --> 'fizz'
2. print voor veelvouden van 5 --> 'buzz'
3.print voor veelvouden van 3 en 5 --> 'fizzbuzz'
'''

# Versie 1: zonder recursie
def fizzbuzz():
    for i in range(1,101):
        if i%3 == 0:
            if i%5 ==0:
                print('fizzbuzz')
            print('buzz')
        elif  i%5== 0:
            print('buzz')
        else:
            print(i)



#fizzbuzz()

# versie met recursie
def fizzbuzz():
    