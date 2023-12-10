import pygame
import pygame_gui
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 800
manager = pygame_gui.UIManager((800, 600))
windows = []
stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]
CLICK_THRESHOLD = 5
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação 2D Sistema Solar")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
LIGHT_GREEN = (64, 184, 133)
ORANGE = (255, 128, 0)
PURPLE = (144, 84, 233)
LIGHT_BLUE = (0, 255, 255)

FONT = pygame.font.SysFont("comicsans", 16)

class Planeta:
    UA = 149.6e6 * 1000
    G = 6.67428e-11
    ESCALA = 250 / UA
    TIMESTEP = 3600*24

    def __init__(self, x, y, raio, cor, massa, nome = None,raioReal = None, afelio = None, perielio = None, Fg = None):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.massa = massa
        self.nome = nome
        self.raioReal = raioReal
        self.afelio = afelio
        self.perielio = perielio
        self.Fg = Fg

        self.orbita = []
        self.estrela = False
        self.distancia_estrela = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.ESCALA + WIDTH / 2
        y = self.y * self.ESCALA + HEIGHT / 2

        if len(self.orbita) > 2:
            updated_points = []
            for point in self.orbita:
                x, y = point
                x = x * self.ESCALA + WIDTH / 2
                y = y * self.ESCALA + HEIGHT / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.cor, False, updated_points, 2)

        pygame.draw.circle(win, self.cor, (x, y), self.raio)

    def atracao(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.estrela:
            self.distancia_estrela = distance

        force = self.G * self.massa * other.massa / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planetas):
        total_fx = total_fy = 0
        for planeta in planetas:
            if self == planeta:
                continue

            fx, fy = self.atracao(planeta)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.massa * self.TIMESTEP
        self.y_vel += total_fy / self.massa * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP

        self.orbita.append((self.x, self.y))

    def check_click_on_planet(self, mouse_pos, planeta):
        x, y = mouse_pos
        x_planeta, y_planeta = planeta.x * Planeta.ESCALA + WIDTH / 2, planeta.y * Planeta.ESCALA + HEIGHT / 2
        if math.hypot(x - x_planeta, y - y_planeta) < planeta.raio:
            return True
        return False 
    
    def is_click_on_orbit(self, click_x, click_y):
        for point in self.orbita:
            orbit_x, orbit_y = point
            orbit_x = orbit_x * self.ESCALA + WIDTH / 2
            orbit_y = orbit_y * self.ESCALA + HEIGHT / 2

            distance = ((orbit_x - click_x) ** 2 + (orbit_y - click_y) ** 2) ** 0.5
            if distance < CLICK_THRESHOLD:
                return True

        return False

def main():

    run = True
    clock = pygame.time.Clock()

    sol = Planeta(0, 0, 30, YELLOW, 1.98892 * 10**30, nome = 'Sol', raioReal = '696.340 km', afelio = None, perielio = None, Fg = '274 m/s²')
    sol.estrela = True

    terra = Planeta(-1 * Planeta.UA, 0, 16, BLUE, 5.9742 * 10**24, nome = 'Terra', raioReal = '6.371 km', afelio =  '152.100.000 km', perielio = '147.100.000 km', Fg = '9,8 m/s²')
    terra.y_vel = 29.783 * 1000 

    marte = Planeta(-1.524 * Planeta.UA, 0, 12, RED, 6.39 * 10**23, nome = 'Marte', raioReal = '3.389,5 km', afelio = '249.200.000 km', perielio = '206.700.000', Fg = '3,71 m/s²')
    marte.y_vel = 24.077 * 1000

    mercurio = Planeta(0.387 * Planeta.UA, 0, 8, DARK_GREY, 3.30 * 10**23, nome = 'Mercúrio', raioReal = '2.439,7 km', afelio = '69.800.000 km', perielio = '46.000.000 km', Fg = '3,7 m/s²')
    mercurio.y_vel = -47.4 * 1000

    venus = Planeta(0.723 * Planeta.UA, 0, 14, ORANGE, 4.8685 * 10**24, nome = 'Vênus', raioReal =  '6.051,8 km', afelio = '108.900.000 km', perielio = '107.500.000 km', Fg = '8,87 m/s²')
    venus.y_vel = -35.02 * 1000

    planetas = [sol, terra, marte, mercurio, venus]

    while run:

        mouse_pos = pygame.mouse.get_pos()

        time_delta = clock.tick(60) / 1000
        WIN.fill((0, 0, 0))

        for star in stars:
            pygame.draw.circle(WIN, (255, 255, 255), star, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_WINDOW_CLOSE:
                    if event.ui_element in windows:
                        event.ui_element.kill()
                        windows.remove(event.ui_element)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()  
                click_x, click_y = mouse_pos

                for planeta in planetas:
                    if planeta.is_click_on_orbit(click_x, click_y) or planeta.check_click_on_planet(mouse_pos, planeta):
                        window = pygame_gui.elements.UIWindow(pygame.Rect((200, 200), (600, 400)), manager)
                        window.set_display_title(f'Informações do Corpo Celeste: {planeta.nome}')
                        windows.append(window)

                        if planeta.estrela == False:

                            raio_label = pygame_gui.elements.UILabel(pygame.Rect((0, 0), (300, 50)), f'Raio: {planeta.raioReal}', manager, window)
                            massa_label = pygame_gui.elements.UILabel(pygame.Rect((0, 50), (300, 50)), f'Massa: {planeta.massa}', manager, window)
                            fg_label = pygame_gui.elements.UILabel(pygame.Rect((0, 200), (300, 50)), f'Aceleração da Gravidade: {planeta.Fg}', manager, window)    
                            afelio_label = pygame_gui.elements.UILabel(pygame.Rect((0, 100), (300, 50)), f'Distância no Afélio: {planeta.afelio}', manager, window)
                            perielio_label = pygame_gui.elements.UILabel(pygame.Rect((0, 150), (300, 50)), f'Distância no Periélio: {planeta.perielio}', manager, window)                        
                        
                            planet_image = pygame.image.load(f'imagens/{planeta.nome}.png')
                            scaled_image = pygame.transform.scale(planet_image, (200, 200))
                            planet_image_ui = pygame_gui.elements.UIImage(pygame.Rect((300, 60), (200, 200)), scaled_image, manager, container=window)

                        elif planeta.estrela == True:

                            raio_label = pygame_gui.elements.UILabel(pygame.Rect((0, 0), (300, 50)), f'Raio: {planeta.raioReal}', manager, window)
                            massa_label = pygame_gui.elements.UILabel(pygame.Rect((0, 50), (300, 50)), f'Massa: {planeta.massa}', manager, window)
                            fg_label = pygame_gui.elements.UILabel(pygame.Rect((0, 200), (300, 50)), f'Aceleração da Gravidade: {planeta.Fg}', manager, window)
                            magg_label = pygame_gui.elements.UILabel(pygame.Rect((0, 100), (300, 50)), 'M.absoluta: 4,83', manager, window)
                            mag_label = pygame_gui.elements.UILabel(pygame.Rect((0, 150), (300, 50)), 'M. aparente: -26,74', manager, window)

                            planet_image = pygame.image.load(f'imagens/{planeta.nome}.png')
                            scaled_image = pygame.transform.scale(planet_image, (200, 200))
                            planet_image_ui = pygame_gui.elements.UIImage(pygame.Rect((300, 60), (200, 200)), scaled_image, manager, container=window)
                            
            manager.process_events(event)

        for planeta in planetas:
            planeta.update_position(planetas)
            planeta.draw(WIN)

        manager.update(time_delta)
        manager.draw_ui(WIN)

        pygame.display.update()

    pygame.quit()

main()  