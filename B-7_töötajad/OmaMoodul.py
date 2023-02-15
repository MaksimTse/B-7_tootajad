from math import *

def tootajad(r:list,a:list):
    """lisa tootajad
    :param list r: Inimeste järend
    :param list a: Aastade järend
    :rtype: list, list
    """
    while True:
        try:
            D = int(input('Mitu töötajat sa soovid lisada? '))
            break
        except ValueError:
            print("Sisestus peab olema täisarv!")
    for j in range(D):
        nimi = input('Enter name: ').title()
        vana = int(input('Enter age: '))
        r.append(nimi)
        a.append(vana)
    return (r,a)

def vanad(r:list, a:list):
    """leiab pentsioneerid
    :param list r: Inimeste järend
    :param list a: Aastade järend
    :rtype: list, list
    """
    rabotniki_65 = []
    for i in range(len(r)):
        rab = r[i]
        age = a[i]
        if age > 65:
            rabotniki_65.append(rab)
            print(f'{rabotniki_65} on pentsioneer(id)')
    return(r,a)

def find_average(a:list):
    kesk=(a[0]+a[1])/len(a)
    print(kesk)
    
def oldyoung(r:list):
    """leiab 10 vanam ja 10 noorem
    :param list r: Inimeste järend
    """
    young = [r[0]]
    old = [r[0]]

    for rabot in r[1:]:
        if rabot[1] < young[0][1]:
            young = [r]
        elif r[1] == young[0][1]:
            young.append(r)
        if rabot[1] > old[0][1]:
            old = [rabot]
        elif rabot[1] == old[0][1]:
            old.append(rabot)
    young = young[:2]
    old = old[:2]
    print(young)
    print(old)

def find(a:list):
    """leiab pentsioneerid
    :param list a: Aastade järend
    """
    year=int(input('aasta: '))
    old=2023-year
    found = []
    for i in range(len(a)):
        if a[i] == old:
            found.append(i)
    print(found)
