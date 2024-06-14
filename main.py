import sqlite3
import os
import random

c = sqlite3.connect("terra.db")
print(f"\033[1;37m") #Set text color to white
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
    game = True
    score = 0
    cursorHL = c.cursor()
    cursorHL.execute("SELECT Name, Population FROM Country")
    countries = cursorHL.fetchall()
    firstCountry = countries[random.randint(0, len(countries))]
    while game:
        secondCountry = countries[random.randint(0, len(countries))]
        if firstCountry[0] == secondCountry[0]:
            break
        guess = input(f"Hat {secondCountry[0]} mehr Einwohner als {firstCountry[0]}?\n1 steht für Ja 2 für Nein\n{firstCountry[0]} hat {firstCountry[1]} Einwohner\n")
        if guess.lower() in ["high", "higher", "ja", "mehr", "1"] and secondCountry[1] >= firstCountry[1]:
            score += 1
            print(f"\nRichig {secondCountry[0]} mit {secondCountry[1]} Einwohnern hat mehr Einwohner als {firstCountry[0]} mit {secondCountry[1]} Einwohnern.\n\nAktueller Score:\033[1;31m {score}\n\033[1;37m")
        elif guess.lower() in ["low", "lower", "nein", "weniger", "2"] and secondCountry[1] <= firstCountry[1]:
            score += 1
            print(f"\nRichig {secondCountry[0]} mit {secondCountry[1]} Einwohnern hat weniger Einwohner als {firstCountry[0]} mit {firstCountry[1]}.\n\nAktueller Score:\033[1;31m {score}\n\033[1;37m")
        else:
            print(f"\nDas ist leider Falsch. {secondCountry[0]} hat {secondCountry[1]} Einwohner und {firstCountry[0]} hat {firstCountry[1]}\nDein finaler Score war\033[1;31m {score}\n \033[1;37m")
            game = False
        firstCountry = secondCountry


def HauptstädteDerWelt():
    cursorHDW = c.cursor()
    cursorHDW.execute("SELECT Name, Capital FROM Country")
    countries = cursorHDW.fetchall()
    games = int(input(f"Wie viele Runden möchtest du spielen?\n"))
    counter = 0
    score = 0

    while counter < games:
        country = countries[random.randint(0, len(countries))]
        guess = input(f"Runde {counter + 1}:\nWas ist die Hauptstadt von \033[1;31m{country[0]}\033[1;37m?\n")

        if guess.lower() == country[1].lower():
            score += 1
            print(f"Das ist Richtig.\n\nAktueller Score: \033[1;31m{score}\033[1;37m\n")
        else:
            print(f"Leider Falsch.\nDie Hauptstadt von {country[0]} ist \033[1;32m{country[1]}\033[1;37m.\n\nAktueller Score: \033[1;31m{score}\033[1;37m\n")
        counter += 1
    
    print(f"Du hast {counter} Runden gespielt.\nDein finaler Score war \033[1;31m{score}\033[1;37m.\n")

GameBundeslaenderUndHauptstadt()