from string import ascii_lowercase, ascii_uppercase


class CaesarCode: 
    def caesar_code(messege: str, offset: int):
        for i in messege:
            if i in ascii_uppercase:
                (24 + offset) % len(ascii_uppercase) == 2                
                messege.index(i) == ascii_uppercase.index(i) + offset
            
            elif i in ascii_lowercase:
                (24 + offset) % len(ascii_uppercase) == 2
                caesar_code = ascii_lowercase.index(i)+ offset
                messege.index(i) == caesar_code
            return messege


    def reverse_caesar(messege_code):
        clean_messege = reversed(messege_code)
        return clean_messege



class RailFenceCipher:
    def get_a_messege(messege: str):
        return messege
    
    def removes_spaces(messege_with_spaces: get_a_messege):
        messege_without_spaces = messege_with_spaces.repalce(" ", "")
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
    
    


