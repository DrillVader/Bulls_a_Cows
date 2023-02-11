"""
Bulls_Cows.py: druhý projekt do Engeto Online Python Akademie
author: Vojtěch Junek
email: vojta.junek@tiscali.cz
discord: jsemnamol#8198
"""





import random
import time

def bullscowsgame():
    #vygenerujeme nahodne 4 ciferne cislo
    randomcislo = str(random.randint(1000,9999))
    print("Vítejte ve hře Bulls and Cows! Vašim cílem je uhodnout čtyř ciferné číslo")
    print("pokud uhodnete číslo, i jeho umístění správně, vypíše se 1 bull")
    print("pokud uhodnete pouze číslo a ne jeho umístění, vypíše se Cow")
    pokusy = 0
    max_pokusy = 20

    #timer
    start_časovač = time.time()

    while pokusy < max_pokusy:
        guess = input("zadejte svůj odhad: ")        
        cows = 0
        bulls = 0

        for i in range(4):
            if guess[i]==randomcislo[i]:
                bulls += 1
            elif guess[i] in randomcislo:
                cows +=1

        if bulls == 4:
            print("Vyhrávate! hádané číslo bylo: ", randomcislo)
            ubehly_cas = time.time() - start_časovač
            print("čas hry: ", ubehly_cas,"sekund")
            break
        else:
            pokusy +=1
            print("Cows: ",cows, "Bulls: ", bulls)
            print("zbývá vám ",max_pokusy - pokusy, "pokusů")
            if pokusy == max_pokusy:
                print("Prohráváte, došly vám pokusy. Hádané číslo bylo: ", randomcislo)
                break

    
if __name__ == "__main__":
    bullscowsgame()
    

    