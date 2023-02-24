import string
import random

keyname = input("Nom du fichier clé :")
key_length = int(input("Longueur de la clé :"))

key = ''.join(random.choices(string.ascii_letters + string.digits + "_" + "-" + "&" + "#" + "!", k=key_length))

with open(f'{keyname}.key', "w") as f:
    f.write(key)
