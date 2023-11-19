import time

input_file = input("Fichier à chiffrer: ")
output_file = input("Nom du fichier en sortie: ")
filename = input("Clé de chiffrement (fichier): ")

t_start = time.perf_counter()

with open(input_file, 'rb') as file_in:
    content = file_in.read()

with open(filename,"rb") as key:
    key_content = key.read()
key = tuple([byte for byte in key_content])

encrypted_content = bytearray([content[i] ^ key[i % len(key_content)] for i in range(len(content))])

with open(output_file, 'wb') as file_out:
    file_out.write(encrypted_content)

t_stop = time.perf_counter()
print(f"Fichier chiffré en {t_stop - t_start:0.2f} secondes !")

