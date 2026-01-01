# Importutejeme naši funkci ze složky src
from src.vypocty import vytvorit_vydaj

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

    print(f"Připraveno k uložení: {radek_pro_ulozeni.strip()}")

#Vstupní bod programu:
if __name__ == "__main__":
    main()