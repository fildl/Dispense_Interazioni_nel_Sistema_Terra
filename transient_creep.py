import matplotlib.pyplot as plt
import numpy as np
import math
import os

def exponential_retardation(x,
                            A, tau):
    return A * (1 - np.exp(-x / tau))

def Andrade_creep_equation(x,
                           epsilon0, beta, m):
    return epsilon0 + beta * (x ** m)

def Scott_Blair(x,
                a, nu):
    return a * x ** nu / math.gamma(1 + nu)

def logarithmic_creep_law(x,
                          A, tau0):
    return A * np.log(1 + x/tau0)

def modified_lomnitz(x,
                     epsilon0, a, q, alpha):
    return epsilon0 * (1 + q * ((1 + a * x) ** alpha - 1) / alpha)

x = np.linspace(0, 5, 500)

plt.figure(figsize=(10, 6), dpi=150)
plt.plot(x, exponential_retardation(x,
                                    A=1, tau=1),
                                    label="Exponential Retardation")
plt.plot(x, Andrade_creep_equation(x,
                                   epsilon0=0, beta=1, m=0.4),
                                   label="Andrade Creep")
plt.plot(x, Scott_Blair(x,
                        a=1, nu=0.5),
                        label="Scott-Blair")
plt.plot(x, logarithmic_creep_law(x,
                                  A=1, tau0=1),
                                  label="Logarithmic Creep")
plt.plot(x, modified_lomnitz(x,
                             epsilon0=1, a=1, q=1, alpha=1),
                             label="Modified Lomnitz")
plt.title("Transients Creep $\epsilon_t(t)$")
plt.xlabel("$t$")
plt.ylabel("Strain $\epsilon_t$")
plt.legend()
#plt.show()

if not os.path.exists('fig'):
    os.makedirs('fig')

plt.savefig('fig/transient_creep.png')
