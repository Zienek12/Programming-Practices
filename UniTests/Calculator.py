import re

def Add(numbers):
    # Punkt 1: Pusty ciag zwraca 0
    if not numbers:
        return 0
    
    # Punkt 5: Sprawdzenie blednego formatu "1,\n"
    # Szukamy wystapienia przecinka obok nowej linii
    if ",\n" in numbers or "\n," in numbers:
        raise ValueError("Nieprawidlowy format danych: przecinek i nowa linia obok siebie")

    # Punkt 5: Obsluga wielu separatorow (przecinek lub nowa linia)
    # Uzywamy wyrazenia regularnego do podzialu ciagu
    # split('[,\n]') dzieli ciag wszędzie tam, gdzie znajdzie , lub \n
    parts = re.split(r'[,\n]', numbers)
    
    # Punkt 4 i 6: Implementacja z uwzglednieniem zwracania bledu
    result = 0
    for part in parts:
        try:
            # Punkt 3: Rozszerzenie o mozliwosc przyjmowania wielu liczb
            result += int(part)
        except ValueError:
            # Punkt 4: Zwracanie bledu w przypadku nieprawidlowych wartosci
            raise ValueError(f"Nieprawidlowa wartosc: {part}")
            
    return result