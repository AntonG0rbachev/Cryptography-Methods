from caesar import CaesarAlgorithm
import argparse

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