import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.special import rel_entr
from scipy.optimize import minimize_scalar

import constriction


plt.close()

def kl(p,q):
    return sum(rel_entr(p,q))/np.log(2)

def exp(n,l):
    p = l * np.exp(-l*n)
    return p / sum(p)

n = np.arange(50)
a = 2.0
b = 0.1
p = n ** (a-1) * np.exp(-b*n) * b**a / (gamma(a))+0.001

p = p / sum(p)

# 1 - Graph source model
plt.figure(figsize=(5,2))
plt.plot(n,p, lw=2.0)
plt.ylim([0,max(p)*1.1])
plt.grid()
plt.xlabel("Symbol")
plt.ylabel("Probability")
plt.tight_layout()
plt.savefig("i1.png", dpi = 600)

"""
plt.figure()
plt.plot(n,p, lw=2.0)
plt.plot(n,exp(n,0.05),'--',label = "Exp. RV, $\lambda = 0.05$", lw=2.0)
plt.plot(n,np.ones(50)/50.0,'--',label = "Uniform RV", lw=2.0)
plt.ylim([0,max(exp(n,0.05))*1.1])
plt.grid()
plt.legend()
plt.xlabel("Symbol")
plt.ylabel("Probability")
plt.tight_layout()
"""

#plt.figure()
# Calculates an exponential distribution (truncated)
# with parameter 'l'
def exp(n,l):
    p = l * np.exp(-l*n)
    return p / sum(p)
# Find optimal exponential distribution
f = minimize_scalar(lambda x : kl(p,exp(n,x)))
l_optimal = f.x
l_divergence = f.fun
print("Exponential Divergence: {} using lambda = {}".format(l_divergence,l_optimal))

# Uniform distribution
p_uniform = np.ones(50) / 50.0
print("Uniform divergence: {}".format(kl(p,p_uniform)))

plt.figure(figsize=(5,2))
plt.plot(n,p, lw=2.0, label = "Source Model")
plt.plot(n,exp(n,l_optimal),'--',label = "Exponential Model", lw=2.0)
plt.ylim([0,max(exp(n,l_optimal))*1.1])
plt.grid()
plt.legend()
plt.xlabel("Symbol")
plt.ylabel("Probability")
plt.tight_layout()
plt.savefig("i2.png", dpi = 600)



# 3 - Test w/ constriction
pc = np.cumsum(p)

information_model = constriction.stream.model.Categorical(p)
approximate_model = constriction.stream.model.Categorical(exp(n,0.1))

N = 1000

def get_symbol():
    r = np.random.rand()
    for i in range(50):
        if pc[i] > r:
            return i
    return 49

approximate_size = []
size = []

Ls = [int(x) for x in np.linspace(100,5000,100)]
for L in Ls:
    symbols = np.array([get_symbol() for _ in range(L)], dtype=np.int32)
    coder = constriction.stream.stack.AnsCoder()
    coder.encode_reverse(symbols, information_model)
    size.append(coder.num_bits() + 32*50)

    coder2 = constriction.stream.stack.AnsCoder()
    coder2.encode_reverse(symbols, approximate_model)
    approximate_size.append(coder2.num_bits() + 32 + 8)

plt.figure(figsize=(5,3))
plt.plot(Ls, size, label = "Ideal Model")
plt.plot(Ls, approximate_size, label = "Approximate Model")
plt.ylabel("Bits")
plt.xlabel("Number of Symbols")
plt.legend(loc = "lower right")
plt.tight_layout()
plt.savefig("out.svg")