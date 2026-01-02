#Src uloziste.py

def pridat_radek(cesta: str, radek: str) -> None:
    """Otevře soubor a připíše řádek na jeho konec. Pokud soubor neexistuje, automaticky ho vytvoří."""
    #mode="a" znamená APPEND (připojit se nakonec)
    # kdybychom dali mode="w" automaticky by se vždy soubor smazal a přepsal!
    with open(cesta, mode="a", encoding="utf-8") as soubor:
        soubor.write(radek)

def nacist_vydaje(cesta: str) -> list[str]:
    """Načte všechny řádky ze souboru a vrátí je jako seznam. Pokud soubor neexistuje, vrátí seznam prázdný a nevyhodí chybu."""
    try:
        with open(cesta, mode="r", encoding="utf-8") as soubor:
            #readlines() načte soubor řádek po řádku do seznamu
            return soubor.readlines()
    except FileNotFoundError:
        return []