class HexagAPI:
    def __init__(self, scheduler, classic_processor, quantum_processor):
        self.scheduler = scheduler
        self.classic_processor = classic_processor
        self.quantum_processor = quantum_processor

    def submit_classic_task(self, task, priority=1):
        """Soumet une tâche classique au planificateur."""
        self.scheduler.add_task("classic", task, priority)

    def submit_quantum_task(self, circuit, priority=1):
        """Soumet une tâche quantique au planificateur."""
        self.scheduler.add_task("quantum", circuit, priority)

    def run(self):
        """Exécute les tâches en attente."""
        self.scheduler.schedule_tasks(self.classic_processor, self.quantum_processor)
