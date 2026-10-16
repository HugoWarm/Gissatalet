
'''
Gissa.py: Ett program som genererar ett hemligt nummer och spelaren har 7 gissningar på sig att lista ut nummret

__author__  = "Hugo Warmland"
__version__ = "1.0.0"
__email__   = "hugo.warmland@elev.ga.dbgy.se"
'''

import random
import os
import subprocess
from bcolors import bcolors

subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)



while True:
    print(bcolors.LIGHT_PURPLE + """--------------------------------------------------
          Välkomen till mitt spel!
    Du ska gissa ett tal mellan 1 och 100
Du kommer få 7 gissningar på dig att gissa rätt
        Om du vill avsulta skirv: 0
--------------------------------------------------
    """)
    guesses=7
    x=1
    corect=False
    nummber=random.randint(1,100)
    färg=46
    
    while x!=8:
        
        while True:
            try:
                guess=int(input(f"\033[38;5;{färg}mGissnig {x}:\033[0m"))
                break
            except:
                print(bcolors.CYAN + "Skriv bara siffror")
        if guess == 0:
            exit()
        if nummber == guess:
            print(bcolors.GREEN + "Bra jobbat, du gissade rätt!\nDu har",str(guesses-1),"gissningar kvar")
            corect=True
            break
        elif guess<=nummber:
            print(bcolors.BLUE + "För litet")
        elif guess>=nummber:
            print(bcolors.RED + "För stort")
        if guesses==7:
            färg=46
        elif guesses==6:
            färg=118
        elif guesses==5:
            färg=190
        elif guesses==4:
            färg=226
        elif guesses==3:
            färg=214
        elif guesses==2:
            färg=202
        elif guesses==1:
            färg=196
        
        guesses-=1
        x+=1
    

    if corect==False:
        print(bcolors.RED + "Du förlorade....")
        print(bcolors.RED + "Svaret var",nummber)

    
    while True:
        answer=input(bcolors.DEFAULT + "Vill du köra igen?")
        if answer.upper() == "JA":
            break
        elif answer.upper() == "NEJ":
            exit()
        else:
            print("Skriv ja eller nej")