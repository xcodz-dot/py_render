from PIL import Image
from py_render import layers
import pygame

pygame.init()

display = pygame.display.set_mode((1280, 720))

im = Image.open("test_images/beach.jpg")
im = im.resize((1280, 720))

font = pygame.font.Font(pygame.font.get_default_font(), 30)

def convert_to_pygame(im: Image.Image):
    return pygame.image.fromstring(im.tobytes(), im.size, im.mode)

running = True
FPS=60
clock = pygame.time.Clock()
blur = 1
x = y = 0
while running:
    update_frame=False
    time_delta = clock.tick(FPS)
    cfps = 1000//time_delta
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            update_frame = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                if blur - 2 > 0:
                    blur -= 2
            elif event.key == pygame.K_UP:
                blur += 2
    
    if update_frame:
        frame = layers.AreaFilter((x, y, 200, 200), layers.Blur(blur)).apply(im)
        display.blit(convert_to_pygame(frame), (0, 0))

    display.fill((255,)*3, (0, 0, 100, 40))
    display.blit(font.render(str(cfps), False, (0, 220, 0) if cfps > 30 else (255, 0, 0)), (0, 0))
    
    pygame.display.update()
