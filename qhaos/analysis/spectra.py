import numpy as np


def level_spacings(phases):
    """
    Compute unfolded level spacings from Floquet phases

    Parameters:
        - phases: array-like, eigenphases of Floquet operator

    Returns:
        - spacings: array-like, normalized level spacings
    """
    sorted_phases = np.sort(np.mod(phases, 2*np.pi))
    spacings = np.diff(sorted_phases)
    mean_spacing = np.mean(spacings)
    return spacings/mean_spacing