import matplotlib.pyplot as plt


def plot_level_spacing_distribution(spacings, bins=50):
    plt.hist(spacings, 
             bins=bins, 
             density=True, 
             alpha=0.7,
             label="Numerical")
    plt.xlabel("s (normalized spacing)")
    plt.ylabel("P(s)")
    plt.title("Level Spacing Distribution")
    plt.legend()
    plt.grid(True)
    plt.show