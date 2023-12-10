import os
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import subprocess

def run_file1():
    subprocess.Popen(['python', 'implementações/graficos.py'])

def run_file2():
    subprocess.Popen(['python', 'implementações/teste_obliquo.py'])

def run_file3():
    subprocess.Popen(['python', 'implementações/planetas.py'])

def run_file4():
    subprocess.Popen(['python', 'implementações/planetas3d.py'])

def run_file5():
    subprocess.Popen(['python', 'implementações/elastica.py'])

root = tk.Tk()
root.configure(bg='white')

customFont = tkFont.Font(family="Helvetica", size=12)

style = ttk.Style()
style.configure("BW.TButton", foreground="gray", background="white", font=customFont, cursor="hand2")

button1 = ttk.Button(root, text="Plotar Gráficos Cinemática", command=run_file1, style="BW.TButton")
button1.pack(pady=10)

button2 = ttk.Button(root, text="Simulação 3D Lançamento Oblíquo", command=run_file2, style="BW.TButton")
button2.pack(pady=10)

button3 = ttk.Button(root, text="Simulação 2D Sistema Solar", command=run_file3, style="BW.TButton")
button3.pack(pady=10)

button4 = ttk.Button(root, text="Simulação 3D Sistema Solar", command=run_file4, style="BW.TButton")
button4.pack(pady=10)

button5 = ttk.Button(root, text="Simulação 3D Sistema Massa-MOla", command=run_file4, style="BW.TButton")
button5.pack(pady=10)

root.mainloop()