from vpython import *

scene = canvas(align="center", width=700, height=400, title = "<h1>Simulação 3D de Sistema Massa-Mola</h1>")
scene.autoscale = False

g1 = graph(title="Energia vs Deslocamento", xtitle="Deslocamento (m)", ytitle="Energia (J)")
cinetica_c = gcurve(color=color.red, label="Cinética", graph=g1)
potencial_c = gcurve(color=color.blue, label="Potencial Elástica", graph=g1)

L = 8
mola = helix(pos=vec(0, 0, 0), radius=.6, length=L, axis=vec(1, 0, 0),
               coils=22, k=1, amplitude=2)

bloco = box(pos=mola.pos + vec(mola.length, 0, 0), size=vec(2, 2, 2), mass=0.1, texture = textures.wood)

parede = box(pos=mola.pos, size=vec(.5, 3, 4), texture = textures.metal)

superficie = box(pos=vec(mola.length, -bloco.height / 2 - .25, 0), size=vec(L + 10, .5, 4), texture = textures.metal)

def k_adjust(k):
    mola.k = k_slider.value
    k_cap.text = str(k_slider.value) + " N/m\n"
    potencial_c.delete()
    cinetica_c.delete()

textoPosicao = wtext(text="")
textoVelocidade = wtext(text="")
textoEnergiaCinetica = wtext(text="")
textoEnergiaPotencial = wtext(text="")
textoEnergiaTotalEMassa = wtext(text="")

wtext(text="\n\nConstante Elástica")

k_slider = slider(min=.2, max=10, value=1, step=.2, bind=k_adjust)
k_cap = wtext(text=str(k_slider.value) + " N/m\n")

rodando = True
def Rodar(b):
    global rodando, ultimo_dt, dt
    rodando = not rodando
    if rodando:
        b.text = "Pausar"
        dt = ultimo_dt
    else: 
        b.text = "Rodar"
        ultimo_dt = dt
        dt = 0
    return

dt = 0.01
t = 0

button(text="Pausar", pos=scene.title_anchor, bind=Rodar)

scene.camera.follow(bloco)

while True:
    
    rate(100)
    A = mola.amplitude
    w0 = sqrt(mola.k / bloco.mass)
    T = 2 * pi / w0
    xt = A * cos(w0 * t)
    bloco.pos.x = L + xt
    mola.length = bloco.pos.x
    max_Energy = (1 / 2) * mola.k * (A) ** 2
    potential = (1 / 2) * mola.k * (xt) ** 2
    kinetic = max_Energy - potential

    cinetica_c.plot(xt, kinetic)
    potencial_c.plot(xt, potential)

    textoPosicao.text = "\nPosição: {:.2f} m".format(xt)

    velocidade = sqrt(2 * kinetic / bloco.mass)
    textoVelocidade.text = "\nVelocidade: {:.2f} m/s".format(velocidade)

    textoEnergiaTotalEMassa.text = "\nEnergia Total: {:.2f} J".format(max_Energy) + "  e  Massa: {:.2f} kg".format(bloco.mass)

    textoEnergiaCinetica.text = "\nEnergia Cinética: {:.2f} J".format(kinetic)

    textoEnergiaPotencial.text = "\nEnergia Potencial Elástica: {:.2f} J".format(potential)

    t += dt