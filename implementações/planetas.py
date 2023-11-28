import pygame
import pygame_gui
import math

pygame.init()

WIDTH, HEIGHT = 800, 800
manager = pygame_gui.UIManager((800, 600))
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simulação Sistema Solar")

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

    def __init__(self, x, y, raio, cor, massa):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.massa = massa

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
        
        if not self.estrela:
            distance_text = FONT.render(f"{round(self.distancia_estrela/1000, 1)}km", 1, WHITE)
            win.blit(distance_text, (x - distance_text.get_width()/2, y - distance_text.get_height()/2))

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

def main():

    run = True
    clock = pygame.time.Clock()

    sol = Planeta(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sol.estrela = True

    terra = Planeta(-1 * Planeta.UA, 0, 16, BLUE, 5.9742 * 10**24)
    terra.y_vel = 29.783 * 1000 

    marte = Planeta(-1.524 * Planeta.UA, 0, 12, RED, 6.39 * 10**23)
    marte.y_vel = 24.077 * 1000

    mercurio = Planeta(0.387 * Planeta.UA, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercurio.y_vel = -47.4 * 1000

    venus = Planeta(0.723 * Planeta.UA, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000

    planetas = [sol, terra, marte, mercurio, venus]

    while run:

        time_delta = clock.tick(60) / 1000
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window.hide()
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
            
                for planeta in planetas:
                    if planeta.check_click_on_planet(mouse_pos, planeta):
                        print("Planeta clicado")
                        window = pygame_gui.elements.UIWindow(pygame.Rect((200, 200), (600, 400)), manager)
                        window.set_display_title('Edição de Planeta')
                        
                        x_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((0, 0), (200, 50)), manager, window, placeholder_text='Coordenada X')
                        y_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((0, 50), (200, 50)), manager, window, placeholder_text='Coordenada Y')
                        raio_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((0, 100), (200, 50)), manager, window, placeholder_text='Raio do Planeta')
                        cor_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((0, 150), (200, 50)), manager, window, placeholder_text='Cor do Planeta')
                        massa_entry = pygame_gui.elements.UITextEntryLine(pygame.Rect((0, 200), (200, 50)), manager, window, placeholder_text='Massa do Planeta')                     

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if event.ui_element == x_entry:
                    planeta.x = int(event.text)
                elif event.ui_element == y_entry:
                    planeta.y = int(event.text)
                elif event.ui_element == raio_entry:
                    planeta.raio = int(event.text)
                elif event.ui_element == cor_entry:
                    planeta.cor = event.text
                elif event.ui_element == massa_entry:
                    planeta.massa = float(event.text)
                elif event.type == pygame_gui.UI_WINDOW_CLOSE:
                    window.hide()

        manager.process_events(event)

        for planeta in planetas:
            planeta.update_position(planetas)
            planeta.draw(WIN)

        manager.update(time_delta)
        manager.draw_ui(WIN)

        pygame.display.update()

    pygame.quit()

main()  

          