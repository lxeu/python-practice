alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(text, shift, direction):
        # Error check direction
        if direction.lower() not in ["encode", "decode"]:
            print("Enter either 'encode' or 'decode'.")
            return
        # Error check shift
        if not shift.isdigit():
            print("Enter a number")
            return
        shift = int(shift)
        # Make shift subtraction for decode
        if direction.lower() == "decode":
            shift *= -1
        # Result word
        crypted_word = ""
        for i in text:
            # Keep value unchanged if not a letter
            if i not in alphabet:
                 crypted_word += i
            else:
                # Logic for encode/decode
                letter = alphabet.index(i)
                encrypted_letter = alphabet[(letter + shift) % 26]
                crypted_word += encrypted_letter
        print(f"Your {direction}d message is: {crypted_word}")

# Run program again if user wants to
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message\n").lower()
    shift = input("Type the shift number\n")
    ceasar(text, shift, direction)

    choice = input("Would you like to use the Caesar cipher again? (yes/no)\n").lower()

    if choice != "yes":
        break