class QuantumMemoryManager:
    def __init__(self, total_qubits):
        self.total_qubits = total_qubits
        self.allocated_qubits = set()

    def allocate_qubits(self, num_qubits):
        """Alloue un certain nombre de qubits si disponibles."""
        if len(self.allocated_qubits) + num_qubits > self.total_qubits:
            raise ValueError("Nombre de qubits insuffisants.")
        qubit_indices = list(range(len(self.allocated_qubits), len(self.allocated_qubits) + num_qubits))
        self.allocated_qubits.update(qubit_indices)
        return qubit_indices

    def free_qubits(self, qubit_indices):
        """Libère les qubits utilisés."""
        for qubit in qubit_indices:
            self.allocated_qubits.discard(qubit)

    def get_available_qubits(self):
        """Renvoie le nombre de qubits disponibles."""
        return self.total_qubits - len(self.allocated_qubits)
