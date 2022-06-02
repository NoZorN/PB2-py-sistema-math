"""
Repositorija `https://github.com/pikcrvt-students/PB2-py-sistema-math`

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
temas = ['Aritmētiskā progresija', 'Tēma2']
temas_izveles = [str(x + 1) for x in range(len(temas) + 1)]
teorija = []


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


def arit_prog1():
    punkti_max = 4
    punkti = 0
    print(f'Jūs varat iegūt {punkti_max} punktus par šo uzdevumu.\n')

    a = randint(0, 20)
    b = 1
    c = randint(2, 10)
    n_loceklis = randint(10, 30)
    vert = a + (n_loceklis - b) * c
    print('Dota virkne ', end='')
    for n in range(1, 6):
        an = a + (n - b) * c
        print(an, end='; ')
    print('... ir aritmētiskā progresija.')
    print('Uzraksti vispārīgā locekļa formulu!')
    print('An = a + (n - b) * c')
    inp_a = input('Ievadiet koeficientu a: ')
    inp_b = input('Ievadiet koeficientu b: ')
    inp_c = input('Ievadiet koeficientu c: ')
    print(f'Jūsu atbilde An = {inp_a} + (n - {inp_b}) * {inp_c}')
    print(f'\nAprēķini {n_loceklis}. locekļa vērtību!')
    inp_vert = input('Ievadiet vērtību: ')

    if inp_a == str(a):
        punkti += 1
    if inp_b == str(b):
        punkti += 1
    if inp_c == str(c):
        punkti += 1
    if inp_vert == str(vert):
        punkti += 1
    return punkti, punkti_max


def arit_prog2():
    punkti_max = 3
    punkti = 0
    print(f'Jūs varat iegūt {punkti_max} punktus par šo uzdevumu.\n')

    reizes = randint(2, 5)
    a3 = randint(1, 10)
    a = a3 * reizes
    vid = (a + a3) / 2

    print(f'Trīs skaitļi veido aritmētisko progresiju. Vidējais skaitlis ir {vid},')
    print(f'bet pirmais skaitlis ir {reizes} reizes lielāks par trešo skaitli.')
    print('Aprēķini pirmo un trešo no šiem skaitļiem!')
    inp_a = input('Ievadiet pirmo skaitli: ')
    inp_a3 = input('Ievadiet trešo skaitli: ')

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

    if inp_a == str(a):
        punkti += 1
    if inp_a3 == str(a3):
        punkti += 1
    if inp_atbilde == pareizais_atbildes_variants:
        punkti += 1
    return punkti, punkti_max


def arit_prog3():
    punkti_max = 3
    punkti = 0
    print(f'Jūs varat iegūt {punkti_max} punktus par šo uzdevumu.\n')

    beigas = 1 + randint(100, 500)
    dalamais = randint(2, 10)
    reiz = beigas // dalamais
    beigas_dalas = dalamais * reiz
    summ = int(((dalamais + beigas_dalas) * reiz) / 2)
    
    print(f'Aplūkojam visus naturālos skaitļus, kas dalās ar {dalamais}.')
    print(f'Cik skaitļa {dalamais} dalāmie atrodas intervālā no 1 līdz {beigas}?')
    print(f'Šajā intervālā ir ... skaitļa {dalamais} dalāmie.')
    inp_reiz = input('Ievadiet atbildi: ')
    print()

    print('Aprēķini šo dalāmo summu!')
    inp_sum = input('Summa ir: ')

    if inp_reiz == str(reiz):
        punkti += 1
    if inp_sum == str(summ):
        punkti += 2
    return punkti, punkti_max


uzdevumi = [[arit_prog1, arit_prog2, arit_prog3]]
parbaudes_darbi = [[arit_prog1, arit_prog1, arit_prog2, arit_prog2, arit_prog3]]


def pildit_uzdevumus(temas_indekss):
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


def pildit_parbaudes_darbu(temas_indekss):
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
    filepath = f'teorija/{tema}.txt'
    pievienot_teoriju = None
    if not path.exists(filepath):
        pievienot_teoriju = f'Tēmas {tema} teorija...'
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
    print('Matemātikas sistēma')
    for x in range(len(temas)):
        print(f'{x + 1}] {temas[x]}')
    print(f'{len(temas) + 1}] Iziet')
    print()

    option = int(option_choice('Izvēlieties tēmu: ', temas_izveles))
    if option == len(temas) + 1:  # Iziet no izvēles
        break

    temas_indekss = option - 1
    while True:
        system('cls')
        print('Izvēlētā tēma:', temas[temas_indekss])
        print('1] Apskatīt teoriju')
        print('2] Pildīt uzdevumus')
        print('3] Pildīt pārbaudes darbu')
        print('4] Iziet')
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
