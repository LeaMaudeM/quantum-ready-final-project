from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

num_bits = 8 # Length of the pad
qc = QuantumCircuit(num_bits, num_bits)

# Apply H-gate to all qubits
for i in range(num_bits):
    qc.h(i)

# Measure all qubits
qc.measure(range(num_bits), range(num_bits))

# Run simulation
simulator = AerSimulator()
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1, memory=True)
result = job.result()
random_pad = result.get_memory(qc)[0]

print(f"Generated {num_bits}-bit pad: {random_pad}")