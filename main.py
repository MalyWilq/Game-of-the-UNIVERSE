import time
import math
import random


HP = 100
DEF = 100
SPEED = 100
STRG = 100
#STRG - siła
STRGZ = 100
#STRGZ - siła zbrojna
INTL = 100
#INTL - inteligencja
END = 0
character = []



def start():
    print('Game of the UNIVERSE v1.2\n')
    print('czy chcesz zacząć grę?')
    odp = input()
    if odp == 'tak':
        gcreator()

def gcreator():
    global character
    global HP
    global DEF
    global SPEED
    global STRG
    global STRGZ
    global INTL
    gatunek = ['Człowiek', 'Kree', 'Elf', 'Bio-cyborg']
    ccztery = ['']
    print('wybież gatunek')
    for i in range(len(gatunek)):
        print(f'{i+1}. {gatunek[i]}')
    odp = input('wybieram ')
    if odp == '1':
        odp2 = input(f'Wybrano rasę {gatunek[0]}. Czy napewno? ')
        print()
        if odp2 != 'tak':
            gcreator()
        else:
            HP = 100
            DEF = 0
            SPEED = 50
            STRG = 50
            STRGZ = 50
            INTL = 50
            character.append(gatunek[0])
            kcreator(character)
    elif odp == '2':
        odp2 = input(f'Wybrano rasę {gatunek[1]}. Czy napewno? ')
        print()
        if odp2 != 'tak':
            gcreator()
        else:
            HP = 100
            DEF = 50
            SPEED = 40
            STRG = 40
            STRGZ = 100
            INTL = 100
            character.append(gatunek[1])
            kcreator(character)
    elif odp == '3':
        odp2 = input(f'Wybrano rasę {gatunek[2]}. Czy napewno? ')
        print()
        if odp2 != 'tak':
            gcreator()
        else:
            HP = 80
            DEF = 10
            SPEED = 70
            STRG = 30
            STRGZ = 30
            INTL = 40
            character.append(gatunek[3])
            kcreator(character)
    elif odp == '4':
        odp2 = input(f'Wybrano rasę {gatunek[3]}. Czy napewno? ')
        print()
        if odp2 != 'tak':
            gcreator()
        else:
            HP = 200
            DEF = 200
            SPEED = 20
            STRG = 100
            STRGZ = 110
            INTL = 50
            character.append(gatunek[3])
            kcreator(character)
    elif odp == '5':
        odp2 = input(f'Wybrano rasę {gatunek[4]}g. Czy napewno? ')
        print()
        if odp2 != 'tak':
            gcreator()
        else:
            character.append(gatunek[4])
            kcreator(character)
    if odp == 'C4':
        for i in range(i+i):
            print(i)



def kcreator(postać):
    global character
    global HP
    global DEF
    global SPEED
    global STRG
    global STRGZ
    global INTL
    klasyC = ['Assasin', 'Mag', 'Ninja', 'Bogacz', 'Żołnierz']
    klasyK = ['Inżynier', 'Strzelec', 'Pilot', ]
    klasyE = ['Czarownik', 'Wojownik', 'Łucznik']
    klasyBC = ['Czołg', 'Biegacz']
    if postać[0] == 'Człowiek':
        print('Wybierz klasę')
        for i in range(len(klasyC)):
            print(f'{i+1}. {klasyC[i]}')
        odp = input('Wybieram klasę ')
        if odp == '1':
            odp2 = input(f'Wybrano klasę {klasyC[0]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 110
                DEF = 90
                SPEED = 50
                STRG = 70
                STRGZ = 50
                INTL = 50
                character.append(klasyC[0])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0)
                    character.remove(1)
                    gcreator()
                else:
                    historia(character)
        if odp == '2':
            odp2 = input(f'Wybrano klasę {klasyC[1]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 80
                DEF = 10
                SPEED = 10
                STRG = 10
                STRGZ = 67
                INTL = 80
                character.append(klasyC[1])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0)
                    character.remove(1)
                    gcreator()
                else:
                    historia(character)
        if odp == '3':
            odp2 = input(f'Wybrano klasę {klasyC[2]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 60
                DEF = 10
                SPEED = 70
                STRG = 70
                STRGZ = 70
                INTL = 50
                character.append(klasyC[2])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0)
                    character.remove(1)
                    gcreator()
                else:
                    historia(character)
        if odp == '4':
            odp2 = input(f'Wybrano klasę {klasyC[3]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 200
                DEF = 150
                SPEED = 10
                STRG = 10
                STRGZ = 200
                INTL = 60
                character.append(klasyC[3])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0)
                    character.remove(1)
                    gcreator()
                else:
                    historia(character)
        if odp == '5':
            odp2 = input(f'Wybrano klasę {klasyC[4]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 100
                DEF = 200
                SPEED = 60
                STRG = 70
                STRGZ = 80
                INTL = 50
                character.append(klasyC[4])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0)
                    character.remove(1)
                    gcreator()
                else:
                    historia(character)
    if postać[0] == 'Kree':
        print('Wybierz klasę')
        for i in range(len(klasyK)):
            print(f'{i + 1}. {klasyK[i]}')
        odp = input('Wybieram klasę ')
        if odp == '1':
            odp2 = input(f'Wybrano klasę {klasyK[0]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 100
                DEF = 120
                STRG = 60
                STRGZ = 80
                SPEED = 40
                INTL = 100
                character.append(klasyK[0])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
        if odp == '2':
            odp2 = input(f'Wybrano klasę {klasyK[1]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 100
                DEF = 70
                STRG = 60
                STRGZ = 90
                SPEED = 40
                INTL = 60
                character.append(klasyK[1])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
        if odp == '3':
            odp2 = input(f'Wybrano klasę {klasyK[2]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 100
                DEF = 50
                STRG = 50
                STRGZ = 70
                SPEED = 50
                INTL = 60
                character.append(klasyK[2])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
    if postać[0] == 'Elf':
        print('Wybierz klasę')
        for i in range(len(klasyE)):
            print(f'{i + 1}. {klasyE[i]}')
        odp = input('Wybieram klasę ')
        if odp == '1':
            odp2 = input(f'Wybrano klasę {klasyE[0]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 100
                DEF = 80
                STRG = 40
                STRGZ = 100
                SPEED = 60
                INTL = 200
                character.append(klasyE[0])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
        if odp == '2':
            odp2 = input(f'Wybrano klasę {klasyE[1]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 100
                DEF = 20
                STRG = 70
                STRGZ = 50
                SPEED = 60
                INTL = 40
                character.append(klasyE[1])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
        if odp == '3':
            odp2 = input(f'Wybrano klasę {klasyE[2]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 100
                DEF = 10
                STRG = 50
                STRGZ = 80
                SPEED = 80
                INTL = 40
                character.append(klasyE[2])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
    if postać[0] == 'Bio-cyborg':
        print('Wybierz klasę')
        for i in range(len(klasyBC)):
            print(f'{i + 1}. {klasyBC[i]}')
        odp = input('Wybieram klasę ')
        if odp == '1':
            odp2 = input(f'Wybrano klasę {klasyBC[0]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 200
                DEF = 300
                STRG = 200
                STRGZ = 10
                SPEED = 10
                INTL = 30
                character.append(klasyBC[0])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
        if odp == '2':
            odp2 = input(f'Wybrano klasę {klasyBC[1]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                HP = 200
                DEF = 50
                STRG = 50
                STRGZ = 10
                SPEED = 200
                INTL = 60
                character.append(klasyBC[1])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
#        if odp == '3':
#            odp2 = input(f'Wybrano klasę {klasyBC[2]}. Czy napewno? ')
#            if odp2 != 'tak':
#                kcreator(character)
#            else:
#                character.append(klasyBC[1])
#                odp3 = input(f'twoja postać to {character}. tak? ')
#                if odp3 != 'tak':
#                    character.remove(0, 1)
#                    gcreator()
#                else:
#                    historia(character)



def historia(ty):
    print('\nrok: 32899')
    print('Universe Labs')
    print('Naukowiec1: Reaktor jest przeciążony, jak wybuchnie połączą się wszstkie alternatywne światy!')
    input('<wciśnij enter>')
    print()
    print('Naukowiec2: Cicho! Zwiększ moc do 78%.')
    input('<wciścnij enter>')
    print()
    print('Naukowiec1: robi się.')
    print('[syczenia reaktora]')
    input('<wciśnij enter>')
    print()
    print('Naukowiec2: Zwiększ moc do 100% i otwórz portal do wymiaru 379. Jeden portal!')
    input('<wciśnij enter>')
    print()
    print('Naukowiec1: Zwiększam moc do 100%, Wpisuje numer świata, wpisuje liczbę portali, OTWIERAM PORTAL!!!')
    print('[piszczenie przycisków]')
    input('<wciśnij enter>')
    print()
    print('S.O.P.U.L.19(System ochrony placówki Universe Labs 19): Uwaga! Uwaga! Przeciążenie reaktora antymaterii.')
    print('Cały personel jest zmuszony do postępowania zgodnie z procedurą 312')
    print('[wycie alarmu]')
    input('<wciśnij enter>')
    print()
    print('Naukowiec2: 1 coś ty zrobił')
    print('Naukowiec1: To nie ja. To ty kazałeś mi to zrobić')
    print('[wycie alarmu]')
    input('<wciśnij enter>')
    print()
    print('J.O.P.U.L 1(Jednostka ochrony placówek Universe Labs):Co wy tu robicie 1 i 2! Macie uciekać do bramy 1!')
    print('J.O.P.U.L 2(Jednostka ochrony placówek Universe Labs): Natychmiast!')
    input('<wciśnij enter>')
    print()
    nameg()

def nameg():
    global character
    name = input('Jesteś eksperymentem404. Wpisz własne imie:')
    if name == '':
        nameg()
    elif name == 'W123':
        pass
    elif name == 'MWDevTool':
        pass
    else:
        odp = input(f'wybrano imię {name}. Czy potwierdzasz: ')
        if odp != 'tak':
            nameg()
        else:
            character.append(name)
            print(f'Jesteś: Rasa {character[0]}, klasa {character[1]}, imię {character[2]}')


#def historia2(ty):
#    print('\nrok 32928')
#    print('miejsce: 29 lat temu: Universe Labs. Teraz Infinity Labs')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()