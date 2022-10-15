import time
import math


HP = 100
DEF = 100
END = 0
character = []



def start():
    print('UNIVERSE anomaly v1.0 alpha\n')
    print('czy chcesz zacząć grę?')
    odp = input()
    if odp == 'tak':
        gcreator()

def gcreator():
    global character
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
            character.append(gatunek[0])
            kcreator(character)
    elif odp == '2':
        odp2 = input(f'Wybrano rasę {gatunek[1]}. Czy napewno? ')
        print()
        if odp2 != 'tak':
            gcreator()
        else:
            character.append(gatunek[1])
            kcreator(character)
    elif odp == '3':
        odp2 = input(f'Wybrano rasę {gatunek[2]}. Czy napewno? ')
        print()
        if odp2 != 'tak':
            gcreator()
        else:
            character.append(gatunek[3])
            kcreator(character)
    elif odp == '4':
        odp2 = input(f'Wybrano rasę {gatunek[3]}. Czy napewno? ')
        print()
        if odp2 != 'tak':
            gcreator()
        else:
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
    klasyC = ['Assasin', 'Mag', 'Ninja', 'Bogacz', 'Żołnierz']
    klasyK = ['Inżynier', 'Strzelec', 'Pilot', ]
    klasyE = ['Czarownik', 'Wojownik', 'Łucznik']
    klasyBC = ['Czołg', 'Laserowy strzelec']
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
                character.append(klasyK[0])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
        if odp == '2':
            odp2 = input(f'Wybrano klasę {klasyC[1]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                character.append(klasyC[1])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)
        if odp == '3':
            odp2 = input(f'Wybrano klasę {klasyC[2]}. Czy napewno? ')
            if odp2 != 'tak':
                kcreator(character)
            else:
                character.append(klasyC[2])
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
                character.append(klasyBC[1])
                odp3 = input(f'twoja postać to {character}. tak? ')
                if odp3 != 'tak':
                    character.remove(0, 1)
                    gcreator()
                else:
                    historia(character)

def historia(ty):
    print('rok: 32899')
    print('Universe Labs')
    print('Naukowiec1: Reaktor jest przeciążony może wybuchnąć, co skutkuje połączeniem wszstkich alternatywnych światów!')
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
    print('Cały personel jest zmuszony do postępowania zgodnie z procedurą 312 paragrafu 5')
    print('[wycie alarmu]')
    input('<wciśnij enter>')
    print()
    print('Naukowiec2: 1 coś ty zrobił')
    print('Naukowiec1: To nie ja. To yy kazałeś mi to zrobić')
    print('[wycie alarmu]')
    input('<wciśnij enter>')
    print()
    print('J.O.P.U.L 1(Jednostka ochrony placówek Universe Labs):Co wy tu robicie 1 i 2! Macie uciekać do bramy 1!')
    print('J.O.P.U.L 2(Jednostka ochrony placówek Universe Labs): Natychmiast!')
    input('<wciśnij enter>')
    print()
    gra()

def gra():
    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()