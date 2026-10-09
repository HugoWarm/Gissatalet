
'''
Gissa.py: Ett program som genererar ett hemligt nummer och spelaren har 7 gissningar p sig att lista ut nummret

__author__  = "Hugo Warmland"
__version__ = "1.0.0"
__email__   = "hugo.warmland@elev.ga.dbgy.se"
'''

import random
import os
import subprocess
from bcolors import bcolors

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

print(bcolors.PURPLE + """Välkomen till mitt spel!
Du ska gissa ett tal mellan 1 och 100
Du kommer få 7 gissningar på dig att gissa rätt
""")

while True:
    
    guesses=7
    x=1
    corect=False
    nummber=random.randint(1,100)
    while x!=8:
        
        while True:
            try:
                guess=int(input(bcolors.DEFAULT + "Gissnig "+str(x)+":"))
                break
            except:
                print(bcolors.CYAN + "Skriv bara siffror")

        if nummber == guess:
            print(bcolors.GREEN + "Bra jobbat, du gissade rätt!")
            corect=True
            break
        elif guess<=nummber:
            print(bcolors.BLUE + "För litet")
        elif guess>=nummber:
            print(bcolors.RED + "För stort")
        
        guesses-=1
        x+=1
        print(bcolors.CYAN + "Du har",guesses,"gissningar kvar")

    if corect==False:
        print("Svaret var",nummber)

    
    while True:
        answer=input(bcolors.DEFAULT + "Vill du köra igen?")
        if answer.upper() == "JA":
            break
        elif answer.upper() == "NEJ":
            exit()
        else:
            print("skriv ja eller nej")
