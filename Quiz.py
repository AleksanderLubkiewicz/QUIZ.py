"""
Spis treści:

    1) Listy zawierające hasła i odpowiedzi do pytań.   [34-166]
        1.1)Stolice                                     [38]
        1.2)Rok                                         [79]
        1.3)Imiona                                      [95]
        1.4)Pierwiastki                                 [109]
        1.5)Prawda czy fałsz                            [126]
        1.6)Przydomek/Pseudonim                         [144]
        1.7) Łączna lista.                              [159]
    2)  Kod programu                                    [168-402]
        2.1) Import potrzebnych funkcji                 [169]
        2.2) Okno startowe                              [181]
        2.3) Okno pytań                                 [223]
        2.4) Okno wyników                               [335]

Contents:

    1) Lists containing entries and answers to questions.   [34-166]
        1.1)Capitals                                        [38]
        1.2) Year                                           [79]
        1.3) Names                                          [95]
        1.4) Elements                                       [109]
        1.5)True or false                                   [126]
        1.6) Nickname/Nickname                              [144]
        1.7) Total List.                                    [159]
    2) Program code                                         [168-402]
        2.1) Import of necessary functions                  [169]
        2.2) Startup window                                 [181]
        2.3) Question window                                [223]
        2.4) Results window                                 [335]
"""
#..............................................................................................................
# 1)Listy zawierające hasła i odpowiedzi do pytań.
# 1) Lists containing entries and answers to questions.

# 1.1) STOLICE
# Hasło - kraj, odpowiedź - stolica
# 1.1)Capitals
# Password - country, answer - capital

st = [["Albania", "Tirana"], ["Andora", "Andora"], ["Austria", "Wiedeń"], ["Belgia", "Bruksela"], ["Białoruś", "Mińsk"],
      ["Bośnia i Hercegowina", "Sarajewo"], ["Bułgaria", "Sofia"], ["Chorwacja", "Zagrzeb"], ["Czechy", "Praga"],
      ["Dania", "Kopenhaga"], ["Estonia", "Talin"], ["Finlandia", "Helsinki"], ["Francja", "Paryż"], ["Grecja", "Ateny"],
      ["Hiszpania", "Madryt"], ["Holandia", "Amsterdam"], ["Irlandia", "Dublin"], ["Islandia", "Rejkiawik"],
      ["Liechtenstein", "Vaduz"], ["Litwa", "Wilno"], ["Luksemburg", "Luksemburg"], ["Łotwa", "Ryga"],
      ["Macedonia", "Skopje"], ["Malta", "La Valetta"], ["Mołdawia", "Kiszyniów"], ["Monako", "Monako"],
      ["Niemcy", "Berlin"], ["Norwegia", "Oslo"], ["Polska", "Warszawa"], ["Portugalia", "Lizbona"], ["Rosja", "Moskwa"],
      ["Rumunia", "Bukareszt"], ["San Marino", "San Marino"], ["Serbia", "Belgrad"], ["Słowacja", "Bratysława"],
      ["Słowenia", "Lublana"], ["Szwajcaria", "Berno"], ["Szwecja", "Sztokholm"], ["Turcja", "Ankara"],
      ["Ukraina", "Kijów"], ["Walia", "Cardiff"], ["Watykan", "Watykan"], ["Węgry", "Budapeszt"], ["Anglia", "Londyn"],
      ["Włochy", "Rzym"],["ALŻERIA", "ALGIERS"], ["ANGOLA", "LUANDA"], ["BENIN", "PORTO-NOVO"], ["BWANŻUŁA", "GWINEA-BISSAU"],
    ["BURKINA FASO", "OUAGADOUGOU"], ["BURUNDI", "GITEGA"], ["REPUBLIKA ŚRODKOWOAFRYKAŃSKA", "BANGUI"], ["CZAD", "NDŻAMENA"],
    ["KOMORY", "MORONI"], ["KONGO", "BRAZZAVILLE"],["DEMOKRATYCZNA REPUBLIKA KONGA", "KINSZASA"], ["DŻIBUTI", "DŻIBUTI"],
    ["EGIPT", "KAIRO"], ["GABON", "LIBREVILLE"], ["GAMBIA", "BANJUL"],["GHANA", "ACCRA"], ["GWINEA", "CONAKRY"],
    ["GWINEA RÓWNIKOWA", "MALABO"], ["KENIA", "NAIROBI"], ["LESOTHO", "MASERU"], ["LIBAN", "TRIPOLI"],
    ["LIBERIA", "MONROVIA"], ["LIBIA", "TRYPOLIS"], ["MADAGASKAR", "ANTANANARYWA"], ["MALAWI", "LILONGWE"],
    ["MALI", "BAMAKO"], ["MAURETANIA", "NOUAKCHOTT"], ["MAURITIUS", "PORT LOUIS"], ["MAROKO", "RABAT"],
    ["MOZAMBIK", "MAPUTO"], ["NAMIBIA", "WINDHUK"], ["NIGER", "NIAMEY"], ["NIGERIA", "ABUJA"], ["RWANDA", "KIGALI"],
    ["SAHARA WSCHODNIA", "AL-AJUN"], ["WYBRZEŻE KOŚCI SŁONIOWEJ", "YAMOUSSOUKRO"],
    ["WYSPY ŚW. TOMASZA I KSIĄŻĘCA", "SÃO TOMÉ"], ["SENEGAL", "DAKAR"], ["SEYCHELLE", "VICTORIA"],
    ["SIERRA LEONE", "FREETOWN"], ["SOMALIA", "MOGADISZU"], ["SUDEAN", "CHARTUM"], ["SUAZI", "MBABANE"],
    ["TANZANIA", "DODOMA"], ["TOGO", "LOMÉ"], ["TUNEZJA", "TUNEZJA"], ["UGANDA", "KAMPALA"],
    ["ZACHODNIA SAHARA", "EL-AJUN"], ["ZAMBIA", "LUSAKA"], ["ZIMBABWE", "HARARE"]]

# Pętlna przerabiająca pisownię na duże litery.
# A loop that converts spelling to capital letters.
stolice = []

for x in st:
    y = x[0].upper()
    z = x[1].upper()
    stolice.append([y,z])



# ....................................................................................................
# 1.2)ROK
# Hasło - wydarzenie, - odpowiedź - rok w którym miało miejsce.
#1.2)YEAR
# Password - event, - answer - year in which it took place.

rok = [["CHRZEST POLSKI", "966"], ["ZJAZD GNIEŹNIEŃSKI", "1000"], ["PODZIAŁ POSLKI NA DZIELNICE", "1138"],
       ["POWSTANIE UNIWERSYTETU JAGIELOŃSKIEGO", "1364"], ["BITWA POD GRUNWALDEM", "1410"],
       ["UNIA LUBELSKA Z LITWĄ", "1569"], ["PIERWSZY ROZBIÓR POLSKI", "1772"], ["ODZYSKANIE NIEPODLEGŁOŚCI POLSKI", "1918"],
       ["BITWA WARSZAWSKA", "1920"], ["OBRADY OKRĄGŁEGO STOŁU", "1989"], ["EDYKT MEDIOLAŃSKI", "313"],
       ["PODZIAŁ CESARSTWA RZYMSKIEGO", "395"], ["UPADEK CESARSTWA ZACHODNIORZYMSKIEGO", "476"], ["WIELKA SCHIZMA", "1045"],
       ["ZDOBYCIE KONSTANTYNOPOLA PRZEZ TURKÓW", "1456"], ["ODKRYCIE AMERYKI PRZEZ KOLUMBA", "1492"],
       ["WYSTĄPIENIE MARCINA LUTRA", "1517"], ["OGŁOSZENIE DEKLARACJI NIEPODLEGŁOŚCI USA", "1776"],
       ["UCHWALENIE KONSTYTUCJI USA", "1785"], ["WYBUCH REWOLUCJI FRANCUSKIEJ", "1789"], ["KORONACJA NAPOLEONA", "1804"],
       ["PIERWSZE NOWOŻYTNE IGRZYSKA", "1896"]]

#......................................................................................................................
# 1.3) IMIONA
# Hasło - nazwisko, odpowiedź - imię.
#1.3) NAMES
# Password - surname, answer - name.

imiona = [["TUWIM", "JULIAN"], ["BRZECHWA", "JAN"], ["EINSTEIN", "ALBERT"], ["TESLA", "NICOLA"], ["LINCOLN", "ABRACHAM"],
        ["WASZYNGTON (POLITYK)", "JERZY"], ["PITT", "BRAD"], ["DEPP", "JOHNNY"], ["KAFKA", "FRANZ"],
          ["SHAKESPEARE", "WILLIAM"], ["DOSTOJEWSKI", "FIODOR"], ["DICKENS", "CHARLES"], ["ORWELL", "GEORGE"],
          ["TWAIEN", "MARK"], ["TOŁSTOJ", "LEW"], ["CONRAD", "JOSEPH"], ["NOBEL", "ALFRED"], ["ŁUKASIEWICZ", "IGNACY"],
          ["GALILEI", "GALILEO"], ["HAWKING", "STEPHEN"], ["KOPERNIK", "MIKOŁAJ"], ["PASTEUR", "LOUIS"],
          ["SZYMBORSKA", "WIESŁAWA"], ["MIŁOSZ", "CZESŁAW"], ["MICKIEWICZ", "ADAM"], ["WOODS", "ELDRICK"],
          ["FEDERER", "ROGER"], ["BOLT", "USAIN"], ["MESSI", "LIONEL"], ["JOLIE", "ANGELINA"]]

#..............................................................................................................
# 1.4) PIERWIASTKI
# Hasło - symbol pierwistka, odpowiedź - jego nazwa
#1.4) ELEMENTS
# Password - symbol of the element, answer - its name

pierwiastki = [["H", "WODÓR"], ["He", "HEL"], ["Li", "LIT"], ["Be", "BERYL"], ["B", "BOR"], ["C", "WĘGIEL"], ["N", "AZOT"],
              ["O", "TLEN"], ["F", "FLUOR"], ["Ne", "NEON"], ["Na", "SÓD"], ["Mg", "MAGBEZ"], ["Al, GLIN"],
              ["Si", "KRZEM"], ["P", "FOSFOR"], ["S", "SIARKA"], ["Cl", "CHLOR"], ["Ar", "ARGON"], ["K", "POTAS"],
              ["Ca", "WAPŃ"], ["Sc", "SKAND"], ["Ti", "TYTAN"], ["V", "WANAD"], ["Cr", "CHROM"], ["Mn", "MANGAN"],
              ["Fe", "ŻELAZO"], ["Co", "KOBALT"], ["Ni", "NIKIEL"], ["Cu", "MIEDŹ"], ["Zn", "CYNK"], ["Ga", "GAL"],
              ["Ge", "GERMAN"], ["As", "ARSEN"], ["Se", "SELEN"], ["Br", "BROM"], ["Kr", "KRYPTON"], ["Rb", "RUBID"],
              ["Sr", "STRONT"], ["Y", "ITR"], ["Zr", "CYRKON"], ["Nb", "NIOB"], ["Mo", "MOLIBDEN"], ["Tc", "TECHNET"],
              ["Ru", "RUTEN"], ["Rh", "ROD"], ["Pd", "PALLAD"], ["Ag", "SREBRO"], ["Cd", "KADM"], ["In", "IND"],
              ["Sn", "CYNA"], ["Sb", "ANTYMON"], ["Te", "TELLUR"], ["I", "JOD"], ["Xe", "KSENON"], ["Cs", "CEZ"],
              ["Ba", "BAR"], ["La", "LANTAN"], ["Ce", "CER"], ["Pr", "PREZEODYM"], ["Nd", "NEODYM"]]

#..............................................................................................................
# 1.5)PRAWDA CZY FAŁSZ
# Hasło - pytanie, - odpowiedź - prawda lub fałsz
#1.5)TRUE OR FALSE
# Password - question, - answer - true or false

pf = [["JOWISZ JEST PIĄTĄ PLANETĄ LICZĄC OD SŁOŃCA", "PRAWDA"], ["ZŁOTO JEST GĘSTSZE OD ŻELAZA", "PRAWDA"],
      ["NEPTUN POSIADA PONAD 20 KSIĘŻYCÓW", "FAŁSZ"], ["W POWIETRZU DŹWIĘK ROZCHODZI SIĘ Z PRĘDKOŚCIĄ PONAD 1200 KM/H",
      "PRAWDA"], ["LANCE ARMSTRONG BYŁ PIERWSZYM CZŁOWIEKIEM NA KSIĘŻYCU", "FAŁSZ"],
      ["NEIL ARMSTRONG BYŁ PIERWSZYM CZŁOWIEKIEM NA KSIĘŻYCU", "PRAWDA"], ["MOSIĄDZ TO STOP MIEDZI I CYNKU", "PRAWDA"],
      ["TEMPERATURA WRZENIA WODY ZALERZY OD CIŚNIENIA ATMOSFERYCZNEGO", "PRAWDA"],
      ["NA ZIEMI JEST PONAD 190 PAŃSTW", "PRAWDA"], ["MOUNT EVEREST MA PONAD 8850 METRÓW WYSOKOŚCI", "FAŁSZ"],
      ["JEDNOSTKA ASTRONAMICZNA TO ŚREDNIA ODLEGŁOŚĆ ZIEMI OD SŁOŃCA", "PRAWDA"],
      ["USA MIAŁO W SWOJEJ HISTORII PONAD PIĘĆDZIESIĘCIU PREZYDENTÓW", "FAŁSZ"],
      ["TRZECH PREZYDENTÓW USA ZGINĘŁO W WYNIKU ZAMACHU", "FAŁSZ"],
      ["SEAN CONNERY SIEDMIOKROTNIE WCIELAŁ SIĘ W BONDA", "PRAWDA"],
      ["TOLKIENOWSKA DRUŻYNA PIERŚCIENIA SKŁADAŁA SIĘ Z DZIEWIĘCIU OSÓB", "PRAWDA"]]

#..................................................................................................................
# 1.6)Przydomek/Pseudonim
# Hasło - imię i nazwisko fikcyjnej postaci. Odpowiedź - przydomek/pseudonim
#1.6) Nickname/Nickname
# Password - name and surname of a fictional character. Answer - nickname/nickname

alias = [["BRUCE WAYNE", "BATMAN"], ["RICHARD GRAYSON (W DZIECIŃSTWIE)", "ROBIN"], ["RICHARD GRAYSON (DOROSŁY)",
        "NIGHTWING"], ["JASON TODD (PRZED ŚMIERCIĄ)", "ROBIN"], ["JASON TODD (PO ZMARTWYCHWSTANIU)", "RED HOOD"],
         ["DAMIAN WAYNE", "ROBIN"], ["BARBARA GORDON (POCZĄTKI KARIERY SUPERBOHATERKI)", "BATGIRL"],
         ["BARBARA GORDON (PO POSTRZALE)", "WYROCZNIA"], ["CLARK KENT", "SUPERMAN"], ["KARA ZOR-EL", "SUPERGIRL"],
         ["DIANA Z THEMISCIRY", "WONDER WOMEN"], ["BARRY ALTEN", "FLASH"], ["HAL JORDAN", "GREEN LANTERN"],
         ["PETER PARKER", "SPIDER MAN"], ["ANTHONY STARK", "IRON MAN"], ["FRANCIS CASTLE", "PUNISHER"],
         ["WADE WILSON", "DEADPOOL"], ["JAMES HOWLETT", "WOLVERINE"], ["ERZA SCARLET", "TYTANIA"], ["SATIMA",
            "ONE PUNCH MAN"]]

#...................................................................................................................
# 1.7)PYTANIA
# Lista łączna do pytań.
#1.7)QUESTIONS
# Total list for questions.

pytania = [stolice, rok, imiona, pierwiastki, pf, alias]


#......................................................................................................
# 2)  Kod programu
# 2.1) Import potrzebnych funkcji
#2) Program code
#2.1) Import needed functions

import tkinter as tk
import random

#..............................................................................................................
# Pętla umożliwiająca wielokrotne zagranie w quiz
# A loop that allows you to play the quiz multiple times

while True:
    # 2.2)Okno startowe
    # Przycisk rozpoczynający grę oraz przycisk wyłączający program.
    # 2.2)Start window
    # A button to start the game and a button to turn off the program.

    okno1 = tk.Tk()
    okno1.title("Quiz")
    okno1.attributes("-fullscreen", True)

    tekst10 = tk.Label(master=okno1,
                       text="Quiz z wiedzy ogólnej.",
                       foreground="orange",
                       background="black",
                       width=50,
                       height=15,
                       anchor=tk.CENTER,
                       font="Arial 20")

    tekst11 = tk.Label(master=okno1,
                       background="black",
                       height=2)

    przyciski = tk.Frame(okno1, background="black")

    przycisk10 = tk.Button(przyciski, text="START", fg="orange", background="black", command=lambda: okno1.destroy())
    przycisk11 = tk.Button(przyciski, text="EXIT", fg="orange", background="black", command=lambda: exit())



    tekst10.pack(fill=tk.BOTH, expand=True)
    czarne1 = tk.Label(przyciski, background="black")
    czarne2 = tk.Label(przyciski, background="black")
    czarne1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    czarne2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    przycisk10.pack(side=tk.LEFT)
    przycisk11.pack(side=tk.RIGHT)
    przyciski.pack(side=tk.TOP, fill=tk.BOTH)
    tekst11.pack(fill=tk.BOTH)

    okno1.mainloop()

# .....................................................................................................
# 2.3) Okno pytań
# Program podaje po jednym pytaniu z każdej kategorii.
# Gracz odpowiada za pomocą Entry.
# Odpowiedzi gracza, odpowiedzi poprawne oraz hasła są zapisywane w listach.
# Przycisk wyłączający program.

# 2.3) Question window
# The program gives one question from each category.
# The player responds with Entry.
# Player answers, correct answers and passwords are saved in lists.
# Button to turn off the program.

    odpowiedziP = []
    odpowiedziG = []
    hasła = []

# Pętla przechodząca po poszczególnych kategoriach pytań.
# Loop through individual question categories.

    for kategoria in pytania:

        okno2 = tk.Tk()
        okno2.title("Quiz")
        okno2.attributes("-fullscreen", True)

        karta = random.choice(kategoria)

        if kategoria == pytania[0]:
            tekst21 = "Podaj stolicę następującego kraju"
        elif kategoria == pytania[1]:
            tekst21 = "W którym roku naszej ery miało miejsce to wydażenie"
        elif kategoria == pytania[2]:
            tekst21 = "Podaj pierwsze imię następujączej postaci"
        elif kategoria == pytania[3]:
            tekst21 = "Jaki to pierwsiatek?"
        elif kategoria == pytania[4]:
            tekst21 = "Prada czy fałsz"
        elif kategoria == pytania[5]:
            tekst21 = "Podaj przydomek / alter-ego następującej fikcyjnej postaci"

        pytanie = karta[0]

        hasła.append(karta[0])
        odpowiedziP.append(karta[1])

        tekst20 = tk.Label(master=okno2,
                           text=tekst21,
                           foreground="orange",
                           background="black",
                           width=50,
                           height=9,
                           anchor=tk.CENTER,
                           font="Arial 20")

        tekst22 = tk.Label(master=okno2,
                           text=pytanie,
                           foreground="white",
                           background="black",
                           width=50,
                           height=1,
                           anchor=tk.CENTER,
                           font="Arial 20")

        tekst23 = tk.Label(master=okno2,
                           background="black",
                           width=50,
                           height=4,
                           anchor=tk.CENTER,
                           font="Arial 20")

        tekst24 = tk.Label(master=okno2,
                           background="black",
                           width=50,
                           height=2,
                           anchor=tk.CENTER,
                           font="Arial 20")

        przyciski2 = tk.Frame(okno2, background="black")
        przycisk20 = tk.Button(przyciski2, text="EXIT", fg="orange", background="black", command=lambda: exit())


        odpC = tk.Frame(okno2, background="black")
        odp = tk.Entry(odpC, width=20, font="Arial 30", background="black", foreground="white")

        def odp2(e):

            odp3 = str(e.widget.get())
            odpowiedziG.append(odp3.upper())
            okno2.destroy()


        odp.bind("<Return>", odp2)
        tekst20.pack(fill=tk.BOTH, expand=True)
        tekst22.pack(fill=tk.BOTH, expand=True)
        odpL = tk.Label(odpC)
        odpP = tk.Label(odpC)
        odpL.pack(side=tk.LEFT, fill=tk.BOTH)
        odp.pack(side=tk.TOP)
        odpL.pack(side=tk.RIGHT)
        odpC.pack(side=tk.TOP, fill=tk.BOTH)
        tekst23.pack(fill=tk.BOTH, expand=True)
        czarne1 = tk.Label(przyciski2, background="black")
        czarne2 = tk.Label(przyciski2, background="black")
        czarne1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        czarne2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        przycisk20.pack(side=tk.TOP, fill=tk.BOTH)
        przyciski2.pack(side=tk.TOP, fill=tk.BOTH)
        tekst24.pack(fill=tk.BOTH)

        okno2.mainloop()

# ...........................................................................................
# 2.4) OKNO WYNIKU
# Program porównuje odpowiedzi gracza z odpowiedziami poprawnymi oraz wyświetla wynik.
# Przycisk wyłączający program oraz przycisk ponownej gry.
# 2.4) RESULT WINDOW
# The program compares the player's answers with the correct answers and displays the result.
# Program shutdown button and replay button.

    okno3 = tk.Tk()
    okno3.title("Quiz")
    okno3.attributes("-fullscreen", True)

    o = 0
    punkty = 0

    while o != len(odpowiedziG):

        if odpowiedziP[o] == odpowiedziG[o]:
            tekst31 = hasła[o] + " / " + odpowiedziP[o]
            kolor3 = "green"
            punkty += 1

        else:
            tekst31 = hasła[o] + " / TWOJA ODPOWIEDŹ TO " + odpowiedziG[o] + " / POPRAWNA ODPOWIEDŹ TO " + odpowiedziP[o]
            kolor3 = "red"

        tekst30 = tk.Label(master=okno3,
                           text=tekst31,
                           foreground=kolor3,
                           background="black",
                           width=50,
                           height=1,
                           anchor=tk.CENTER,
                           font="Arial 15")

        o += 1

        tekst30.pack(fill=tk.BOTH, expand=True)

    tekst33 = "zdobyłeś " + str(punkty) + " na 6 punktów."
    tekst32 = tk.Label(master=okno3,
                       text=tekst33,
                       foreground="orange",
                       background="black",
                       width=50,
                       height=1,
                       anchor=tk.CENTER,
                       font="Arial 15")

    tekst34 = tk.Label(master=okno3,
                       background="black",
                       width=50,
                       height=2,
                       anchor=tk.CENTER,
                       font="Arial 15")
    przyciski3 = tk.Frame(okno3, background="black")
    przycisk30 = tk.Button(przyciski3, text="EXIT", fg="orange", background="black", command=lambda: exit())
    przycisk31 = tk.Button(przyciski3, text="JESZCZE RAZ", fg="orange", background="black", command=lambda: okno3.destroy())

    tekst32.pack(fill=tk.BOTH, expand=True)
    czarne1 = tk.Label(przyciski3, background="black")
    czarne2 = tk.Label(przyciski3, background="black")
    czarne1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    czarne2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    przycisk30.pack(side=tk.LEFT)
    przycisk31.pack(side=tk.RIGHT)
    przyciski3.pack(side=tk.TOP, fill=tk.BOTH)
    tekst34.pack(fill=tk.BOTH)
    okno3.mainloop()








