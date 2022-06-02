# Matemātikas sistēma

---
## Uzdevuma formulējums
Sistēma ar kuras palīdzību ir iespējams:
 - Izvēlēties vienu no dažādām tēmām
 - Lasīt teoriju par šīm tēmām
 - Pildīt uzdevumus par šīm tēmām
 - Pildīt kontroldarbus par šīm tēmām (vērtējums ballēs)
---
## Ievades/izvades dati
Ievadē ietilpst:
 - Visas izvēles
 - Uzdevumu atbildes
 - Citas ievades opcijas (vārds, uzvārds, utt.)

Izvadē ietilpst:
 - Instrukcijas lietotājam
 - Informācija par tēmu (teorija)
 - Informācija par uzdevumiem
 - Rezultāti pēc uzdevumu un kontroldarbu pildīšanas
---
## Datu apstrāde
### Tēma: Aritmētiskā progresija
1. Uzdevums tiek automātiski ģenerēts ar nejaušām vērtībām.
Audzēknis aprēķina aritmētiskās progresijas sākuma vērtību un
soli, konstantu jāzina no teorijas.
```python
sakuma_vertiba = randint(0, 20)
konstants = 1
solis = randint(2, 10)
ntais_loceklis = randint(10, 30)
nta_vertiba = sakuma_vertiba + (n_loceklis - konstants) * solis
```
2. Uzdevums tiek automātiski ģenerēts ar nejaušām vērtībām.
Audzēknis aprēķina pirmo un trešo aritmētiskās progresijas
locekli, ja ir dots otrais un cik reizes pirmais ir lielāks
par trešo locekli.
```python
reizes_lielaks = randint(2, 5)
a_reiz_3 = randint(1, 10)
a_reiz_1 = a_reiz_3 * reizes_lielaks
a_reiz_2 = (a_reiz_1 + a_reiz_3) / 2
...
pareizais_atbildes_variants = '1'
```
3. Uzdevums tiek automātiski ģenerēts ar nejaušām vērtībām.
Audzēknis aprēķina cik reizes skaitļi intervālā dalās ar
doto dalāmo skaitli un jāaprēķina šo dalāmo summu.
```python
intervala_beigas = 1 + randint(100, 500)
dalamais = randint(2, 10)
reizes_dalas = intervala_beigas // dalamais
beigas_dalas = dalamais * reizes_dalas
dalamo_summa = int(((dalamais + beigas_dalas) * reizes_dalas) / 2)
```
---
## Lietotāja instrukcija
### Skolotājai
Ir iespēja pievienot jaunas tēmas `Tēmas.txt` failā, taču uzdevumus
var izveidot tikai programmētājs, jo tie ir nejauši ģenerēti
uzdevumi. Lai tēmām ievietotu vai nomainītu teoriju ir jāiet mapē
`teorija` un jāizveido jeb jāatver tēmas fails, piemēram:
`Aritmētiskā progresija.txt`.
### Audzēkņiem
Jāatver programma `main.py` un jāizvēlas attiecīgā sadaļa,
kur audzēknis vēlas doties, piemēram: `Teorija`, `Uzdevumi`,
`Pārbaudes Darbs`. Jāseko programmas dotajām instrukcijām,
lai to izmantotu.

---
## Testēšana
Testēšana...

---
## Nobeigums
Aukšupielādēt sistēmu platformā GitHub:
`https://github.com/pikcrvt-students/PB2-py-sistema-math`