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
        randcislo = random.randint(1000, 9999)
        str_cislo = str(randcislo)
        ud = set(str_cislo)
        if len(ud) != 1:
            return randcislo

def bulls_cows_game():
    #vygenerujeme nahodne 4 ciferne cislo
    cislo = generuj_cislo()    
    print("Vítejte ve hře Bulls and Cows! Vašim cílem je uhodnout čtyř ciferné číslo")
    print("pokud uhodnete číslo, i jeho umístění správně, vypíše se 1 bull")
    print("pokud uhodnete pouze číslo a ne jeho umístění, vypíše se Cow")
    pokusy = 0
    max_pokusy = 20

    #timer
    start_časovač = time.time()
    
    while pokusy < max_pokusy:
        odhad = input("zadejte svůj odhad: ")   
        if not odhad.isdigit() or not (1000 <= int(odhad) <= 9999):
            print("Špatný formát čísla, zadejte 4 místné číslo nezačínající nulou")
            continue    
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



    