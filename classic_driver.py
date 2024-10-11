class ClassicProcessor:
    def execute_classic_task(self, task):
        """Exécute une tâche classique (calcul numérique, logique, etc.)."""
        try:
            result = eval(task)
            return result
        except Exception as e:
            return f"Erreur lors de l'exécution de la tâche classique : {e}"
