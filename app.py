import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation

class PhysicsGraphApp:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Aplicativo de Gráficos de Física")
        self.root.configure(bg='white') 

        self.label = ttk.Label(root, text="Escolha o tipo de movimento:")
        self.label.pack()

        self.options = ["MRU", "MRUV", "MCU", "MCUV"]
        self.choice = tk.StringVar()
        self.choice.set(self.options[0])

        self.option_menu = ttk.OptionMenu(root, self.choice, *self.options)
        self.option_menu.pack()

        self.button = ttk.Button(root, text="Abrir", command=self.open_graph_window, style="TButton")
        self.button.pack()


    def open_graph_window(self):
        choice = self.choice.get()
        if choice == "MRU":
            self.open_mru_window()
        elif choice == "MRUV":
            self.open_mruv_window()
        elif choice == "MCU":
            self.open_mcu_window()
        elif choice == "MCUV":
            self.open_mcuv_window()

    def open_mru_window(self):

        mru_window = tk.Toplevel(self.root)
        mru_window.title("MRU")

        velocidade_label = ttk.Label(mru_window, text="Digite a velocidade do MRU:")
        velocidade_label.pack()
        velocidade_entry = ttk.Entry(mru_window)
        velocidade_entry.pack()


        inicial_label = ttk.Label(mru_window, text="Digite a posição inicial:")
        inicial_label.pack()
        inicial_entry = ttk.Entry(mru_window)
        inicial_entry.pack()

        plot_button = ttk.Button(mru_window, text="Plotar Gráfico", command=lambda: self.plot_mru(float(velocidade_entry.get()), np.arange(1.0, 51.0, 0.1).tolist(), float(inicial_entry.get())))
        plot_button.pack()

    def open_mruv_window(self):

        mruv_window = tk.Toplevel(self.root)
        mruv_window.title("MRUV")

        velocidade_inicial_label = ttk.Label(mruv_window, text="Digite a velocidade inicial do MRUV:")
        velocidade_inicial_label.pack()
        velocidade_inicial_entry = ttk.Entry(mruv_window)
        velocidade_inicial_entry.pack()

        aceleracao_label = ttk.Label(mruv_window, text="Digite a aceleração do MRUV:")
        aceleracao_label.pack()
        aceleracao_entry = ttk.Entry(mruv_window)
        aceleracao_entry.pack()

        inicial_label = ttk.Label(mruv_window, text="Digite a posição inicial:")
        inicial_label.pack()
        inicial_entry = ttk.Entry(mruv_window)
        inicial_entry.pack()


        plot_button = ttk.Button(mruv_window, text="Plotar Gráfico", command=lambda: self.plot_mruv(float(velocidade_inicial_entry.get()), float(aceleracao_entry.get()), np.arange(1.0, 51.0, 0.1).tolist(), float(inicial_entry.get())))
        plot_button.pack()

    def open_mcu_window(self):
        mcu_window = tk.Toplevel(self.root)
        mcu_window.title("MCU")

        velocidade_linear_label = ttk.Label(mcu_window, text= "Digite a velocidade linear do MCU:")
        velocidade_linear_label.pack()
        velocidade_linear_entry = ttk.Entry(mcu_window)
        velocidade_linear_entry.pack()

        raio_label = ttk.Label(mcu_window, text="Digite o raio do MCU:")
        raio_label.pack()
        raio_entry = ttk.Entry(mcu_window)
        raio_entry.pack()

        plot_button = ttk.Button(mcu_window, text="Plotar Gráfico", command=lambda: self.plot_mcu(float(velocidade_linear_entry.get()), float(raio_entry.get()), np.arange(1.0, 51.0, 0.1).tolist()))
        plot_button.pack()

    def open_mcuv_window(self):
        mcuv_window = tk.Toplevel(self.root)
        mcuv_window.title("MCUV")

        velocidade_angular_inicial_label = ttk.Label(mcuv_window, text="Digite a velocidade linear inicial do MCUV:")
        velocidade_angular_inicial_label.pack()
        velocidade_angular_inicial_entry = ttk.Entry(mcuv_window)
        velocidade_angular_inicial_entry.pack()

        aceleracao_angular_label = ttk.Label(mcuv_window, text="Digite a aceleração linear do MCUV:")
        aceleracao_angular_label.pack()
        aceleracao_angular_entry = ttk.Entry(mcuv_window)
        aceleracao_angular_entry.pack()

        raio_label = ttk.Label(mcuv_window, text="Digite o raio do MCUV:")
        raio_label.pack()
        raio_entry = ttk.Entry(mcuv_window)
        raio_entry.pack()

        plot_button = ttk.Button(mcuv_window, text="Plotar Gráfico", command=lambda: self.plot_mcuv(float(velocidade_angular_inicial_entry.get()), float(aceleracao_angular_entry.get()), float(raio_entry.get()), np.arange(1.0, 51.0, 0.1).tolist()))
        plot_button.pack()

    
    def plot_mru(self, velocidade, tempo, inicial):
        posicoes = [inicial + velocidade * t for t in tempo]
        plt.plot(tempo, posicoes, label="MRU")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Posição (m)")
        plt.title("Gráfico de Movimento Retilíneo Uniforme")
        plt.legend()
        plt.show()

    def plot_mruv(self, velocidade_inicial, aceleracao, tempo, inicial):
        posicoes = [inicial + velocidade_inicial * t + 0.5 * aceleracao * t**2 for t in tempo]
        velocidades = [velocidade_inicial + aceleracao * t for t in tempo]
    
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.plot(tempo, posicoes, label="MRUV")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Posição (m)")
        plt.title("Gráfico de Movimento Retilíneo Uniformemente Variado")
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(tempo, velocidades, label="MRUV")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade (m/s)")
        plt.title("Gráfico de Velocidade do Movimento Retilíneo Uniformemente Variado")
        plt.legend()

        plt.tight_layout()
        plt.show()

    def plot_mcu(self, velocidade_linear, raio, tempo):
        velocidade_angular = velocidade_linear / raio
        posicoes_angulares = [velocidade_angular * t for t in tempo]
        plt.plot(tempo, posicoes_angulares, label="MCU")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Ângulo (rad)")
        plt.title("Gráfico de Movimento Circular Uniforme")
        plt.legend()
        plt.show()

    def plot_mcuv(self, velocidade_angular_inicial, aceleracao_angular, raio, tempo):
        posicoes_angulares = [velocidade_angular_inicial * t + 0.5 * aceleracao_angular * t**2 for t in tempo]
        velocidades_angulares = [velocidade_angular_inicial + aceleracao_angular * t for t in tempo]

        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.plot(tempo, posicoes_angulares, label="MCUV")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Ângulo (rad)")
        plt.title("Gráfico de Movimento Circular Uniformemente Variado")
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.plot(tempo, velocidades_angulares, label="MCUV")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade Angular (rad/s)")
        plt.title("Gráfico de Velocidade Angular do Movimento Circular Uniformemente Variado")
        plt.legend()

        plt.tight_layout()
        plt.show()

root = tk.Tk()
app = PhysicsGraphApp(root)
root.mainloop()
