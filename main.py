import sqlite3
import os
import random

c = sqlite3.connect("terra.db")
#cursor = c.cursor()
#
#files = os.listdir("mondial_sqlite/sql/data")
#for file in files:
#    #commands = [cmd for cmd in open(f"mondial_sqlite/sql/data/{file}").read().replace("\n", " ").split(";")]
#    #for cmd in commands:
#    #    print(cmd)
#    #    cursor.execute(cmd)
#    with open(f"mondial_sqlite/sql/data/{file}", "r") as sql_file:
#        sql_script = sql_file.read()
#    print(sql_script)
#    print(file)
#    cursor.executescript(sql_script)
#
#cursor.close()



def GameBundeslaenderUndHauptstadt():
    cursorBLHS = c.cursor()
    cursorBLHS.execute("SELECT Name, Capital FROM Province WHERE Country = 'D'")
    bundeslaender = cursorBLHS.fetchall()
    score = 0
    for x in range(16):
        ans = input(f"Wie heißt die Hauptstadt von {bundeslaender[x][0]}? \n")
        if ans.lower() == bundeslaender[x][1].lower():
            print(f"Richtig die Hauptstadt von {bundeslaender[x][0]} ist {bundeslaender[x][1]}.")
            score += 1
        else:
            print(f"Leider Falsch. Die Hauptstadt von {bundeslaender[x][0]} ist {bundeslaender[x][1]}")
    print(f"Du hast {score} Hauptstädte richtig erraten.")
    cursorBLHS.close()
    return

def GameBundeslaenderAufzählen():
    cursorBLR = c.cursor()
    cursorBLR.execute("SELECT Name FROM Province WHERE Country = 'D'")
    bundeslaender = cursorBLR.fetchall()
    erraten = []
    triesLeft = 20
    while triesLeft > 0 and len(erraten) < 16:
        guessW = False
        guess = input(f"Nenne ein Bundesland. Du hast noch {triesLeft} Versuche.\n")
        if guess in erraten:
            print(f"{guess} hast du schon erraten.")
            guessW = True
        else:
            for b in bundeslaender:
                if guess.lower() == b[0].lower():
                    print(f"{guess} ist ein Bundesland")
                    erraten.append(b[0])
                    guessW = True
                    break
        if not guessW:
            print(f"{guess} ist kein Bundesland.")
                    
        triesLeft -= 1
    if len(erraten) != 16:
        print(f"Du hast {len(erraten)} Bundesländer richtig erraten. \nHier ist die Liste: {erraten}.\nHier ist eine Liste aller Bundesländer: {bundeslaender}")
    else:
        print(f"Du hast alle Bundesländer erraten. Sehr gut.")
    cursorBLR.close()
    return

def HigherLowerCountry():
    cursorHL = c.cursor()
    cursorHL.execute("SELECT Name, Population FROM Countries")
    countries = cursorHL.fetchall()
    firstCountry = countries[random.randint(0, len(countries))]
    while True:
        secondCountry = countries[random.randint(0, len(countries))]
        guess = input(f"Hat {secondCountry[0]} mehr Einwohner als {firstCountry[0]}?\n ")