import random
import os
import subprocess

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)
guess=0
guesses=7
x=1
corect=False
nummber=random.randint(1,100)


print("""Välkomen till mitt spel!
Du ska gissa ett tal mellan 1 och 100
Du kommer få 7 gissningar på dig att gissa rätt
""")
while True:
    guess=0
    guesses=7
    x=1
    corect=False
    nummber=random.randint(1,100)
    while x!=8:
        
        while True:
            try:
                guess=int(input("Gissnig "+str(x)+":"))
                break
            except:
                print("Skriv bara siffror")

        if nummber == guess:
            print("Du gissade rätt!")
            corect=True
            break
        elif guess<=nummber:
            print("Ditt nummer är för litet")
        elif guess>=nummber:
            print("Ditt nummer är för stort")
        guesses-=1
        x+=1
        print("Du har",guesses,"gissningar kvar")


    if corect==False:
        print("Svaret var",nummber)
    
    answer=input("Om du vill köra igen skriv ja ")
    if answer.upper() != "JA":
        exit()
