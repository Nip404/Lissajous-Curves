from engine import *
import pygame

s = [800, 800]

pygame.init()
screen = pygame.display.set_mode(s, 0, 32)
clock = pygame.time.Clock()
pygame.display.set_caption("Lissajous curve animations by NIP")

def get_circles(x_amount, y_amount):
    x_amount += 1
    y_amount += 1
    
    x_rad = int(screen.get_width() / (x_amount*2))
    y_rad = int(screen.get_height() / (y_amount*2))

    if x_rad > y_rad:
        y_rad = int((screen.get_height() - (2*x_rad)) / (y_amount*2))
        x_start = y_rad
        y_start = 2 * x_rad
        
    elif y_rad > x_rad:
        x_rad = int((screen.get_width() - (2*y_rad)) / (x_amount*2))
        
        x_start = 2 * y_rad
        y_start = x_rad
        
    else:
        x_start = x_rad
        y_start = y_rad
        
    x = [Circle([x_start + (p * 2 * x_rad),x_rad], x_rad, p/3) for p in range(x_amount)]
    y = [Circle([y_rad, y_start + (p * 2 * y_rad)], y_rad, p/3) for p in range(y_amount)]

    return x[1:], y[1:]

def main():
    display = Display(screen)
    x_amount, y_amount = 5, 5

    x, y = get_circles(x_amount, y_amount)

    display.init_x_circles(x)
    display.init_y_circles(y)

    while True:
        #clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        screen.fill((0, 0, 0))

        display.draw_sources()
        display.draw_lines()
        display.draw_drawn_shapes()
        display.animate()
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
