import numpy as np


# def floquet_operator(N, K, hbar):
#     """
#     Constructs the Floquet operator for the quantum kicked rotor.

#     Parameters:
#         - N: int, Hilbert space dimension
#         - K: float, kick strength
#         - hbar: float effective Planck constant

#     Returns:
#         - U: np.ndarray, Floquet operator
#     """
#     n = np.arange(N)
#     p = np.exp(-1j * (hbar* n**2)/2)
#     V = np.exp(-1j * K * np.cos(2 * np.pi*n/N)/hbar) #kicking potential

#     U = np.fft.ifft(np.fft.fft(p*V)) # "simple" way to write U = P*V
#     return U



def floquet_operator(N, K, hbar):
    """
    Constructs the Floquet operator U = exp(-iT p^2 / 2hbar) * exp(-iK cos(x) / hbar)
    in momentum basis.
    
    Parameters:
    - N: int, Hilbert space dimension
    - K: float, kick strength
    - hbar: float, effective Planck constant
    
    Returns:
    - U: (N, N) complex ndarray, the Floquet operator
    """
    # Define momentum basis
    n = np.arange(N)
    p = np.exp(-1j * (hbar * n**2) / 2)
    
    # Kicking potential in position basis
    theta = np.arange(N) * 2 * np.pi / N
    V = np.exp(-1j * K * np.cos(theta) / hbar)
    
    # Define DFT and its inverse
    F = np.fft.fft(np.eye(N)) / np.sqrt(N)
    F_dag = np.conj(F.T)
    
    # Construct U = F_dag @ diag(p) @ F @ diag(V)
    U = F_dag @ np.diag(p) @ F @ np.diag(V)
    return U