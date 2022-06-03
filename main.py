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

temu_fails = 'tēmas.txt'
teoriju_faili = 'teorija/{}.txt'


def dabut_vai_uztaisit_failu(filepath: str, default_text: str = 'Noklusējuma get_file teksts\n') -> str:
    if not path.exists(filepath):
        f = open(filepath, 'w', encoding='utf-8')
        f.write(default_text)
        f.close()
        return default_text
    f = open(filepath, 'rt', encoding='utf-8')
    text = f.read()
    f.close()
    return text


temas = dabut_vai_uztaisit_failu(temu_fails).splitlines()
temas_izveles = temas + ['Beigt Darbu']
teorija = []


def izveles_iespejas_numuretas(prompt: str, options: list) -> str:
    opcijas_izveles_iespejas = []
    for opcijas_indekss, opcija in enumerate(options):
        print(f'{opcijas_indekss + 1}] {opcija}')
        opcijas_izveles_iespejas.append(str(opcijas_indekss + 1))
    print()

    while True:
        ievade = input(prompt)
        if ievade in opcijas_izveles_iespejas:
            return ievade
        print('Nederīga ievade!')


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
    solis = randint(2, 10)
    ntais_loceklis = randint(10, 30)
    nta_vertiba = sakuma_vertiba + (ntais_loceklis - 1) * solis
    print('Dota virkne ', end='')
    for n in range(1, 6):
        an = sakuma_vertiba + (n - 1) * solis
        print(an, end='; ')
    print('... ir aritmētiskā progresija.')
    print('Uzraksti vispārīgā locekļa formulu!')
    print('An = A1 + (n - 1) * d')
    print()

    inp_sakuma_vertiba = input(f'(Ievadiet sākuma vērtību A1)\tAn = ')
    inp_solis = input(f'(Ievadiet differenci d)\t\tAn = {inp_sakuma_vertiba} + (n - 1) * ')
    print(f'Jūsu atbilde ir An = {inp_sakuma_vertiba} + (n - 1) * {inp_solis}')
    print(f'\nAprēķini {ntais_loceklis}. locekļa vērtību!')
    inp_nta_vertiba = input('Ievadiet vērtību: ')

    if inp_sakuma_vertiba == str(sakuma_vertiba):
        punkti += 1
    if inp_solis == str(solis):
        punkti += 2
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
    if a_reiz_2.is_integer():
        a_reiz_2 = int(a_reiz_2)

    print(f'Trīs skaitļi veido aritmētisko progresiju. Vidējais skaitlis ir {a_reiz_2},')
    print(f'bet pirmais skaitlis ir {reizes_lielaks} reizes lielāks par trešo skaitli.')
    print('Aprēķini pirmo un trešo no šiem skaitļiem!')
    print(f'A1 {a_reiz_2} A3')
    print()

    inp_a_reiz_1 = input(f'(Ievadiet pirmo progresijas skaitli) ')
    inp_a_reiz_3 = input(f'(Ievadiet trešo progresijas skaitli) {inp_a_reiz_1} {a_reiz_2} ')
    print(f'Jūsu atbilde ir {inp_a_reiz_1} {a_reiz_2} {inp_a_reiz_3}')

    print('\nPapildjautājums')
    print('Kuru no formulām var lietot atbildes iegūšanai?')

    pareizais_atbildes_variants = '1'
    atbildes_varianti = ['An = (An-1 + An+1) / 2',
                         'Sn = (A1 + An)n',
                         'An = An-1 * An+1',
                         'An = A1 - (n + 1)d']
    inp_atbilde = izveles_iespejas_numuretas('Ievadiet atbildes variantu: ', atbildes_varianti)

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
        punkti = 0
        punkti_max = 0
        for uzdevuma_indekss, uzdevums in enumerate(uzdevumi[temas_indekss]):
            print(f'\nUzdevums Nr. {uzdevuma_indekss + 1} / {uzdevumu_skaits}')
            punkti, punkti_max = uzdevums()
            system('cls')
            print('Uzdevumi tēmai:', temas_nosaukums)
            print(f'Jūs ieguvāt {punkti} / {punkti_max} punktus par {uzdevuma_indekss + 1}. uzdevumu!')
        print(f'Iegūtais punktu skaits par visiem uzdevumiem {punkti} / {punkti_max}')
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
    pievienot_teoriju = dabut_vai_uztaisit_failu(teoriju_faili.format(tema), noklusejuma_temas_teorija.format(tema))
    teorija.append(pievienot_teoriju)

while True:
    system('cls')
    print(sistemas_nosaukums)
    izvele = int(izveles_iespejas_numuretas('Izvēlieties tēmu: ', temas_izveles))

    if izvele == len(temas) + 1:  # Iziet no izvēles
        break

    temas_indekss = izvele - 1
    while True:
        system('cls')
        print('Izvēlētā tēma:', temas[temas_indekss])
        darbibu_izveles = ['Teorija', 'Uzdevumi', 'Pārbaudes Darbs', 'Atpakaļ']
        suboption = int(izveles_iespejas_numuretas('Izvēlieties darbību: ', darbibu_izveles))

        system('cls')
        if suboption == 1:  # Teorijas apskatīšana
            apskatit_teoriju(temas_indekss)
        elif suboption == 2:  # Uzdevumu pildīšana
            pildit_uzdevumus(temas_indekss)
        elif suboption == 3:  # Pārbaudes darba pildīšana
            pildit_parbaudes_darbu(temas_indekss)
        elif suboption == 4:  # Iziet no izvēles
            break
