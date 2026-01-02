# Importutejeme naši funkci ze složky src
from src.vypocty import vytvorit_vydaj
from src.uloziste import pridat_radek, nacist_vydaje

#Definujeme konstantu ať ji nemáme natvrdo v kódu
CESTA_K_DATUM = "data/vydaje.txt"

def main():
    print("___MANAŽÉR VÝDAJŮ___")

    print ("\n[Historie výdajů]")
    seznam_vydaju = nacist_vydaje(CESTA_K_DATUM)
    if not seznam_vydaju:
        print("Zatím nejsou k dispozici žádné výdaje")
    else:
        for radek in seznam_vydaju:
            # .strip odstranní neviditelný enter na konci řádků, aby se nám nedělaly prázdné řádky mezi výpisy
            print(f" - {radek.strip()}")
    print ("-"*20) # --> Oddělovací čára

    #Získání dat od uživatele (input vrací vždy text, proto převod na float)
    zbozi = input("Zadejte název výdaje (např. oběd): ")
    cena_text = input("Zadejte částku (např. 150) ")

    # Jednoduchá ochrana v kódu kdyby uživatel nezedal číslo
    try:
        cena = float(cena_text)
    except ValueError:
        print("Chyba, částka musí být číslo!")
        return

    # Použití naší funkce
    radek_pro_ulozeni = vytvorit_vydaj(zbozi, cena)

    print(f"Ukládám do souboru: {CESTA_K_DATUM} ...")

    pridat_radek(CESTA_K_DATUM, radek_pro_ulozeni)

    print("✅ Uloženo!")

#Vstupní bod programu:
if __name__ == "__main__":
    main()