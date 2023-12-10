from vpython import *

canvas(align="left", width=700, height=400)
scene.autoscale = False

g1 = graph(title="Energia vs Deslocamento", xtitle="deslocamento", ytitle="Energia", align="left")
cinetica_c = gcurve(color=color.red, label="Cinetica", graph=g1)
potencial_c = gcurve(color=color.blue, label="Potencial", graph=g1)

L = 8
mola = helix(pos=vec(0, 0, 0), radius=.6, length=L, axis=vec(1, 0, 0),
               coils=22, k=1, amplitude=2)

bloco = box(pos=mola.pos + vec(mola.length, 0, 0), size=vec(2, 2, 2), mass=0.1, texture = textures.wood)

parede = box(pos=mola.pos, size=vec(.5, 3, 4), texture = textures.metal)

surface = box(pos=vec(mola.length / 2, -bloco.height / 2 - .25, 0), size=vec(L + 10, .5, 4), texture = textures.metal)

def k_adjust(k):
    mola.k = k_slider.value
    k_cap.text = str(k_slider.value) + " N/m\n"
    potencial_c.delete()
    cinetica_c.delete()

wtext(text="\n\nConstante Elástica")

k_slider = slider(min=0.2, max=10, value=1, bind=k_adjust)
k_cap = wtext(text=str(k_slider.value) + " N/m\n")

dt = 0.01
t = 0
while True:
    
    rate(100)
    A = mola.amplitude
    w0 = sqrt(mola.k / bloco.mass)
    T = 2 * pi / w0
    xt = A * cos(w0 * t)
    bloco.pos.x = L + xt
    mola.length = bloco.pos.x
    max_Energy = (1 / 2) * mola.k * (A / 100) ** 2
    potential = (1 / 2) * mola.k * (xt / 100) ** 2
    kinetic = max_Energy - potential

    cinetica_c.plot(xt, kinetic)
    potencial_c.plot(xt, potential)

    t += dt