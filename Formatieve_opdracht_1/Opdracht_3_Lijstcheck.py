# a Functie count die berekent hoe vaak een geheel getal x in een lijst voorkomt
def count(lst):
    aantal_geheel_getallen= []
    for i in lst:
        try :
            int(i)
            aantal_geheel_getallen.append(i)
        except:
            continue
    return aantal_geheel_getallen



print('Er zitten {} in dit lijst'.format(count([2,5,6,7,8])))
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#b Schrijf een functie die een gegeve lijst het grootste verschil tussen twee op een volgende getallen bepaalt?

def grootste_verschil(lst):
    'grootste verschil bepalen tussen twee op een een volgende getallen van een gegeven lijst'
    verschil_lijst=[]
    i=0

    while i<=(len(lst)-1):
        if i == len(lst)-1:
            return max(verschil_lijst)
        else:
            getallen_aftrekken = lst[i+1]-lst[i]
            verschil_lijst.append(getallen_aftrekken)
            i+=1


print('Het grootste verschil tussen twee op een volgende getallen van de lijst is {} '.format(grootste_verschil([2,5,6,7,8])))

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
c Schrijf een functie ,die bepaalt of een gegeven lijst met alleen 1'en en 0'en aan de eisen voldoet.
    1. aantal 1'en > aantal 0'en
    2. Er mogen niet meer dan 12  0'en zijn
'''
def lijst_voldoen(lst):
    'Bepaal of een lijst voldoet aan de eisen hierboven'
    lijst_nul_een = []
    lst_int = count(lst) # Int van lst in een lijst zetten
    for i in lst_int:       # Lijst filteren om alleen ene lijst van 0'en en 1'en te krijgen en toeveogen in lijst lijst_nul_een
        if i == 0 or i==1:
            lijst_nul_een.append(i)
    #Bepaal of lijst_nul_een voldoet aan eisen
    if lijst_nul_een.count(0) >= 12:
        return 'Voldoen niet aan de eisen'
    elif lijst_nul_een.count(1)<=lijst_nul_een.count(0):
        return 'Voldoen niet aan de eisen'
    else:
        return 'Lijst voldoen aan de eisen'

#controle
print(lijst_voldoen([1,3,4,7,'string', 'word', 1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0]))
#Output : Voldoen niet aan de eisen
