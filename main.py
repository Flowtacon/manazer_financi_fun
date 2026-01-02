# Importutejeme naši funkci ze složky src
from src.vypocty import vytvorit_vydaj
from src.uloziste import pridat_radek

#Definujeme konstantu ať ji nemáme natvrdo v kódu
CESTA_K_DATUM = "data/vydaje.txt"

def main():
    print("___MANAŽÉR VÝDAJŮ___")

    #Získání dat od uživatele (input vrací vždy text, proto převod na float)
    zbozi = input("Zadejte název výdaje (např. objed): ")
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