'''
CISC-121 2022F

Name: Yun Kyaw
Date: 2022-09-16

I confirm that this assignment solution is my own work and conforms to
Queen’s standards of Academic Integrity
'''
import string


def making_uppercase(plaintext, key):
    """
    This function converts the plaintext and key to uppercase letters, and removes non-letters from the plaintext
    Input: 
        plaintext, key  - str
    Output:
        plaintext_alpha, key  - str
    """
    plaintext = plaintext.upper()
    key = key.upper()

    plaintext_alpha = ""
    """This for loop removes non-letters from the plaintext"""
    for letter in plaintext:
        if letter.isalpha() == True: 
            plaintext_alpha += letter

    return(plaintext_alpha, key)



def encrypt_plaintext(plaintext, key, table):
    """
    This function encrypts the plaintext
    Input:
        plaintext, key  - str
        table - list of lists
    Output: 
        plaintext_encrypt - str
    """
    plaintext_encrypt = ""  # this represents the new encrypted plaintext

    key_plaintext_diff = len(plaintext) - len(key)

    """This for loop extends the length of the key to match the length of the plaintext"""
    for i in range(key_plaintext_diff):
        key += key[i]

    """This for loop finds the row and column that the key and plaintext belong to, to find the corresponding cypher value"""
    for i in range(len(key)):
        for nos in range(26):
            if key[i] == table[nos][0]:
                encrypt_row = nos
            if plaintext[i] == table[0][nos]:
                encrypt_col = nos
        encrypt_letter = table[encrypt_row][encrypt_col]
        plaintext_encrypt += encrypt_letter
    return(plaintext_encrypt)



def main():
    alphabet = list(string.ascii_uppercase)
    # Create the Vigenere table
    table = []  # this represents the Vigenere table
    r = []  # this represents each row in the table

    """This for loop creates the Vigenere table by splicing the alphabet"""
    for i in range(26):
        for letter in alphabet:  
            r = alphabet[i:] + alphabet[:i]
        table.append(r)
    
    loop = "Yes"
    while loop == "Yes" or loop == "yes":
        plaintext = input("What is the plaintext? ")
        key = input("What is the key? ")

        upper = making_uppercase(plaintext, key)

        plaintext_encrypt = encrypt_plaintext(upper[0], upper[1], table)
        print("The Vigenere cypher is:", plaintext_encrypt)
        
        loop = input("Would you like to create another cypher? (Yes/No) ")
        
    print("Okay, goodbye...")
    
main()




