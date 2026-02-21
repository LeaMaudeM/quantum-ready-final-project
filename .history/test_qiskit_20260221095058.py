from qiskit import QuantumCircuit
from qiskit.primitives import Sampler

# Create a simple circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

print("Circuit:")
print(qc)

# Run it with the sampler
sampler = Sampler()
result = sampler.run(qc).result()

print("\nResult:")
print(result)