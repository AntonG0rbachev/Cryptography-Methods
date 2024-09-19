import argparse

class CaesarAlgorithm:

    def encrypt(self, message, key, alphabet):

        # start with empty ciphertext
        ciphertext = ""

        # iterate through each character in message
        for old_character in message:
            new_character = ""

            # if character is in alphabet -> append to ciphertext
            if(old_character in alphabet):
                index = alphabet.index(old_character)
                new_index = (index + key) % len(alphabet)
                new_character = alphabet[new_index]

            # Note: characters not defined in the alphabet are ignored

            # add new character to ciphertext
            ciphertext = ciphertext + new_character

        # return ciphertext to calling function
        return ciphertext


    def decrypt(self, message, key, alphabet):

        # decrypting is like encrypting but with negative key
        plaintext = self.encrypt(message, 0 - key, alphabet)

        # return plaintext to calling function
        return plaintext


# parse the arguments (args) given via the command line
parser = argparse.ArgumentParser()
parser.add_argument("-e", "--encrypt", dest="encrypt_or_decrypt", action="store_true")
parser.add_argument("-d", "--decrypt", dest="encrypt_or_decrypt", action="store_false")
parser.add_argument("-m", "--message", help="message for encrypt / decrypt", type=str)
parser.add_argument("-k", "--key", help="key for encrypt / decrypt", type=int)
parser.add_argument("-a", "--alphabet", help="defined alphabet", type=str)
args = parser.parse_args()

# create caesar instance
caesar = CaesarAlgorithm()

# if --encrypt -> call encrypt function
if(args.encrypt_or_decrypt == True):
    print(caesar.encrypt(args.message, args.key, args.alphabet))

# if --decrypt -> call decrypt function
else:
    print(caesar.decrypt(args.message, args.key, args.alphabet))