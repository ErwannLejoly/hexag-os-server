import queue

class HexagScheduler:
    def __init__(self):
        self.classic_queue = queue.PriorityQueue()  # File des tâches classiques
        self.quantum_queue = queue.PriorityQueue()  # File des tâches quantiques
        self.task_priorities = {}

    def add_task(self, task_type, task, priority=1):
        """Ajoute une tâche avec une priorité dans la file correspondante."""
        if task_type == "classic":
            self.classic_queue.put((priority, task))
        elif task_type == "quantum":
            self.quantum_queue.put((priority, task))
        self.task_priorities[task] = priority

    def schedule_tasks(self, classic_processor, quantum_processor):
        """Planifie les tâches en fonction des priorités."""
        # Exécution des tâches classiques
        while not self.classic_queue.empty():
            priority, task = self.classic_queue.get()
            result = classic_processor.execute_classic_task(task)
            print(f"Résultat de la tâche classique : {result}")

        # Exécution des tâches quantiques
        while not self.quantum_queue.empty():
            priority, task = self.quantum_queue.get()
            result = quantum_processor.execute_quantum_task(task)
            print(f"Résultat de la tâche quantique : {result}")
