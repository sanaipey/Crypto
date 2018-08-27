from helpers import alphabet_position, rotate_character
import string
        
def encrypt(input_char, encryption_char):
    """ input= The  crow flies at midnight!” , key = "boom", Uvs osck rmwse bh auebwsih!
    input_char = input("Enter message")"""
    """ use for loop for the  input so it iterates over each letter, and with each letter use another for loop """
    encrypted = []
    start_index = 0
    for letter in input_char:
        rotation = alphabet_position(encryption_char[start_index])



        if letter in string.ascii_letters:
            encrypted.append(rotate_character(letter, rotation))
            if start_index == (len(encryption_char) -1):
                start_index = 0
            else:
                start_index += 1

        else:
            encrypted.append(letter)

    return ''.join(encrypted)

def main():
    input_char = input("Enter a message to encrypt")
    encryption_char = input("Enter the encryption key")
    print(encrypt(input_char, encryption_char))
    
if __name__ == "__main__":
    main()

