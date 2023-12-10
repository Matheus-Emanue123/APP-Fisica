from vpython import *
import random
import time
import sys

def deslocar(corpo):
    global dt
    queda = True
    p = corpo.traj.point(corpo.traj.npoints - 1)["pos"]
    corpo.pos += dt*corpo.v + dt**2*corpo.a/2.
    if corpo.v.y < 0 and corpo.pos.y < corpo.radius:
        if p.y != corpo.pos.y:
            f = (p.y - corpo.radius)/(p.y - corpo.pos.y)
            corpo.pos -= (1 - f)*(corpo.pos - p)
            corpo.v += f*dt*corpo.a
            corpo.t += f*dt
        queda = False
    else:
        corpo.t += dt 
        corpo.v += dt*corpo.a
    corpo.traj.append(pos = vec(corpo.pos))
    corpo.d += mag(corpo.pos - p)
    return queda

def resultados(corpo):
    p0 = corpo.traj.point(0)["pos"]
    alcance = corpo.pos.x - p0.x
    velocidade = corpo.d / corpo.t
    scene.caption += "<b>" + corpo.legenda + "</b>\n"
    time.sleep(0.5)
    scene.caption += "Tempo total = {:.2f} s\n".format(corpo.t)
    time.sleep(0.5)
    scene.caption += "Alcance horizontal = {:.2f} m\n".format(alcance)
    time.sleep(0.5)
    scene.caption += "Distância percorrida = {:.2f} m\n".format(corpo.d)
    time.sleep(0.5)
    scene.caption += "Velocidade média = {:.2f} m/s\n".format(velocidade)
    time.sleep(0.5)
    scene.caption += "Altura máxima = {:.2f} m\n\n".format(corpo.alt)
    return 

def projetar(corpo, vel, ang, leg):
    corpo.v = vel*vec(cos(ang*pi/180.), sin(ang*pi/180.), 0)
    corpo.t = corpo.d = 0
    corpo.legenda = leg 
    corpo.traj = curve(pos = vec(corpo.pos),color = corpo.color) 
    corpo.alt = (vel**2)*(sin(ang*pi/180.)**2) / (2*9.8)

scene = canvas(title = "<h1>Simulação 3D de Lançamento Oblíquo</h1>", forward = vec(-0.5, -0.2, -1))
scene.caption = ""
a = 47.
dt = 0.01
g = vec(0, -9.8, 0)
q1 = True


solo = box(pos = vec(0, -0.1, 0), size = vec(60 , 0.2, 10),texture = textures.metal)

while True:

    cont = 0
    
    vel = float(input('Velocidade:'))
    ang = float(input('Ângulo:'))

    color = vec(random.random(), random.random(), random.random())

    bola = sphere(pos = vec(-28, 0.2, 1), radius = 0.2, color = color)

    bola.t = 0
    bola.d = 0

    cont += 1
    projetar(bola, vel, ang, "Dados da simulação:")

    bola.a = g

    q1 = True 
    
    while q1:
        rate(100)
        if q1: 
            q1 = deslocar(bola)
            
    resultados(bola)

    resposta = input('Deseja executar a simulação novamente? (s/n): ')
    if resposta.lower() in ['n', 'nao', 'não']:
        break