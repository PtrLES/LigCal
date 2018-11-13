def volume(length, enter_concetration, result_moles):
    return length*0.66*result_moles/enter_concetration


def load():
    lvector = float(raw_input("Podaj wielkosc wektora w bp:   "))
    cvector = float(raw_input("Podaj stezenie wektora w ng/ul:    "))
    linsert = float(raw_input("Podaj wielkosc wstawki w bp:   "))
    cinsert = float(raw_input("Podaj stezenie wstawki w ng/ul:    "))
    return lvector, cvector, linsert, cinsert


def recipe(tabele):
    vvector = round(volume(tabele[0], tabele[1], 0.02), 2)
    vinsert = round(volume(tabele[2], tabele[3], 0.06), 2)
    h2o = round(float(17.-vvector-vinsert), 2)
    print("\n\n")
    print "Przepis na udana ligacje to:"
    print "Woda----%.2f ul" % h2o
    print "Bufor do ligacji----2 ul"
    print "Wstawka----%.2f ul" % vinsert
    print "Wektor----%.2f ul" % vvector
    print "Ligaza----1 ul"


def welcome():
    print"\n\n\nProgram ligcalcualtor zwraca sklad mieszaniny ligacyjnej\
     \nz 0.06 pmol wstawki i 0.02 pmol wektora. Koncowa objetos mieszaniny to 20 ul\n"


def maine():
    welcome()
    recipe(load())

if __name__ == "__main__":
    maine()