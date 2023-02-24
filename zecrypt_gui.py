import os

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import ttk

def encryptFile():
    in_file = filedialog.askopenfile(title="Sélectionner fichier à chiffrer").name
    out_file = in_file+".encrypted"
    key = simpledialog.askstring(title="Clé de chiffrement", prompt="Veuillez entrer la clé de chiffrement")
    deleteFile = messagebox.askyesno(title="Suppression du fichier", message="Souhaitez vous supprimer le fichier original après le chiffrement ?")

    from hashlib import sha256
    keys = sha256(key.encode("utf-8")).digest()
    with open(in_file,"rb") as f_input:
        with open(out_file,"wb") as f_output:
            i = 0
            while f_input.peek():
                c = ord(f_input.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_output.write(b)
                i = i +1
    if deleteFile==True:
        os.remove(in_file)

def decryptFile():
    in_file = filedialog.askopenfile(title="Sélectionner fichier à déchiffrer").name
    out_file = in_file.replace(".encrypted","")
    key = simpledialog.askstring(title="Clé de chiffrement", prompt="Veuillez entrer la clé de chiffrement")
    deleteFile = messagebox.askyesno(title="Suppression du fichier", message="Souhaitez vous supprimer le fichier original après le déchiffrement ?")

    from hashlib import sha256
    keys = sha256(key.encode("utf-8")).digest()
    with open(in_file,"rb") as f_input:
        with open(out_file,"wb") as f_output:
            i = 0
            while f_input.peek():
                c = ord(f_input.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_output.write(b)
                i = i +1
    if deleteFile==True:
        os.remove(in_file)


root = Tk()
root.title("ZeCrypt - Version 2.1")
root.geometry("175x200")
root.attributes("-alpha", 0.9)
root.iconphoto(False, PhotoImage(file='C:/Windows/System32/@bitlockertoastimage.png'))

frame = ttk.Frame(root, padding=10)
frame.grid()
ttk.Label(frame, text="ZeCrypt", font=("Arial",24)).grid(column=0, row=0)
ttk.Label(frame, text="").grid(column=0,row=1)
ttk.Label(frame, text="").grid(column=0,row=2)
ttk.Button(frame, text="Chiffrer un fichier", command=encryptFile).grid(column=0,row=3)
ttk.Button(frame, text="Déchiffrer un fichier", command=decryptFile).grid(column=0,row=4)
ttk.Label(frame, text="").grid(column=0,row=5)
ttk.Button(frame, text="QUITTER", command=root.destroy).grid(column=0, row=99)
root.mainloop()
