import string 

def alphabet_position(letter):
    """Function takes a letter and returns the index position of that letter with 0 being 'a'
    or 'A' and 'z' being 25. Function should be case insensitive."""
    letters = string.ascii_lowercase

    return letters.index(letter.lower())      

def rotate_character(char, rot):
    """ rotate letter(char) by number(rot) to the right. Return the value after rotation"""
    """ If char is not a letter i.e != isalpha() == False, return the original value"""
    letterss = string.ascii_lowercase 
    if char.isalpha() == True:
        rotated_position = (alphabet_position(char) + rot) % 26
        rotated_char = letterss[rotated_position]
        if char in string.ascii_uppercase:
            return(rotated_char.upper()) 
        else:
            return(rotated_char)
    
    else:
        return(char)