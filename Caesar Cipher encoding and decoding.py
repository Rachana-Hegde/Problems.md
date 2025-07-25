def caesar_cipher(message, shift, mode='encode'):
    if mode == 'decode':
        shift = -shift
    result = ''
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g. 3): "))
    mode = input("Mode (encode/decode): ").strip().lower()
    result = caesar_cipher(message, shift, mode)
    print(f"\nResult: {result}")
