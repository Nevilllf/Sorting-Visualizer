import pygame
import random

pygame.init()

class DrawInfo:
    black = 0,0,0
    white = 255,255, 255
    green = 0, 255, 255
    red = 255, 0 ,0
    grey = 128, 128, 128
    BACKGROUND_COL = white
    side_pad = 100
    top_pad = 150

    GRADIENTS = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]

    def __init__(self,width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Visualization")
        self.set_list(lst)

    def set_list(self,lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.side_pad)) / len(lst)
        self.block_height = round((self.height - self.top_pad) / (self.max_val - self.min_val))
        self.start_x = self.side_pad // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COL)
    draw_list(draw_info)
    pygame.display.update()

def draw_list(draw_info):
    lst = draw_info.lst
    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val)*draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]
        pygame.draw.rect(draw_info.window, color, (x,y,draw_info.block_width, draw_info.block_height))


def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    n= 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInfo(800,600,lst)

    while run:
        clock.tick(60)
        draw(draw_info)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()




