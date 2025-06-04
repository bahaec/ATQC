import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk

PI = np.pi

def test():
    return

x = []
y1 = []
y2 = []

root = tk.Tk()
root.title("QEVT Simulation")
tk.Label(root, text="Choose a QEVT simulation:", font=("Arial", 14)).pack(pady=10)
tk.Button(root, text="test", command=test, width=25).pack(pady=5)
root.mainloop()