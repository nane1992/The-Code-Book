def get_file_path():
    while True:
        file_path = input("Enter file path: ")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print("File not found.")
        except UnicodeDecodeError:
            print("Decoding issue, check file encoding.")

def get_shift():
    while True:
        user_input = input("Shift? (1-26) or type exit to quit: ").strip().lower()
        if user_input == "exit":
            exit()
        try:
            shift = int(user_input)
            if 1<= shift <=26:
                return shift
            else:
                print("Enter a value between 1 and 26")
        except ValueError:
            print("Invalid input. Enter a number between 1 and 26.")

def decrypt_caesar_shift(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            char = char.upper()
            decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            # example: shift of -5 for letter C:
            # ord('C') - ord('A') => 67 - 65 = 2
            # (2-5) % 26 = 23 = ord('Z')
            # 
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = get_file_path()

while True:
    shift = get_shift()
    decryption = decrypt_caesar_shift(ciphertext, shift)
    print("\nDecrypted text:")
    print(decryption +"\n")
    
# lösning: ARCANUM EST NEUTRON