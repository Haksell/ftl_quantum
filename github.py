import numpy as np
from qiskit import QuantumCircuit
from qiskit.primitives import StatevectorSampler

qc = QuantumCircuit(3)
qc.h(0)
qc.p(np.pi / 2, 0)
qc.cx(0, 1)
qc.cx(0, 2)

qc_measured = qc.measure_all(inplace=False)
sampler = StatevectorSampler()
job = sampler.run([qc_measured], shots=1000)
result = job.result()
print(f" > Counts: {result[0].data['meas'].get_counts()}")
