import os
import tkinter as tk

def run_file1():
    os.system('python implementações/graficos.py')

def run_file2():
    os.system('python implementações/teste_obliquo.py')

def run_file3():
    os.system('python implementações/planetas.py')

def run_file4():
    os.system('python implementações/planetas3d.py')

root = tk.Tk()

button1 = tk.Button(root, text="Plotar Gráficos Cinemática", command=run_file1)
button1.pack()

button2 = tk.Button(root, text="Simulação 3D Lançamento Oblíquo", command=run_file2)
button2.pack()

button3 = tk.Button(root, text="Simulação 2D Sistema Solar", command=run_file3)
button3.pack()

button4 = tk.Button(root, text="Simulação 3D Sistema Solar", command=run_file4)
button4.pack()

root.mainloop()