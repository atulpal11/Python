from qiskit import QuantumCircuit 
from qiskit.quantum_info import SparsePauliOp 
from qiskit.transpiler import generate_preset_pass_manager 
from qiskit_ibm_runtime import EstimatorV2 as Estimator 
# Create a new circuit with two qubits 
qc = QuantumCircuit(1) 
# Add a Hadamard gate to qubit 0 
qc.h(0) 
# Return a drawing of the circuit using MatPlotLib ("mpl"). This is the 
# last line of the cell, so the drawing appears in the cell output. 
# Remove the "mpl" argument to get a text drawing. 
qc.draw("mpl")