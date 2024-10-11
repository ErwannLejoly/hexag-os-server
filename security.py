import threading
from Crypto.Cipher import AES
import base64

class Security:
    def __init__(self, key):
        """Initialiser la sécurité avec une clé AES de 32 octets."""
        self.key = key.ljust(32)[:32].encode('utf-8')

    def encrypt(self, data):
        """Chiffrer les données."""
        cipher = AES.new(self.key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data.encode('utf-8'))
        return base64.b64encode(cipher.nonce + tag + ciphertext).decode('utf-8')

    def decrypt(self, encrypted_data):
        """Déchiffrer les données."""
        data = base64.b64decode(encrypted_data.encode('utf-8'))
        nonce, tag, ciphertext = data[:16], data[16:32], data[32:]
        cipher = AES.new(self.key, AES.MODE_EAX, nonce=nonce)
        return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')

class SafeHexagScheduler(HexagScheduler):
    def __init__(self, security):
        """Initialiser le planificateur sécurisé avec verrou et sécurité."""
        super().__init__()
        self.lock = threading.Lock()
        self.security = security

    def add_task(self, task_type, task, priority=1):
        """Ajoute une tâche de manière sécurisée (thread-safe) et chiffrée."""
        with self.lock:
            # Chiffrer la tâche avant de l'ajouter
            encrypted_task = self.security.encrypt(task)
            super().add_task(task_type, encrypted_task, priority)

    def schedule_tasks(self, classic_processor, quantum_processor):
        """Planifie les tâches de manière sécurisée (thread-safe)."""
        with self.lock:
            super().schedule_tasks(classic_processor, quantum_processor)

# Exemple d'utilisation
if __name__ == "__main__":
    sec = Security("secret_key")  # Clé utilisée pour chiffrer les tâches
    scheduler = SafeHexagScheduler(sec)

    # Simuler l'ajout d'une tâche
    task = "Calcul quantique sensible"
    scheduler.add_task("quantum", task, priority=2)

    # Planifier les tâches sur les processeurs (à définir)
    classic_processor = None  # Remplacer par le processeur classique
    quantum_processor = None  # Remplacer par le processeur quantique
    scheduler.schedule_tasks(classic_processor, quantum_processor)
