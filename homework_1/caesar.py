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
