# Logo 
print(''' ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
                   88                                      
                          88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88         ''')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

'''
ToDo 1 : Create a function called encrypt () that takes original_text and shift_amount as 2 inputs.
ToDo 2 : Inside the encrypt function,shift each letter of the original_text towards in the alphabet by the shift amount and print the encrypted text.
ToDo 3 : Call the encrypt function and pass in it user inputs.
'''

# Encrypt function
def encrypt(original_text, shift):
    encrypt_msg = ""
    for char in original_text:
        if char.isalpha():
            cnt = (alphabet.index(char) + shift) % 26
            encrypt_msg += alphabet[cnt]
        else:
            encrypt_msg += char
    print(f"Encrypted msg is: {encrypt_msg}")
    
'''
ToDO 1: Create a function called decrypt() that takes original_text and shift_amount as 2 inputs
ToDo 2: Inside the decrypt() function, shift each letter of the original_text forwards in backward by the shift_amount and print the decrypted text
ToDo 3: Combine the encrypt() and decrypt() f(x)s into a single f(x) called ceasar().    
'''

# Decrypt function
def decrypt(encrypt_msg, shift):
    decrypt_msg = ""
    for char in encrypt_msg:
        if char.isalpha():
            cnt = (alphabet.index(char) - shift) % 26
            decrypt_msg += alphabet[cnt]
        else:
            decrypt_msg += char
    print(f"Decrypted msg is: {decrypt_msg}")

# Combined Caesar Cipher function
def ceaser(encode_or_decode, original_text, shift_amount):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:
        if char.isalpha():
            cnt = (alphabet.index(char) + shift_amount) % 26
            output_text += alphabet[cnt]
        else:
            output_text += char
    print(f"Here is the {encode_or_decode}d message: {output_text}")

# User input loop
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    ceaser(direction, text, shift)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye!")
