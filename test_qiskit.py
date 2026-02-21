from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit import transpile

# Create a circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

print("Circuit:")
print(qc)

simulator = AerSimulator()
compiled = transpile(qc, simulator)
result = simulator.run(compiled).result()

counts = result.get_counts()

print("\nResults:")
print(counts)