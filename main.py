from rsa import *

# we select our primes and generate our public and private keys,
# usually done once
choose_again = input('Do you want to generate new public and private keys? (y or n) ')
if (choose_again == 'y'):
    chooseKeys()

instruction = input('Would you like to encrypt or decrypt? (Enter e or d): ')
if (instruction == 'e'):
    message = input('What would you like to encrypt?\n')
    option = input('Do you want to encrypt using your own public key? (y or n) ')

    if (option == 'y'):
        print('Encrypting...')
        print(encrypt(message))
    else:
        file_option = input('Enter the file name that stores the public key: ')
        print('Encrypting...')
        print(encrypt(message, file_option))

elif (instruction == 'd'):
    message = input('What would you like to decrypt?\n')
    print('Decryption...')
    print(decrypt(message))
else:
    print('That is not a proper instruction.')