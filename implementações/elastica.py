from vpython import *

k = float(input("Constante elástica: "))

wall = box(pos=vector(0,1,0), size=vector(0.2,3,2), color=color.green)
floor = box(pos=vector(6,-0.6,0), size=vector(14,0.2,4), color=color.green)
Mass = box(pos=vector(12,0,0), velocity=vector(0,0,0), size=vector(1,1,1), color=color.blue)
pivot = vector(0,0,0)
spring = helix(pos=pivot, axis=Mass.pos-pivot, radius=0.4, constant = k, thickness=0.1, coils=20, color=color.red)
eq = vector(9,0,0)
t = 0
dt = 0.01

drag_object = None
drag_pos = vector(0,0,0)

def drag(event):
    global drag_object, drag_pos
    if event.press == 'left':
        if event.pick == Mass:
            drag_object = event.pick
            drag_pos = event.pickpos
    elif event.release == 'left':
        drag_object = None

scene.bind('mousedown', drag)
scene.bind('mouseup', drag)

while (t<50):
    rate(100)
    if drag_object:
        new_pos = scene.mouse.project(normal=(0,0,1), d=drag_pos.z)
        if new_pos != None:
            drag_object.pos.x = new_pos.x
    else:
        acc = (eq-Mass.pos)*(spring.constant/Mass.mass)
        Mass.velocity = Mass.velocity + acc*dt
        Mass.pos = Mass.pos + Mass.velocity*dt
    spring.axis = Mass.pos - spring.pos
    t += dt