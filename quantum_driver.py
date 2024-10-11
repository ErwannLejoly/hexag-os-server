from qiskit import QuantumCircuit, Aer, transpile, execute

class QuantumProcessor:
    def execute_quantum_task(self, circuit):
        """Exécute un circuit quantique."""
        try:
            simulator = Aer.get_backend('qasm_simulator')
            compiled_circuit = transpile(circuit, simulator)
            job = execute(compiled_circuit, simulator, shots=1024)
            result = job.result().get_counts()
            return result
        except Exception as e:
            return f"Erreur lors de l'exécution de la tâche quantique : {e}"

def create_quantum_circuit():
    """Crée un circuit quantique simple pour l'exemple."""
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure_all()
    return qc
