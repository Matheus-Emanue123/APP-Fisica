import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import subprocess
import threading
import pyglet

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

def mostrar_creditos():
    
    for widget in root.winfo_children():
        widget.destroy()

    nomes = "Feito por:\n\nGuilherme Alvarenga de Azevedo\n\nMaíra Beatriz de Almeida Lacerda\n\nMaria Eduarda Teixeira Sousa\n\nMatheus Emanuel da Silva\n\nSamuel Silva Gomes"
    creditos_label = tk.Label(root, text=nomes, font=customFont, bg='white', justify='center', anchor='center')
    creditos_label.place(relx=0.5, rely=0.5, anchor='center')

    back_button = ttk.Button(root, text="Voltar", command=show_main_menu, style="BW.TButton")
    back_button.pack(side='bottom', pady=10)

def show_main_menu():
   
    for widget in root.winfo_children():
        widget.destroy()    

def run_splash():
    global splash_x, splash_y, window_width, window_height, win

    animation = pyglet.image.load_animation('gif/loading.gif')
    sprite = pyglet.sprite.Sprite(animation)

    window_width = sprite.width
    window_height = sprite.height

    win = pyglet.window.Window(width=window_width, height=window_height)
    win.set_caption('Carregando...')
    icon = pyglet.image.load('imagens/icon.jpg')
    win.set_icon(icon)

    splash_x = (win.screen.width - win.width) // 2
    splash_y = (win.screen.height - win.height) // 2
    win.set_location(splash_x, splash_y)

    def fechar_janela(dt):
        win.close()
        mostar_principal()

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()

    pyglet.clock.schedule_once(fechar_janela, 4)

    pyglet.app.run()

root = tk.Tk()
root.configure(bg='white')
root.title("Trabalho de Fundamentos da Mecânica Clássica - 2023/2")

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

button5 = ttk.Button(root, text="Simulação 3D Sistema Massa-Mola", command=run_file5, style="BW.TButton")
button5.pack(pady=10)

button6 = ttk.Button(root, text="Sair", command=root.destroy, style="BW.TButton")
button6.pack(side='bottom',pady=10)

creditos_button = ttk.Button(root, text="Creditos", command=mostrar_creditos, style="BW.TButton")
creditos_button.pack(side='bottom', pady=10)

root.withdraw()

threading.Thread(target=run_splash).start()

def mostar_principal():
    win.close()  
    root.geometry(f"{window_width}x{window_height}+{splash_x}+{splash_y}")
    root.deiconify()

root.mainloop()