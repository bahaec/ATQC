import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk

PI = np.pi

# Signal rotation opreator
def W(a):
    ''' x rotation by angle -2*acos(a) '''
    return np.array([[a, 1j*np.sqrt(1-a**2)], 
                     [1j*np.sqrt(1-a**2), a]])

# Signal prcessing rotation operator
def S(phi):
    ''' z rotation by angle -2*phi '''
    return np.array([[np.exp(1j*phi), 0], 
                     [0, np.exp(-1j*phi)]])

# QSP operator sequence
def U(a : float, phi : list):
    res = S(phi[0])
    for i in range(1, len(phi)):
        res = res @ W(a) @ S(phi[i])
    return res

# Probability of a |0⟩ qubit input staying unchanged
def prob(u):
    return np.abs(u[0][0])**2

def bb1_poly(theta):
    return 1 - (5/8) * (theta/2)**6
    
def chebychev_2(a):
    return 2*a*a - 1

def chebychev_3(a):
    return 4*(a**3) - 3*a   

def bb1plot():
    x = []
    y1 = []
    y2 = []
    
    n = 0.5 * np.arccos(-1/4)
    BB1 = [PI/2, -n, 2*n, 0, -2*n, n]
    
    for i in range(-30, 30):
        theta = i / 10
        a = np.cos(theta / 2)
        x.append(theta)
        u = U(a, BB1)
        y1.append(prob(u))
        y2.append(bb1_poly(theta))
    
    plt.figure()
    plt.title("BB1 Sequence")
    plt.plot(x, y1, label="QSP result")
    plt.plot(x, y2, label="BB1 polynomial approx.")
    plt.xlabel("theta")
    plt.legend()
    plt.ylim(0,1)
    plt.show()
    


def chebychev_1plot():
    x = []
    y1 = []
    y2 = []
    
    for i in range(-10, 10):
        a = i / 10
        x.append(a)
        u = U(a, [0, 0])
        y1.append(np.real(u[0][0]))
        y2.append(a)
    
    plt.figure()
    plt.plot(x, y1, label="QSP")
    plt.plot(x, y2, label="Chebyshev 2")
    plt.xlabel("a")
    plt.legend()
    plt.title("1st Chebyshev Polynomial")
    plt.show()
    
def chebychev_2plot():
    x = []
    y1 = []
    y2 = []
    
    for i in range(-10, 10):
        a = i / 10
        x.append(a)
        u = U(a, [0, 0, 0])
        y1.append(np.real(u[0][0]))
        y2.append(chebychev_2(a))
    
    plt.figure()
    plt.plot(x, y1, label="QSP")
    plt.plot(x, y2, label="Chebyshev 2")
    plt.xlabel("a")
    plt.legend()
    plt.title("2nd Chebyshev Polynomial")
    plt.show()

def chebychev_3plot():
    x = []
    y1 = []
    y2 = []
    
    for i in range(-10, 10):
        a = i / 10
        x.append(a)
        u = U(a, [0, 0, 0, 0])
        y1.append(np.real(u[0][0]))
        y2.append(chebychev_3(a))
    
    plt.figure()
    plt.plot(x, y1, label="QSP")
    plt.plot(x, y2, label="Chebyshev 3")
    plt.xlabel("a")
    plt.legend()
    plt.title("3rd Chebyshev Polynomial")
    plt.show()
    
def cos_plot():
    x = []
    y1 = []
    y2 = []
    
    for i in range(-100, 100):
        a = i / 100
        x.append(a)
        phi =  [-1.70932079,-0.05312746, 2.12066859,-0.83307065,-0.50074601, 0.40728859, 0.32838472, 0.9142489,-2.81320793, 0.40728859,-0.50074601, 2.30852201,-1.02092406,-0.05312746, 3.003068]
        u = U(a, phi)
        y1.append(np.real(u[0][0]))
        y2.append(np.cos(5*a))
    
    plt.figure()
    plt.plot(x, y1, label="QSP")
    plt.xlabel("a")
    plt.legend()
    plt.title("Polynomial Approximation to the cosine function")
    plt.show()
    
def thresh_plot():
    x = []
    y1 = []
    y2 = []
    
    for i in range(-100, 100):
        a = i / 100
        x.append(a)
        phi =  [0.73930816,-0.69010006,-0.63972139,-0.47754554,0.81797049, 0.09205065,-0.87660105, 0.13460844,0.23892207, 1.32216648,-2.90267058, 0.13460844,2.2649916,0.09205065,-2.32362216, 2.66404712,-0.63972139,-0.69010006, 2.31010449]
        u = U(a, phi)
        y1.append(np.real(u[0][0]))
        if (a<-0.5 or a>0.5): y2.append(0)
        else: y2.append(0.85)
        
    
    plt.figure()
    plt.plot(x, y1, label="QSP")
    plt.plot(x, y2, label="Target")
    plt.xlabel("a")
    plt.legend()
    plt.title("Polynomial Approximation to the threshhold function")
    plt.show()

root = tk.Tk()
root.title("QSP Simulation")
tk.Label(root, text="Choose a QSP sequence to simulate:", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="BB1 Sequence", command=bb1plot, width=25).pack(pady=5)
tk.Button(root, text="1st Chebyshev Polynomial", command=chebychev_1plot, width=25).pack(pady=5)
tk.Button(root, text="2nd Chebyshev Polynomial", command=chebychev_2plot, width=25).pack(pady=5)
tk.Button(root, text="3rd Chebyshev Polynomial", command=chebychev_3plot, width=25).pack(pady=5)
tk.Button(root, text="Cosine Approximation", command=cos_plot, width=25).pack(pady=5)
tk.Button(root, text="Threshold Approximation", command=thresh_plot, width=25).pack(pady=5)
root.mainloop()