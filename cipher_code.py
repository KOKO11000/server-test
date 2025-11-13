from string import ascii_lowercase, ascii_uppercase

offset = 3
class CaesarCode:    
    def caesar_code(messege: str):
        for i in messege:
            if i in ascii_uppercase:
                (24 + offset) % len(ascii_uppercase) == 2
                messege[i] = ascii_uppercase[i]+offset
            elif i in ascii_lowercase:
                (24 + offset) % len(ascii_uppercase) == 2
                messege[i] = ascii_lowercase[i]+offset
            return messege


    def reverse_caesar(messege_code):
        clean_messege = reversed(messege_code)
        return clean_messege



class RailFenceCipher:
    def get_a_messege(messege: str):
        return messege
    
    def removes_spaces(messege_with_spaces: get_a_messege):
        messege_without_spaces = messege_with_spaces.strip(" ")
        return messege_without_spaces
    
    def separate_even_letters(messge_without_spaces: removes_spaces):
        even = None
        odd = None
        for i in messge_without_spaces:
            if i % 2 == 0:
                even += i
            else:
                odd += i
        fence_code = even + odd
        return fence_code
    
    


