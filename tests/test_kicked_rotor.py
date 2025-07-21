import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

from qhaos.models.kicked_rotor import floquet_operator
import numpy as np


def test_floquet_operator_unitary():
    N = 64
    K = 5.0
    hbar = 2*np.pi/N
    U = floquet_operator(N, K, hbar)
    identity = np.eye(N)
    assert np.allclose(U.conj().T @ U, identity, atol=1e-10)