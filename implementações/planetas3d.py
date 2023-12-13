from vpython import *
import numpy as np

scene = canvas(title = "<h1>Simulação 3D do Sistema Solar</h1><br />", forward = vec(-0.5, -0.2, -1))

solRaio = 69550
mercurioRaio = 2440
venusRaio = 6052
terraRaio = 6371
marteRaio = 3386

solOrbitaRaio = 1.0
mercurioOrbitaRaio = 69.27e6
venusOrbitaRaio = 107.49e6
terraOrbitaRaio = 151.78e6
marteOrbitaRaio = 249.63e6

sol = sphere( radius = solRaio, texture = "https://i.imgur.com/XdRTvzj.jpg", emissive = True )
mercurio = sphere( radius = mercurioRaio, texture = "https://i.imgur.com/SLgVbwD.jpg", make_trail = True, trail_radius = mercurioRaio * 0.05 )
venus = sphere( radius = venusRaio, texture = "https://i.imgur.com/7VTEX2w.jpeg", make_trail = True, trail_color = color.white, trail_radius = 122 )
terra = sphere( radius = terraRaio, texture = textures.earth, make_trail = True, trail_color = color.white, trail_radius = 122 )
marte = sphere( radius = marteRaio, texture = "https://i.imgur.com/Mwsa16j.jpg", make_trail = True, trail_color = color.white, trail_radius = 122) 

sistema_solar = {'Sol': sol, 'Mercúrio': mercurio, 'Vênus': venus, 'Terra': terra, 'Marte': marte}

mercurioOrbitaTaxa = 88.0
venusOrbitaTaxa = 224.7
terraOrbitaTaxa = 365.3
marteOrbitaTaxa = 687.0

solEpsilon = radians(0.1265364)
mercurioEpslion = radians(0.0349066)
venusEpsilon = radians(0.0523599)
terraEpsilon = radians(0.4101524)
marteEpsilon = radians(0.43964844)

mercurioAngulo = 0
venusAngulo = 0
terraAngulo = 0
marteAngulo = 0

luzSol = local_light( pos = vec(0,0,0), color=color.white )

velocidadePrograma = 1.0

scene.pause() 

sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=45e6,shininess=0)

def camera_menu(m):
    if m.selected in sistema_solar:
        scene.camera.follow(sistema_solar[m.selected])

menu(choices=list(sistema_solar.keys()), bind=camera_menu, pos=scene.title_anchor) 

while (True):
 
    rate(150) 
   
    mercurio.pos = vec( mercurioOrbitaRaio/150 * cos(radians(mercurioAngulo)), 0, mercurioOrbitaRaio/150 * sin(radians(mercurioAngulo)) ) 
    venus.pos = vec( venusOrbitaRaio/150 * cos(radians(venusAngulo)), 0, venusOrbitaRaio/150 * sin(radians(venusAngulo)) ) 
    terra.pos = vec( terraOrbitaRaio/150 * cos(radians(terraAngulo)), 0, terraOrbitaRaio/150 * sin(radians(terraAngulo)) )
    marte.pos = vec( marteOrbitaRaio/150 * cos(radians(marteAngulo)), 0, marteOrbitaRaio/150 * sin(radians(marteAngulo)) ) 
    
    mercurioAngulo -= 1/mercurioOrbitaTaxa * velocidadePrograma
    venusAngulo -= 1/venusOrbitaTaxa * velocidadePrograma
    terraAngulo -= 1/terraOrbitaTaxa * velocidadePrograma
    marteAngulo -= 1/marteOrbitaTaxa * velocidadePrograma
    
    sol.rotate (angle = solEpsilon, axis = vector(np.sin(solEpsilon), np.cos(solEpsilon), 0))
    
    mercurio.rotate (angle = mercurioEpslion, axis = vector(np.sin(mercurioEpslion), np.cos(mercurioEpslion), 0))
    venus.rotate (angle = venusEpsilon, axis = vector(np.sin(venusEpsilon), np.cos(venusEpsilon), 0))
    terra.rotate (angle = terraEpsilon, axis = vector(np.sin(terraEpsilon), np.cos(terraEpsilon), 0))
    marte.rotate (angle = marteEpsilon, axis = vector(np.sin(marteEpsilon), np.cos(marteEpsilon), 0))