def indian_currency_format(number):
    s = f"{number:.4f}"
    if '.' in s:
        int_part, dec_part = s.split('.')
    else:
        int_part, dec_part = s, ""

    n = len(int_part)
    if n <= 3:
        return int_part + '.' + dec_part

    result = int_part[-3:]
    int_part = int_part[:-3]

    while len(int_part) > 0:
        result = int_part[-2:] + ',' + result
        int_part = int_part[:-2]

    return result + '.' + dec_part

if __name__ == "__main__":
    try:
        num = float(input("Enter a number (e.g. 123456.7891): "))
        print("Formatted:", indian_currency_format(num))
    except ValueError:
        print("Invalid input! Please enter a valid number like 123456.7891")
