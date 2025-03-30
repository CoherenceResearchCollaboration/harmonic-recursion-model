from mpmath import mp, mpf, sqrt

# Set decimal precision for recursion
mp.dps = 100

# Constants for HRM
phi = (1 + sqrt(5)) / 2               # golden ratio
alpha = mpf('1') / 137                # fine-structure approx
M0 = mpf('1.6726219e-27')             # proton mass seed (kg)

