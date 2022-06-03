"""
Repozitorijs `https://github.com/pikcrvt-students/PB2-py-sistema-math`

Sistēma ar kuras palīdzību skolotāja pārbauda audzēkņu zināšanas
ar vairākām tēmām(šobrīd vienu), uzdod uzdevumus patstāvigajam
darbam un kontroldarbus.

Darbā tiek izmantoti divdimensiju masīvi un failu lasīšana.
Jebkurš izlasot kodu spēs uztaisīt tādu pašu sistēmu.

Iekļautā funkcionalitāte: tēmu izvēle - tās teorija, uzdevumi un
kontroldarbi, kuri tiek vērtēti ballēs.

Izveidoja: Matīss Božko
"""
from os import system, path
from random import randint
sistemas_nosaukums = 'Matemātikas Sistēma: Math'
noklusejuma_temas_nosaukums = 'Tēma1'
noklusejuma_temas_teorija = 'Tēmas {} teorijas fails...\n'

temas = None
temu_fails = 'Tēmas.txt'
teoriju_faili = 'teorija/{}.txt'
if not path.exists(temu_fails):
    f = open(temu_fails, 'w', encoding='utf-8')
    f.write(f'{noklusejuma_temas_nosaukums}\n')
    f.close()
    temas = [noklusejuma_temas_nosaukums]
else:
    f = open(temu_fails, 'rt', encoding='utf-8')
    temas = f.read().splitlines()
    f.close()

temas_izveles = [str(x + 1) for x in range(len(temas) + 1)]
teorija = []


def test() -> None:
    pass


def option_choice(prompt: str, options: list) -> str:
    while True:
        inp = input(prompt)
        if inp in options:
            return inp
        print('Ievades kļūda!')


def apskatit_teoriju(temas_indekss: int) -> None:
    print('Teorija par tēmu:', temas[temas_indekss])
    print()
    print(teorija[temas_indekss])
    input('Uzspiediet ENTER, lai turpinātu...')


def arit_prog1() -> tuple:
    punkti_max = 4
    punkti = 0
    print(f'Jūs varat iegūt {punkti_max} punktus par šo uzdevumu.\n')

    sakuma_vertiba = randint(0, 20)
    konstants = 1
    solis = randint(2, 10)
    ntais_loceklis = randint(10, 30)
    nta_vertiba = sakuma_vertiba + (ntais_loceklis - konstants) * solis
    print('Dota virkne ', end='')
    for n in range(1, 6):
        an = sakuma_vertiba + (n - konstants) * solis
        print(an, end='; ')
    print('... ir aritmētiskā progresija.')
    print('Uzraksti vispārīgā locekļa formulu!')
    print('An = a + (n - b) * c')
    print()

    inp_sakuma_vertiba = input('Ievadiet sākuma vērtību a: ')
    inp_konstants = input('Ievadiet konstantu b: ')
    inp_solis = input('Ievadiet soli c: ')
    print(f'Jūsu atbilde An = {inp_sakuma_vertiba} + (n - {inp_konstants}) * {inp_solis}')
    print(f'\nAprēķini {ntais_loceklis}. locekļa vērtību!')
    inp_nta_vertiba = input('Ievadiet vērtību: ')

    if inp_sakuma_vertiba == str(sakuma_vertiba):
        punkti += 1
    if inp_konstants == str(konstants):
        punkti += 1
    if inp_solis == str(solis):
        punkti += 1
    if inp_nta_vertiba == str(nta_vertiba):
        punkti += 1
    return punkti, punkti_max


def arit_prog2() -> tuple:
    punkti_max = 3
    punkti = 0
    print(f'Jūs varat iegūt {punkti_max} punktus par šo uzdevumu.\n')

    reizes_lielaks = randint(2, 5)
    a_reiz_3 = randint(1, 10)
    a_reiz_1 = a_reiz_3 * reizes_lielaks
    a_reiz_2 = (a_reiz_1 + a_reiz_3) / 2

    print(f'Trīs skaitļi veido aritmētisko progresiju. Vidējais skaitlis ir {a_reiz_2},')
    print(f'bet pirmais skaitlis ir {reizes_lielaks} reizes lielāks par trešo skaitli.')
    print('Aprēķini pirmo un trešo no šiem skaitļiem!')
    inp_a_reiz_1 = input('Ievadiet pirmo progresijas skaitli: ')
    inp_a_reiz_3 = input('Ievadiet trešo progresijas skaitli: ')

    print('\nPapildjautājums')
    print('Kuru no formulām var lietot atbildes iegūšanai?')

    pareizais_atbildes_variants = '1'
    print('1] An = (An-1 + An+1) / 2')
    print('2] Sn = (A1 + An)n')
    print('3] An = An-1 * An+1')
    print('4] An = A1 - (n + 1)d')
    print()

    atbildes_varianti = [str(x + 1) for x in range(4)]
    inp_atbilde = option_choice('Ievadiet atbildes variantu: ', atbildes_varianti)

    if inp_a_reiz_1 == str(a_reiz_1):
        punkti += 1
    if inp_a_reiz_3 == str(a_reiz_3):
        punkti += 1
    if inp_atbilde == pareizais_atbildes_variants:
        punkti += 1
    return punkti, punkti_max


def arit_prog3() -> tuple:
    punkti_max = 3
    punkti = 0
    print(f'Jūs varat iegūt {punkti_max} punktus par šo uzdevumu.\n')

    intervala_beigas = 1 + randint(100, 500)
    dalamais = randint(2, 10)
    reizes_dalas = intervala_beigas // dalamais
    beigas_dalas = dalamais * reizes_dalas
    dalamo_summa = int(((dalamais + beigas_dalas) * reizes_dalas) / 2)
    
    print(f'Aplūkojam visus naturālos skaitļus, kas dalās ar {dalamais}.')
    print(f'Cik skaitļa {dalamais} dalāmie atrodas intervālā no 1 līdz {intervala_beigas}?')
    print(f'Šajā intervālā ir ... skaitļa {dalamais} dalāmie.')
    inp_reizes_dalas = input('Ievadiet atbildi: ')
    print()

    print('Aprēķini šo dalāmo summu!')
    inp_dalamo_summa = input('Summa ir: ')

    if inp_reizes_dalas == str(reizes_dalas):
        punkti += 1
    if inp_dalamo_summa == str(dalamo_summa):
        punkti += 2
    return punkti, punkti_max


uzdevumi = [[arit_prog1, arit_prog2, arit_prog3]]
parbaudes_darbi = [[arit_prog1, arit_prog1, arit_prog2, arit_prog2, arit_prog3]]


def pildit_uzdevumus(temas_indekss: int) -> None:
    temas_nosaukums = temas[temas_indekss]
    print('Uzdevumi tēmai:', temas_nosaukums)
    if temas_nosaukums == "Aritmētiskā progresija":
        uzdevumu_skaits = len(uzdevumi[temas_indekss])
        for uzdevuma_indekss, uzdevums in enumerate(uzdevumi[temas_indekss]):
            print(f'\nUzdevums Nr. {uzdevuma_indekss + 1} / {uzdevumu_skaits}')
            punkti, punkti_max = uzdevums()
            system('cls')
            print('Uzdevumi tēmai:', temas_nosaukums)
            print(f'Jūs ieguvāt {punkti} / {punkti_max} punktus par {uzdevuma_indekss + 1}. uzdevumu!')
    else:
        print(f'\nUzdevumi tēmai {temas_nosaukums} nav izveidoti!')
    print()
    input('Uzspiediet ENTER, lai turpinātu...')


def pildit_parbaudes_darbu(temas_indekss: int) -> None:
    system('cls')
    temas_nosaukums = temas[temas_indekss]
    print('Pārbaudes darbs tēmai:', temas_nosaukums)
    if temas_nosaukums == 'Aritmētiskā progresija':
        uzdevumu_skaits = len(parbaudes_darbi[temas_indekss])
        punkti = 0
        punkti_max = 0
        for parbaudes_darba_indekss in range(uzdevumu_skaits):
            print(f'\nUzdevums Nr. {parbaudes_darba_indekss + 1} / {uzdevumu_skaits}')
            uzdevums = parbaudes_darbi[temas_indekss][parbaudes_darba_indekss]
            darba_punkti, darba_punkti_max = uzdevums()
            system('cls')
            print('Pārbaudes darbs tēmai:', temas_nosaukums)
            punkti += darba_punkti
            punkti_max += darba_punkti_max
        print()
        balles = round(punkti / punkti_max * 10)
        if balles < 1:
            balles = 1
        print(f'Jūsu vērtējums ballēs ir {balles}')
        print(f'Iegūtais punktu skaits {punkti} / {punkti_max}')
    else:
        print(f'\nPārbaudes darbi tēmai {temas_nosaukums} nav izveidoti!')
    print()
    input('Uzspiediet ENTER, lai turpinātu...')


print('Notiek teorijas ielāde...')
for tema in temas:
    filepath = teoriju_faili.format(tema)
    pievienot_teoriju = None
    if not path.exists(filepath):
        pievienot_teoriju = noklusejuma_temas_teorija.format(tema)
        f = open(filepath, 'w', encoding='utf-8')
        f.write(pievienot_teoriju)
        f.close()
    else:
        f = open(filepath, 'rt', encoding='utf-8')
        pievienot_teoriju = f.read()
        f.close()
    teorija.append(pievienot_teoriju)

while True:
    system('cls')
    print(sistemas_nosaukums)
    for x in range(len(temas)):
        print(f'{x + 1}] {temas[x]}')
    print(f'{len(temas) + 1}] Beigt Darbu')
    print()

    option = int(option_choice('Izvēlieties tēmu: ', temas_izveles))
    if option == len(temas) + 1:  # Iziet no izvēles
        break

    temas_indekss = option - 1
    while True:
        system('cls')
        print('Izvēlētā tēma:', temas[temas_indekss])
        print('1] Teoriju')
        print('2] Uzdevumi')
        print('3] Pārbaudes Darbs')
        print('4] Atpakaļ')
        print()

        suboption = int(option_choice('Izvēlieties darbību: ', [str(x + 1) for x in range(4)]))

        system('cls')
        if suboption == 1:  # Teorijas apskatīšana
            apskatit_teoriju(temas_indekss)
        elif suboption == 2:  # Uzdevumu pildīšana
            pildit_uzdevumus(temas_indekss)
        elif suboption == 3:  # Pārbaudes darba pildīšana
            pildit_parbaudes_darbu(temas_indekss)
        elif suboption == 4:  # Iziet no izvēles
            break
