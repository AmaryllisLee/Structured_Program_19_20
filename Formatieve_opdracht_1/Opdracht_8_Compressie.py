
'''
Programma dat uit een gegeven bestand een nieuwe bestand maakt,
wwarbij:
1. iedere regel alle spaties en tabs aan het begin van de regek zijn verwijderd
2.alle lege regels zijn verwijderd
'''


def compress(filename):
    # Acces file and store in variable 'content'
    while True:
        try:
            infile = open(filename)
            content = infile.readlines()
            infile.close()
            break
        except:
            print(('Deze bestand bestaat niet'))
            continue
    #Nieuwe bestand maken met het gegevens uit oude bestand met de gegeven voorwaarde
    outfile = open(filename, 'w')
            #print(content)
    for i in content:
        print(i)
        if i == '\n':
            outfile.write(i.strip('\n'))
        elif i[0] =='':
            outfile(i[0].strip(' \t'))
        else:
            outfile.write(i)
    outfile.close()
    print('gelukt')


#TODO \t verwijderen 



compress('test_opdr8.txt')
