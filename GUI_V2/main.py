import kivy
from kivy.app import App
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout

from hashlib import sha256
from threading import Thread
import os

kivy.require('1.9.0')

class MTThread(Thread):
    def __init__(self, name = "", target = None):
        self.mt_name = name
        self.mt_target = target
        Thread.__init__(self, name = name, target = target)
    def start(self):
        super().start()
        Thread.__init__(self, name = self.mt_name, target = self.mt_target)
    def run(self):
        super().run()
        Thread.__init__(self, name = self.mt_name, target = self.mt_target)

class MyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(MyRoot, self).__init__(**kwargs)

    def encryptFile(self):
        # Acquisition des variables
        input_file = self.input_file.text
        output_file = input_file + ".encrypted"
        useKeyfile = self.use_key.active
        if useKeyfile:
            keyfile = self.encryption_key.text
            try:
                with open(keyfile, "r") as f:
                    key = f.read()
            except FileNotFoundError:
                print("[ERROR] Fichier introuvable ! Opération annulée !")
                return
        else:
            key = self.encryption_key.text

        # Désactivation des boutons
        self.start_encryption.disabled = True
        self.start_decryption.disabled = True

        # Chiffrement du fichier
        keys = sha256(key.encode("utf-8")).digest()
        with open(input_file,"rb") as f_entree:
            size = os.fstat(f_entree.fileno()).st_size
            self.status.color = 1, 0.38, 0, 1
            self.status.text = "CHIFFREMENT EN COURS (0%) ..."
            with open(output_file,"wb") as f_sortie:
                i = 0
                while f_entree.peek():
                    c = ord(f_entree.read(1))
                    j = i % len(keys)
                    b = bytes([c^keys[j]])
                    f_sortie.write(b)
                    i = i +1
                    percentage = 100 * (i / size)
                    self.status.text = f"CHIFFREMENT EN COURS ({percentage:.2f}%) ..."
        # Réinitialisation
        self.status.text = "CHIFFREMENT TERMINE !"
        self.status.color = 0, 1, 0, 1
        self.start_encryption.disabled = False
        self.start_decryption.disabled = False
        os.remove(input_file)
        return
    
    def decryptFile(self):
        # Acquisition des variables
        input_file = self.input_file.text
        output_file = input_file.replace(".encrypted", "")
        useKeyfile = self.use_key.active
        if useKeyfile:
            keyfile = self.encryption_key.text
            try:
                with open(keyfile, "r") as f:
                    key = f.read()
            except FileNotFoundError:
                print("[ERROR] Fichier introuvable ! Opération annulée !")
                return
        else:
            key = self.encryption_key.text

        # Désactivation des boutons
        self.start_encryption.disabled = True
        self.start_decryption.disabled = True

        # Déchiffrement du fichier
        keys = sha256(key.encode("utf-8")).digest()
        with open(input_file,"rb") as f_entree:
            size = os.fstat(f_entree.fileno()).st_size
            self.status.color = 1, 0.38, 0, 1
            self.status.text = "DECHIFFREMENT EN COURS (0%) ..."
            with open(output_file,"wb") as f_sortie:
                i = 0
                while f_entree.peek():
                    c = ord(f_entree.read(1))
                    j = i % len(keys)
                    b = bytes([c^keys[j]])
                    f_sortie.write(b)
                    i = i +1
                    percentage = 100 * (i / size)
                    self.status.text = f"DECHIFFREMENT EN COURS ({percentage:.2f}%) ..." 
        # Réinitialisation
        self.status.text = "DECHIFFREMENT TERMINE !"
        self.status.color = 0, 1, 0, 1
        self.start_encryption.disabled = False
        self.start_decryption.disabled = False
        os.remove(input_file)
        return
    
    def call_encryption(self):
        thread = MTThread(name="Encryption", target=self.encryptFile)
        thread.start()
        return
    
    def call_decryption(self):
        thread = MTThread(name="Decryption", target=self.decryptFile)
        thread.start()
        return

class ZecryptApp(App):
    def build(self):
        return MyRoot()

application = ZecryptApp()
application.run()