from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    """text=abcd	rot=13	output=nopq"""
    encrypted = ""
    for i in text:
        rotated_chars = rotate_character(i, rot)
        encrypted += rotated_chars
        
    return encrypted


#print(encrypt("Hello, World!", 5))


def main():
    text = input("Enter the text: ")
    rot = input("Enter the rotation number: ")
    print(encrypt(text, rot))
    


if __name__ == "__main__":
    main()












        





