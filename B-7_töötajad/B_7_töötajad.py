from OmaMoodul import *

rabotniki=[]
aastat=[]

rabotniki,aastat=tootajad(rabotniki, aastat)
print(rabotniki, aastat)
menu=int(input('1-\n2-\n3-\n4-\n5-\n'))
while True:
    if menu==1:
        vanad(rabotniki, aastat)
        break
    elif menu==2:
        find_average(rabotniki, aastat)
        break
    elif menu==3:
        oldyoung(rabotniki)
        break
    elif menu==4:
        find(aastat)
        break
    else:
        print("Kirjuta õige arv")
        break