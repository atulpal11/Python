from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector, plot_histogram
import matplotlib.pyplot as plt
import numpy as np

def run_swap_cs(state_label):
    qc = QuantumCircuit(2, 2)
    if state_label == "|01⟩":
        qc.x(1)
    elif state_label == "|10⟩":
        qc.x(0)
    elif state_label == "|11⟩":
        qc.x([0, 1])
    qc.swap(0, 1)
    qc.cp(np.pi/2, 0, 1)

    # get statevector before adding measurements
    state = Statevector.from_instruction(qc)

    # draw circuit (matplotlib figure)
    fig_circ = qc.draw("mpl")
    fig_circ.show()
    plt.show()

    # Bloch sphere for the multi-qubit state (plot_bloch_multivector returns a figure)
    print(f"\nBloch Sphere for {state_label}:")
    fig_bloch = plot_bloch_multivector(state)
    fig_bloch.show()
    plt.show()

    # add measurements and run simulator to get counts
    qc.measure([0, 1], [0, 1])
    sim = AerSimulator()
    result = sim.run(qc, shots=1024).result()
    counts = result.get_counts()

    print(f"\nMeasurement Histogram for {state_label}:")
    fig_hist = plot_histogram(counts)
    fig_hist.show()
    plt.show()

if __name__ == "__main__":
    for state in ["|01⟩", "|10⟩", "|11⟩"]:
        run_swap_cs(state)