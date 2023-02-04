alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]


def caesar(direct, word_text, shift_number):
    """ Function to encrypt and decrypt text by specific shift number"""
    caesar_text = ""
    if direct == "decrypt":
        shift_number *= -1
    for letter in word_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            position_new = position + shift_number
            caesar_text += alphabet[position_new]
        else:
            caesar_text += letter
    print(f"The {direct}ed text is {caesar_text}")


while True:
    direction = input("Type 'encrypt' to encode and 'decrypt' to decode the text message: ").lower()
    word = input("What is the word? ").lower()
    shift = int(input("What is the shift?"))
    shift = shift % 26
    caesar(word_text=word, shift_number=shift, direct=direction)
    decide = input("Do you want to continue? Type 'yes' or 'no'").lower()
    if decide == "no":
        break
