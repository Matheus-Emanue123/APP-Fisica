from vpython import *
import numpy as np

sunRadius = 69550
mercuryRadius = 2440
venusRadius = 6052
earthRadius = 6371
marsRadius = 3386

sunOrbitRadius = 1.0
mercuryOrbitRadius = 69.27e6
venusOrbitRadius = 107.49e6
earthOrbitRadius = 151.78e6
marsOrbitRadius = 249.63e6

sun = sphere( radius = sunRadius, texture = "https://i.imgur.com/XdRTvzj.jpg", emissive = True )
mercury = sphere( radius = mercuryRadius, texture = "https://i.imgur.com/SLgVbwD.jpg", make_trail = True, trail_radius = mercuryRadius * 0.05 )
venus = sphere( radius = venusRadius, texture = "https://i.imgur.com/7VTEX2w.jpeg", make_trail = True, trail_color = color.white, trail_radius = 122 )
earth = sphere( radius = earthRadius, texture = textures.earth, make_trail = True, trail_color = color.white, trail_radius = 122 )
mars = sphere( radius = marsRadius, texture = "https://i.imgur.com/Mwsa16j.jpg", make_trail = True, trail_color = color.white, trail_radius = 122) 

solar_system = {'Sun': sun, 'Mercury': mercury, 'Venus': venus, 'Earth': earth, 'Mars': mars}

mercuryOrbitRate = 88.0
venusOrbitRate = 224.7
earthOrbitRate = 365.3
marsOrbitRate = 687.0

sunEpsilon = radians(0.1265364)
mercuryEpslion = radians(0.0349066)
venusEpsilon = radians(0.0523599)
earthEpsilon = radians(0.4101524)
marsEpsilon = radians(0.43964844)

mercuryAngle = 0
venusAngle = 0
earthAngle = 0
marsAngle = 0

sunlight = local_light( pos = vec(0,0,0), color=color.white )

programSpeed = 1.0

scene.pause() 

"""
sphere(pos=vector(0,0,0),texture="https://i.imgur.com/1nVWbbd.jpg",radius=45e6,shininess=0)
"""

def camera_menu(m):
    if m.selected in solar_system:
        scene.camera.follow(solar_system[m.selected])

menu(choices=list(solar_system.keys()), bind=camera_menu, pos=scene.title_anchor) 

while (True):
    rate(150) 
   
    mercury.pos = vec( mercuryOrbitRadius/150 * cos(radians(mercuryAngle)), 0, mercuryOrbitRadius/150 * sin(radians(mercuryAngle)) ) 
    venus.pos = vec( venusOrbitRadius/150 * cos(radians(venusAngle)), 0, venusOrbitRadius/150 * sin(radians(venusAngle)) ) 
    earth.pos = vec( earthOrbitRadius/150 * cos(radians(earthAngle)), 0, earthOrbitRadius/150 * sin(radians(earthAngle)) )
    mars.pos = vec( marsOrbitRadius/150 * cos(radians(marsAngle)), 0, marsOrbitRadius/150 * sin(radians(marsAngle)) ) 
    
    mercuryAngle -= 1/mercuryOrbitRate * programSpeed
    venusAngle -= 1/venusOrbitRate * programSpeed
    earthAngle -= 1/earthOrbitRate * programSpeed
    marsAngle -= 1/marsOrbitRate * programSpeed

   
    sun.rotate (angle = sunEpsilon, axis = vector(np.sin(sunEpsilon), np.cos(sunEpsilon), 0))
    
    mercury.rotate (angle = mercuryEpslion, axis = vector(np.sin(mercuryEpslion), np.cos(mercuryEpslion), 0))
    venus.rotate (angle = venusEpsilon, axis = vector(np.sin(venusEpsilon), np.cos(venusEpsilon), 0))
    earth.rotate (angle = earthEpsilon, axis = vector(np.sin(earthEpsilon), np.cos(earthEpsilon), 0))
    mars.rotate (angle = marsEpsilon, axis = vector(np.sin(marsEpsilon), np.cos(marsEpsilon), 0)) 