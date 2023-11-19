import os, sys
from time import perf_counter
from multiprocessing import Pool

args = sys.argv[1:]
if len(args) < 3:
    print("ERREUR: Nombre d'arguments insuffisant !",\
            "python zecrypt_xor_mass.py [E/D] [dossier racine] [fichier clé]", sep="\n")
    exit()

def process(filename) -> tuple[str, float]:
    print(f"Traitement de {filename} ...")
    if args[0] == "E" or args[0] == "e":
        output = f"{filename}.encrypted"
    else:
        output = filename.replace(".encrypted","")

    t_start = perf_counter()

    with open(filename,"rb") as input_file:
        data = input_file.read()
    
    with open(args[2],"rb") as key_file:
        key_string = key_file.read()
    key = tuple([byte for byte in key_string])
    
    encrypted_data = bytearray([data[i] ^ key[i % len(key_string)] for i in range(len(data))])

    with open(output,"wb") as output_file:
        output_file.write(encrypted_data)
    
    t_stop = perf_counter()
    duration = t_stop - t_start

    os.remove(filename)
    return filename, duration


def main():
    if args[0] != "E" and args[0] != "e" and args[0] != "D" and args[0] != "d":
        print("ERREUR: Méthode invalide")
        return
    
    try:
        with open(args[2],"rb") as f:
            key = f.read()
    except FileNotFoundError:
        print("ERREUR: Fichier introuvable")
        return
    
    global_t_start = perf_counter()
    try:
        file_list = []
        for root,dirs,files in os.walk(args[1]):
            for name in files:
                filename = root + os.sep + name
                file_list.append(filename)
        
        with Pool() as pool:
            results = pool.map(process,file_list)
            for filename,duration in results:
                print(f"{filename} traité en {duration:.2f} secondes")
        
        global_t_stop = perf_counter()
        global_duration = global_t_stop - global_t_start
        print(f"\n\nTous les fichiers ont été traités !\nTemps écoulé: {global_duration:.1f} secondes")
    except KeyboardInterrupt:
        global_t_stop = perf_counter()
        global_duration = global_t_stop - global_t_start
        print(f"\n\nOpération annulée par l'utilisateur (KeyboardInterrupt)\nTemps écoulé: {global_duration:.1f} secondes")
        return

if __name__ == "__main__":
    main()