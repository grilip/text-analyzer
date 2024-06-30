"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Filip Gray
email: gray.filip@proton.me
discord: filipgray
"""

uzivatele = {
    "bob": "123", 
    "ann": "pass123",
    "mike": "password123",
    "liz": "pas123"
    }

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

#Vložení jména a hesla
jmeno = input("username:")
heslo = input("password:")
print("-" *40)

if jmeno in uzivatele and heslo == uzivatele[jmeno]:        #Ověření registrovaných uživatelů
    print("Welcome to the app,", jmeno)
    print("We have 3 texts to be analyzed.", "-" *40, sep = "\n")
    texty = input("Enter a number btw. 1 and 3 to select: ") #Volba čísla textu
    print("-" * 40)
    if texty.isalpha():     #Pokud bude zadáno písmeno, tak se program ukončí
        print("You must enter a number, terminating the program..")
    elif int(texty) == 1 or int(texty) == 2 or int(texty) == 3:       #Zjištění počtu slov
        print("There are", len(TEXTS[int(texty)-1].replace("\n", " ").split()), "words in the selected")
        X = 0       #Zjištění počtu slov začínajících velkým písmenem
        for slovo in TEXTS[int(texty)-1].replace("\n", " ").split():
            if slovo[0].isupper():
                X += 1
        print("There are", X, "titlecase words.")
        Y = 0       #Zjištění počtu slov psaných velkými písmeny
        for slovo2 in TEXTS[int(texty)-1].split():
            if slovo2.isalpha() and slovo2.isupper():
                Y += 1
                print("There are", Y, "uppercase words.")
        Z = 0       #Zjištění počtu slov psaných malými písmeny
        for slovo3 in TEXTS[int(texty)-1].replace(".", " ").split():
            if slovo3.isalpha() and slovo3.islower():
                Z += 1
        print("There are", Z, "lowercase words.")
        list_cisel = list()     #Zjištění počet čísel (ne cifer)
        for slovo4 in TEXTS[int(texty)-1].split():
            if slovo4.isdigit():
                list_cisel.append(int(slovo4))
        print("There are", len(list_cisel), "numeric strings.")
        print("The sum of all the numbers", sum(list_cisel))    
        cetnost_delek_slov = {}
        for delka_slova in TEXTS[int(texty)-1].split():
            x = delka_slova.strip(",.")
            if len(x) not in cetnost_delek_slov:
                cetnost_delek_slov[len(x)] = 1
            else:
                cetnost_delek_slov[len(x)] = cetnost_delek_slov[len(x)] + 1
        print("-" *40, 
            "LEN|  OCCURENCES  |NR.",
            "-" *40, sep = "\n")
        for key, value in sorted(cetnost_delek_slov.items()):
            print("{:>3}|".format(key), "{:<12}".format("*"*value), "|{:<}".format(value))
    else:       #Pokud bude zadáno špatné číslo, program se ukončí
        print("Wrong number, terminating the program..")
else:
    print("Unregistered user, terminating the program..")