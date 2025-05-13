
#all 2d transformations combined (scale, rotate,reflect,shear)

import pygame
import sys
import math

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("2D Transformations")
clock = pygame.time.Clock()

# Shape (triangle) and reference center
shape = [(200, 200), (250, 150), (300, 200)]
center = (250, 200)

def draw_shape(pts):
    pygame.draw.polygon(screen, (0, 255, 0), pts, 2)

def translate(pts, dx, dy):
    return [(x + dx, y + dy) for x, y in pts]

def scale(pts, sx, sy, cx, cy):
    return [((x - cx) * sx + cx, (y - cy) * sy + cy) for x, y in pts]

def rotate(pts, angle_deg, cx, cy):
    rad = math.radians(angle_deg)
    cos_a, sin_a = math.cos(rad), math.sin(rad)
    return [((x - cx) * cos_a - (y - cy) * sin_a + cx,
             (x - cx) * sin_a + (y - cy) * cos_a + cy) for x, y in pts]

def reflect(pts, axis, cx, cy):
    if axis == 'x':
        return [(x, 2*cy - y) for x, y in pts]
    elif axis == 'y':
        return [(2*cx - x, y) for x, y in pts]
    elif axis == 'o':
        return [(2*cx - x, 2*cy - y) for x, y in pts]

def shear(pts, shx, shy, cx, cy):
    return [(x + shx * (y - cy), y + shy * (x - cx)) for x, y in pts]

# Main loop
while True:
    screen.fill((0, 0, 0))
    draw_shape(shape)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    # Translation
    if keys[pygame.K_LEFT]: shape = translate(shape, -5, 0)
    if keys[pygame.K_RIGHT]: shape = translate(shape, 5, 0)
    if keys[pygame.K_UP]: shape = translate(shape, 0, -5)
    if keys[pygame.K_DOWN]: shape = translate(shape, 0, 5)

    # Scaling
    if keys[pygame.K_s]: shape = scale(shape, 1.1, 1.1, *center)
    if keys[pygame.K_a]: shape = scale(shape, 0.9, 0.9, *center)

    # Rotation
    if keys[pygame.K_r]: shape = rotate(shape, -5, *center)
    if keys[pygame.K_l]: shape = rotate(shape, 5, *center)

    # Reflection
    if keys[pygame.K_x]: shape = reflect(shape, 'x', *center)
    if keys[pygame.K_y]: shape = reflect(shape, 'y', *center)
    if keys[pygame.K_o]: shape = reflect(shape, 'o', *center)

    # Shearing
    if keys[pygame.K_h]: shape = shear(shape, 0.2, 0, *center)  # Horizontal
    if keys[pygame.K_v]: shape = shear(shape, 0, 0.2, *center)  # Vertical

    clock.tick(30)
