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

def run_splash():
    global splash_x, splash_y, window_width, window_height, win

    animation = pyglet.image.load_animation('gif/loading.gif')
    sprite = pyglet.sprite.Sprite(animation)

    window_width = sprite.width
    window_height = sprite.height

    win = pyglet.window.Window(width=window_width, height=window_height)
    win.set_caption('Loading...')

    splash_x = (win.screen.width - win.width) // 2
    splash_y = (win.screen.height - win.height) // 2
    win.set_location(splash_x, splash_y)

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()

    pyglet.app.run()

root = tk.Tk()
root.configure(bg='white')
root.title("Trabalho de Física")

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

root.withdraw()

# Run the splash screen in a separate thread
threading.Thread(target=run_splash).start()

def show_main_window():
    win.close()  # Close the pyglet window
    root.geometry(f"{window_width}x{window_height}+{splash_x}+{splash_y}")  # Set the size and position of the tkinter window
    root.deiconify()

root.after(4000, show_main_window)  # Show the main window after 4 seconds

root.mainloop()