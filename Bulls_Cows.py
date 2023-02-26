"""
Bulls_Cows.py: druhý projekt do Engeto Online Python Akademie
author: Vojtěch Junek
email: vojta.junek@tiscali.cz
discord: jsemnamol#8198
"""
import random
import time    

def generuj_cislo():
    while True:
        rand_number = random.sample(range(1, 10), 4)
        number = ''.join(map(str, rand_number))
        if len(set(number)) == 4:
            return number

def odhad_kontrola():
    while True:
        odhad = input("zadejte svůj odhad. Číslo musí mít 4 číslice a nesmí začínat 0: ")
        if len(odhad) != 4:
            print("špatný formát. Zadejte číslo o 4 číslicích.")
            continue
        elif odhad[0] == '0':
            print("špatný formát. Číslo nemůže začínat nulou.")
            continue
        elif not odhad.isdigit():
            print("špatný formát. Zadejte pouze číslice.")
            continue
        else:
            return odhad     

def bulls_cows_game():    
    cislo = generuj_cislo()    
    print("Vítejte ve hře Bulls and Cows! Vašim cílem je uhodnout čtyř ciferné číslo")
    print("pokud uhodnete číslo, i jeho umístění správně, vypíše se 1 bull")
    print("pokud uhodnete pouze číslo a ne jeho umístění, vypíše se Cow")
    pokusy = 0
    max_pokusy = 20

    #timer
    start_časovač = time.time()
    
    while pokusy < max_pokusy:
        odhad = odhad_kontrola()        
        cows = 0
        bulls = 0
        cislo_str = str(cislo)

        for i in range(4):
            if odhad[i]==cislo_str[i]:
                bulls += 1
            elif odhad[i] in cislo_str:
                cows +=1

        if bulls == 4:
            print("Vyhrávate! hádané číslo bylo: ", cislo)
            ubehly_cas = time.time() - start_časovač
            print("čas hry: ", ubehly_cas,"sekund")
            break
        else:
            pokusy +=1
            print("Cows: ",cows, "Bulls: ", bulls)
            print("zbývá vám ",max_pokusy - pokusy, "pokusů")
            if pokusy == max_pokusy:
                print("Prohráváte, došly vám pokusy. Hádané číslo bylo: ", cislo)
                break
    
bulls_cows_game()





    