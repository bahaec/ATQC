import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk

PI = np.pi
    
x = []
y1 = []
y2 = []

root = tk.Tk()
root.title("QSP Simulation")
tk.Label(root, text="Choose a QSP sequence to simulate:", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="BB1 Sequence", command=bb1plot, width=25).pack(pady=5)
tk.Button(root, text="1st Chebyshev Polynomial", command=chebychev_1plot, width=25).pack(pady=5)
tk.Button(root, text="2nd Chebyshev Polynomial", command=chebychev_2plot, width=25).pack(pady=5)
tk.Button(root, text="3rd Chebyshev Polynomial", command=chebychev_3plot, width=25).pack(pady=5)
root.mainloop()