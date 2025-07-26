# qhaos
Code for simulating and analyzing quantum chaotic systems.

### Quantum Kicked Rotor
The kicked rotor describes a free rotating stick in gravitation like field that is periodically switched on in short pulses. The Hamiltonian is given by\
$$\mathcal{H}(\theta, p_\theta, t) = \frac{p_\theta^2}{2I} + K\cos(\theta) \sum_{n=-\infty}^\infty \delta\left( \frac{t}{T} - n \right)$$\
In the quantum description we note that because the Hamiltonian is periodic in time, the dynamics can be described using the Floquet operator which evolves the system from one kick to the next\
$$U = e^{-i\frac{p^2}{2\hbar}}e^{-i\frac{K}{\hbar}\cos(\theta)}$$\
The full evolotion is obtained by sandwiching the potential operator between Fourier transforms.
