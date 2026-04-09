def Add(numbers):
    if not numbers:
        return 0
    
    numbers = numbers.replace("\n", ",")

    if ",," in numbers:
        raise ValueError("Invalid input: Consecutive commas detected.")

    parts = numbers.split(",")
    total = 0

    for part in parts:
        clean_part = part.strip()
        if not clean_part:
            raise ValueError("Invalid input: Trailing comma detected.")
        
        try:
            total += int(clean_part)
        except ValueError:
            raise ValueError(f"Nieprawidlowa wartosc: {clean_part}")


    return total
    
    
