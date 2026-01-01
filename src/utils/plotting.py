import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm


def plot_level_spacing_distribution(spacings, bins=50):
    # plt.hist(spacings, 
    #          bins=bins, 
    #          density=True, 
    #          alpha=0.7,
    #          label="Numerical")
    # plt.xlabel("s (normalized spacing)")
    # plt.ylabel("P(s)")
    # plt.title("Level Spacing Distribution")
    # plt.legend()
    # plt.grid(True)
    # plt.show


    plt.figure()

    #normalize spacings
    spacings = spacings / np.mean(spacings)

    #histogram
    plt.hist(spacings, 
             bins=bins, 
             density=True, 
             alpha=0.6,
             label="Numerical")
    
    #wigner-dyson (GOE)
    s = np.linspace(0, 4, 400)
    P_wigner = (np.pi/2)*s*np.exp(-1*(np.pi/4)*s**2)
    plt.plot(s, P_wigner, "r-", label="Wigner-Dyson")

    #poisson
    P_poisson = np.exp(-s)
    plt.plot(s, P_poisson, "g--", label="Poisson")

    plt.xlabel("s (normalized spacing)")
    plt.ylabel("P(s)")
    plt.title("Level Spacing Distribution")
    plt.legend()
    plt.grid(True)
    plt.show