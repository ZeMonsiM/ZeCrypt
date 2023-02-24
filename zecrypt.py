from hashlib import sha256
import os
in_file = input("Fichier en entrée :")
out_file = input("Fichier en sortie :")
key = input("Clé de chiffrement (entrer 'file' pour utiliser un fichier comme clé) :")

def progressbar(progress, total):
    percent = 100 * (progress / float(total))
    bar = '█' * int(percent) + '-' * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")

if key=="file":
    filename = input("Emplacement du fichier clé :")
    try:
        with open(filename, "r") as f:
            key = f.read()
    except FileNotFoundError:
        print("[ERROR] Fichier introuvable ! Opération annulée !")
        exit()

keys = sha256(key.encode("utf-8")).digest()
with open(in_file,"rb") as f_input:
    size = os.fstat(f_input.fileno()).st_size
    progressbar(0,size)
    with open(out_file,"wb") as f_output:
        i = 0
        while f_input.peek():
            c = ord(f_input.read(1))
            j = i % len(keys)
            b = bytes([c^keys[j]])
            f_output.write(b)
            i = i +1
            progressbar(i, size)
