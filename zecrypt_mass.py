import os
from hashlib import sha256
import time
from multiprocessing import Pool
import sys

def main_func():
    args = sys.argv[1:]
    if len(args) < 3:
        print("ERREUR: Veuillez exécuter la commande avec les arguments !","Syntaxe: zecrypt_mass_mp.py [méthode] [répertoire] [clé de chiffrement] [emplacement de la clé (facultatif)]",\
            "Méthode: 1=Chiffrer, 2=Déchiffrer\nRépertoire: Dossier contenant les fichiers à chiffrer\nClé de chiffrement: entrer 'file' utilisera comme clé le contenu du fichier spécifié en 4e argument", sep="\n\n")
        exit()

    method = args[0]
    root_dir = args[1]
    if args[2] != "file":
        key = args[2]
    else:
        if len(args) < 4:
            print("ERREUR: Argument manquant (emplacement de la clé) !")
            exit()
        else:
            try:
                with open(args[3], "r") as f:
                    key = f.read()
            except FileNotFoundError:
                print("[ERROR] Fichier introuvable ! Opération annulée !")
                exit()
    keys = sha256(key.encode()).digest()
    keys = str(keys)

    t_start_global = time.perf_counter()
    try:
        filenames = []
        for root, dirs, files in os.walk(root_dir):
            for name in files:
                filename = root + os.sep + name
                filenames.append(filename)
        with Pool() as pool:
            results = pool.map(encrypt, filenames)
            for filename, duration in results:
                print(f"'{filename}' traité en {duration:.1f} secondes")
        t_stop_global = time.perf_counter()
        t_elapsed_global = t_stop_global - t_start_global
        print(f"\n\nTous les fichiers ont été traités ! Temps écoulé: {t_elapsed_global:0.1f} secondes")
    except KeyboardInterrupt:
        t_stop_global = time.perf_counter()
        t_elapsed_global = t_stop_global - t_start_global
        print(f"\n\nOpération annulée par l'utilisateur (KeyboardInterrupt)\nTemps écoulé: {t_elapsed_global} secondes")
        exit()

def encrypt(filename) -> tuple[str, float]:

    method = int(sys.argv[1])
    if sys.argv[3] != "file":
        key = sys.argv[3]
    else:
        if len(sys.argv) < 5:
            print("ERROR: Argument manquant (emplacement de la clé) !")
            exit()
        else:
            try:
                with open(sys.argv[4], "r") as f:
                    key = f.read()
            except FileNotFoundError:
                print("[ERROR] Fichier introuvable ! Opération annulée !")
                exit()
    keys = sha256(key.encode()).digest()

    print(f"Traitement de '{filename}' ...")
    if method == 1:
        outfile = f"{filename}.encrypted"
    else:
        outfile = filename.replace(".encrypted","")
    
    t_start = time.perf_counter()
    with open(filename,"rb") as f_input:
        with open(outfile,"wb") as f_output:
            i = 0
            while f_input.peek():
                c = ord(f_input.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_output.write(b)
                i = i +1
    t_stop = time.perf_counter()
    t_elapsed = t_stop - t_start
    os.remove(filename)
    return filename, t_elapsed

if __name__ == "__main__":
    main_func()