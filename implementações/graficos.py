import tkinter as tk
from tkinter import ttk
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
import numpy as np

class PhysicsGraphApp:

    def __init__(self, root):
        pass

        self.root = root
        self.root.title("Plotar Gráficos Cinemática")

        tab_control = ttk.Notebook(self.root)

        mru_tab = ttk.Frame(tab_control)
        tab_control.add(mru_tab, text='MRU')
        self.setup_mru_tab(mru_tab)

        mruv_tab = ttk.Frame(tab_control)
        tab_control.add(mruv_tab, text='MRUV')
        self.setup_mruv_tab(mruv_tab)

        mcu_tab = ttk.Frame(tab_control)
        tab_control.add(mcu_tab, text='MCU')
        self.setup_mcu_tab(mcu_tab)

        mcuv_tab = ttk.Frame(tab_control)
        tab_control.add(mcuv_tab, text='MCUV')
        self.setup_mcuv_tab(mcuv_tab)

        tab_control.pack(expand=1, fill='both')


    def setup_mru_tab(self, tab):

        velocidade_label = ttk.Label(tab, text="Digite a velocidade do MRU:")
        velocidade_label.pack()
        velocidade_entry = ttk.Entry(tab)
        velocidade_entry.pack()

        inicial_label = ttk.Label(tab, text="Digite a posição inicial:")
        inicial_label.pack()
        inicial_entry = ttk.Entry(tab)
        inicial_entry.pack()

        plot_button = ttk.Button(tab, text="Plotar Gráfico", command=lambda: self.plot_mru(float(velocidade_entry.get()),np.arange(0.0, 51.0, 0.1).tolist(), float(inicial_entry.get())))
        plot_button.pack()

    def setup_mruv_tab(self, tab):

        velocidade_inicial_label = ttk.Label(tab, text="Digite a velocidade inicial:")
        velocidade_inicial_label.pack()
        velocidade_inicial_entry = ttk.Entry(tab)
        velocidade_inicial_entry.pack()

        aceleracao_label = ttk.Label(tab, text="Digite a aceleração:")
        aceleracao_label.pack()
        aceleracao_entry = ttk.Entry(tab)
        aceleracao_entry.pack()

        inicial_label = ttk.Label(tab, text="Digite a posição inicial:")
        inicial_label.pack()
        inicial_entry = ttk.Entry(tab)
        inicial_entry.pack()

        plot_button = ttk.Button(tab, text="Plotar Gráfico", command=lambda: self.plot_mruv(float(velocidade_inicial_entry.get()), float(aceleracao_entry.get()), np.arange(0.0, 51.0, 0.1).tolist(), float(inicial_entry.get())))
        plot_button.pack()

    def setup_mcu_tab(self, tab):

        velocidade_linear_label = ttk.Label(tab, text= "Digite a velocidade linear do MCU:")
        velocidade_linear_label.pack()
        velocidade_linear_entry = ttk.Entry(tab)
        velocidade_linear_entry.pack()

        raio_label = ttk.Label(tab, text="Digite o raio do MCU:")
        raio_label.pack()
        raio_entry = ttk.Entry(tab)
        raio_entry.pack()

        plot_button = ttk.Button(tab, text="Plotar Gráfico", command=lambda: self.plot_mcu(float(velocidade_linear_entry.get()), float(raio_entry.get()), np.arange(0.0, 51.0, 0.1).tolist()))
        plot_button.pack()

    def setup_mcuv_tab(self, tab):

        velocidade_angular_inicial_label = ttk.Label(tab, text="Digite a velocidade linear inicial do MCUV:")
        velocidade_angular_inicial_label.pack()
        velocidade_angular_inicial_entry = ttk.Entry(tab)
        velocidade_angular_inicial_entry.pack()

        aceleracao_angular_label = ttk.Label(tab, text="Digite a aceleração linear do MCUV:")
        aceleracao_angular_label.pack()
        aceleracao_angular_entry = ttk.Entry(tab)
        aceleracao_angular_entry.pack()

        raio_label = ttk.Label(tab, text="Digite o raio do MCUV:")
        raio_label.pack()
        raio_entry = ttk.Entry(tab)
        raio_entry.pack()

        plot_button = ttk.Button(tab, text="Plotar Gráfico", command=lambda: self.plot_mcuv(float(velocidade_angular_inicial_entry.get()), float(aceleracao_angular_entry.get()), float(raio_entry.get()), np.arange(0.0, 51.0, 0.1).tolist()))
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
