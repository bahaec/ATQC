import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from scipy.linalg import sqrtm, expm
PI = np.pi

# Embedding H into a unitary: Block encoding
def block_encoding(H):
    n = len(H[0])
    I = np.eye(n)
    sqrt_I_minus_H2 = sqrtm(I - (H @ H))

    row1 = np.hstack([H, sqrt_I_minus_H2])
    row2 = np.hstack([sqrt_I_minus_H2, -H])
    U = np.vstack([row1, row2])
    
    return U

# projector-controlled phase shift
def PI_phi(phi,n):
    I_n = np.eye(n)
    Pi = np.kron(np.array([[1, 0], [0, 0]]), I_n)
    # Pi = np.array([[1, 0], [0, 0]])  # Π = ∣0⟩⟨0∣
    operator = 2 * Pi - np.eye(2 * n)
    return expm(1j * phi * operator) # exp(2iφΠ)

# QEVT Sequence
def QEVT(H, phi):
    n = len(H[0])
    d = len(phi)
    
    U = block_encoding(H)
    U_dagger = U.conj().T
    
    U_phi = np.eye(2 * n, dtype=complex)
    
    if d % 2 == 0: #first case, even d
        k = 0
        while k < d:
            U_phi = U_phi @ PI_phi(phi[k],n) @ U_dagger @ PI_phi(phi[k+1],n) @ U
            k+=2
    else: #second case, odd d
        U_phi = PI_phi(phi[0],n) @ U
        k = 1
        while k < d:
            U_phi = U_phi @ PI_phi(phi[k],n) @ U_dagger @ PI_phi(phi[k+1],n) @ U
            k+=2
    
    Poly_H = U_phi[:n, :n]
    
    return Poly_H

H = np.array([[0.5, 0.3],
              [0.3, -0.2]])

phi = [0,0,0]

Poly_H = QEVT(H, phi)

eigvals = np.linalg.eigvalsh(H)
transformed = np.linalg.eigvalsh(Poly_H)
print(Poly_H)
print("eigenvalues:", eigvals)
print("QEVT output:", transformed)