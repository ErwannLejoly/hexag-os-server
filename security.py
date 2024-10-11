import threading

class SafeHexagScheduler(HexagScheduler):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()

    def add_task(self, task_type, task, priority=1):
        """Ajoute une tâche de manière sécurisée (thread-safe)."""
        with self.lock:
            super().add_task(task_type, task, priority)

    def schedule_tasks(self, classic_processor, quantum_processor):
        """Planifie les tâches de manière sécurisée (thread-safe)."""
        with self.lock:
            super().schedule_tasks(classic_processor, quantum_processor)
