def vytvorit_vydaj(nazev: str, castka: float) -> str:
    """Vytvoří formátovaný řádek pro uložení výdaje"""
    # F string je moderní způsob jak spojovat text
    return f"{nazev};{castka}\n"

def spocitat_celkem(seznam_castek: list[float]) -> float:
    """Spočítá součet všech částek v seznamu"""
    suma = sum(seznam_castek)
    return suma

