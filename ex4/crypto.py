
import random

def is_legal_key(s):
    #Takes in key and checks legality by parsing to set and then comparing with alphabet
    alphabet = {chr(alpha) for alpha in range(ord('a'),(ord('z')+1))}
    if set(s) == alphabet:
        return True
    return False
    

def generate_key():
    # Create key from 'alphabet' and randomly change letters around
    alphabet = [chr(letter) for letter in range(ord('a'),ord('z')+1)]
    seen = set()
    i = 0
    while len(seen) != 26:
        rand_i = random.randint(0,25)
        if rand_i not in seen:
            seen.add(rand_i)
            alphabet[i], alphabet[rand_i] = alphabet[rand_i], alphabet[i]
            i += 1

    return ''.join(alphabet)

def encrypt(s,k):
    #Create a alphabet dict with keys {"key":'a-z'} then iterating over letters
    # matching the letter in the string to its key counterpart 
    enc_dic = {}
    enc_str = ''
    s = s.lower()
    for i in range(len(k)):
        enc_dic[(k[i])] = chr((ord('a') + i))
    for letter in s:
        if letter.isalpha():
            enc_str += enc_dic[letter] # returns value not letter itself
    return enc_str

def decrypt(s,k):
    #Create a alphabet dict with keys {'a-z':'key'} then iterating over letters
    # matching the letter in the string to its key counterpart 
    dec_dic = {}
    dec_str = ''
    for i in range(len(k)):
        dec_dic[chr(ord('a') + i)] = k[i]
    for letter in s:
        dec_str += dec_dic[letter]
    return dec_str


def main():
    #user input encrypt or decrypt, program try to open all the files
    #if the program fails it prompts the user to try to place the missing file in the directory, and waits
    #when the program continues it trys to open files again.
    mode = input('"e" for encryption | "d" for decryption: ')
    if mode.lower() == 'e':
        # encrypt opens a file from the directory and encrypts with key -> writes the encrypted data
        # and key to two seperate files
        while True:
            try: 
                rawf = open('plaintext.txt','r')
                ef = open('chipertext.txt','w')
                kf = open('key.txt','w')

                key = generate_key()
                data = rawf.read()
                enc_data = encrypt(data,key)

                kf.write(key)
                ef.write(enc_data)

                rawf.close()
                ef.close()
                kf.close()

                break

            except IOError as ex:
                print(ex, 'try placing the file in the directory')
                input('press enter to continue when you placed the missing file in the directory')

    elif mode.lower() == 'd':
        #decrypt get key and encrypted file, checks for legality of the key -> decrypting the data and writing to file
        while True:
            try:
                kf = open('key.txt','r')
                wf = open('decrypted.txt','w')
                cf = open('chipertext.txt','r')

                key = kf.read()
                data = cf.read()
                
                if is_legal_key(key):
                    dec_data = decrypt(data,key)

                wf.write(dec_data)

                kf.close()
                cf.close()
                wf.close()
                break
                
            except IOError as ex:
                print(ex, 'try placing the file in the directory')
                input('press enter to continue when you placed the missing file in the directory')

main()