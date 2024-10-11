class HexagCLI:
    def __init__(self, api):
        self.api = api

    def show_homepage(self):
        """Affiche la page d'accueil du CLI."""
        print("""
        **********************************
        *  Bienvenue dans Hexag OS        *
        *  Noyau Hybride Quantique         *
        **********************************

        1. Soumettre une tâche classique
        2. Soumettre une tâche quantique
        3. Exécuter les tâches
        4. Quitter
        """)
    
    def handle_input(self):
        """Gère les entrées utilisateur."""
        while True:
            self.show_homepage()
            choice = input("Sélectionnez une option : ")

            if choice == "1":
                task = input("Entrez la tâche classique (ex: 2 + 2) : ")
                self.api.submit_classic_task(task)
                print("Tâche classique soumise.")
            elif choice == "2":
                circuit = create_quantum_circuit()
                self.api.submit_quantum_task(circuit)
                print("Tâche quantique soumise.")
            elif choice == "3":
                self.api.run()
            elif choice == "4":
                print("Fermeture d'Hexag OS.")
                break
            else:
                print("Option non valide, réessayez.")
