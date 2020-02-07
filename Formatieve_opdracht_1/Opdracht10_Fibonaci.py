'''
Implementeer de fibonaci sequence met behulp van recursie 
Bron: itroduction to computing python 2nd edition pg 349
'''

def fibonaci(fn):
    
    if fn < 2:  
        return 1
    else:
        return fibonaci(fn-1)+fibonaci(fn-2)


fibonaci(3)

