import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Définition des symboles
t = sp.Symbol('t')
x = sp.Function('x')(t)

# Paramètres
k = 4000
m = 10
alpha = 20

# Équation différentielle
eq = m * x.diff(t, t) + alpha * x.diff(t) + k * x

# Conditions initiales
x0 = 0.01
dx_dt_0 = 0

# Résolution
sol = sp.dsolve(eq, x, ics={x.subs(t, 0): x0, x.diff(t).subs(t, 0): dx_dt_0})

# Affichage de la solution
print('la valeur de x(t):')
sp.pprint(sol.rhs)
print('\n')

# Calcul de l'énergie cinétique et de l'énergie potentielle
x_t = sol.rhs
dx_dt_t = x_t.diff(t)
Ec = 0.5 * m * dx_dt_t**2
Ep = 0.5 * k * x_t**2
Em = Ec + Ep

# Plot
plt.figure(figsize=(8, 6))
plt.plot(sp.lambdify(t, x_t)(np.linspace(0, 10, 100)), label='x(t)')
plt.xlabel('Temps (s)')
plt.ylabel('Position (m)')
plt.title('Oscillations libres')
plt.legend()
plt.grid(True)
plt.show()

# Affichage des énergies
print(f'Énergie cinétique (Ec) : {Ec}')
print('\n')
print(f'Énergie potentielle (Ep) : {Ep}')
print('\n')
print(f'Énergie mécanique (Em) : {Em}')
print('\n')