import pygame
import sys

def dda(x1, y1, x2, y2, screen):
    dx, dy = x2 - x1, y2 - y1
    steps = int(max(abs(dx), abs(dy)))
    x_inc, y_inc = dx / steps, dy / steps
    x, y = x1, y1
    for _ in range(steps + 1):
        screen.set_at((round(x), round(y)), (255, 255, 255))
        x += x_inc
        y += y_inc

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 0))

dda(50, 50, 300, 200, screen)  # Draw a line from (50, 50) to (300, 200)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



import pygame
import sys

def bresenham(x1, y1, x2, y2, screen):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        screen.set_at((x1, y1), (255, 255, 255))
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 0))

bresenham(50, 50, 300, 200, screen)  # Draw a line from (50, 50) to (300, 200)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



import pygame
import sys

def draw_circle(xc, yc, r, screen):
    x = 0
    y = r
    p = 1 - r

    def plot_circle_points(xc, yc, x, y):
        points = [
            (xc + x, yc + y), (xc - x, yc + y),
            (xc + x, yc - y), (xc - x, yc - y),
            (xc + y, yc + x), (xc - y, yc + x),
            (xc + y, yc - x), (xc - y, yc - x)
        ]
        for px, py in points:
            screen.set_at((px, py), (255, 255, 255))

    while x <= y:
        plot_circle_points(xc, yc, x, y)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 0))

draw_circle(200, 200, 100, screen)  # Circle centered at (200, 200) with radius 100

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


import pygame
import sys

def flood_fill(x, y, target_color, replacement_color, screen):
    if target_color == replacement_color:
        return
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        if 0 <= x < screen.get_width() and 0 <= y < screen.get_height():
            if screen.get_at((x, y))[:3] == target_color:
                screen.set_at((x, y), replacement_color)
                stack.extend([(x+1,y), (x-1,y), (x,y+1), (x,y-1)])

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 0))

# Draw a white rectangle to test fill
pygame.draw.rect(screen, (255, 255, 255), (100, 100, 200, 200))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            target = screen.get_at((x, y))[:3]
            flood_fill(x, y, target, (255, 0, 0), screen)
            pygame.display.update()



import pygame
import sys

def boundary_fill(x, y, fill_color, boundary_color, screen):
    current_color = screen.get_at((x, y))[:3]
    if current_color != boundary_color and current_color != fill_color:
        screen.set_at((x, y), fill_color)
        pygame.display.update()
        boundary_fill(x+1, y, fill_color, boundary_color, screen)
        boundary_fill(x-1, y, fill_color, boundary_color, screen)
        boundary_fill(x, y+1, fill_color, boundary_color, screen)
        boundary_fill(x, y-1, fill_color, boundary_color, screen)

pygame.init()
screen = pygame.display.set_mode((400, 400))
screen.fill((0, 0, 0))

# Draw a white rectangle with a border
pygame.draw.rect(screen, (255, 255, 255), (100, 100, 200, 200), 1)  # boundary = white

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            boundary_fill(x, y, (255, 0, 0), (255, 255, 255), screen)



import pygame
import sys

def draw_shape(points, color, screen):
    pygame.draw.polygon(screen, color, points, 2)

def translate(points, tx, ty):
    return [(x + tx, y + ty) for x, y in points]

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("2D Translation - Arrow Keys")

# Initial shape (triangle)
shape = [(100, 100), (150, 50), (200, 100)]
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    draw_shape(shape, (0, 255, 0), screen)  # Draw translated shape
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        shape = translate(shape, -5, 0)
    if keys[pygame.K_RIGHT]:
        shape = translate(shape, 5, 0)
    if keys[pygame.K_UP]:
        shape = translate(shape, 0, -5)
    if keys[pygame.K_DOWN]:
        shape = translate(shape, 0, 5)

    clock.tick(30)


import pygame
import sys

def draw_shape(points, color, screen):
    pygame.draw.polygon(screen, color, points, 2)

def scale(points, sx, sy, center):
    cx, cy = center
    return [((x - cx) * sx + cx, (y - cy) * sy + cy) for x, y in points]

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("2D Scaling - Use S/s Keys")

# Initial shape (triangle)
shape = [(100, 100), (150, 50), (200, 100)]
center = (150, 100)  # Scaling center

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    draw_shape(shape, (0, 255, 0), screen)  # Green shape
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:  # Scale up
        shape = scale(shape, 1.1, 1.1, center)
    if keys[pygame.K_a]:  # Scale down
        shape = scale(shape, 0.9, 0.9, center)

    clock.tick(30)


import pygame
import sys
import math

def draw_shape(points, color, screen):
    pygame.draw.polygon(screen, color, points, 2)

def rotate(points, angle_deg, center):
    angle_rad = math.radians(angle_deg)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    cx, cy = center
    rotated = []
    for x, y in points:
        x -= cx
        y -= cy
        xr = x * cos_a - y * sin_a
        yr = x * sin_a + y * cos_a
        rotated.append((xr + cx, yr + cy))
    return rotated

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("2D Rotation - Press R/L to Rotate")

# Initial shape (triangle)
shape = [(100, 100), (150, 50), (200, 100)]
center = (150, 100)  # Rotation center

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    draw_shape(shape, (0, 255, 0), screen)  # Green shape
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:  # Rotate clockwise
        shape = rotate(shape, -5, center)
    if keys[pygame.K_l]:  # Rotate counter-clockwise
        shape = rotate(shape, 5, center)

    clock.tick(30)


import pygame
import sys

def draw_shape(points, color, screen):
    pygame.draw.polygon(screen, color, points, 2)

def reflect(points, axis, center):
    cx, cy = center
    reflected = []
    for x, y in points:
        if axis == 'x':
            reflected.append((x, 2*cy - y))
        elif axis == 'y':
            reflected.append((2*cx - x, y))
        elif axis == 'o':
            reflected.append((2*cx - x, 2*cy - y))
    return reflected

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("2D Reflection - Press X/Y/O")

# Initial shape (triangle)
shape = [(100, 100), (150, 50), (200, 100)]
center = (150, 100)  # Reflection center

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    draw_shape(shape, (0, 255, 0), screen)  # Green shape
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:  # Reflect over X-axis
        shape = reflect(shape, 'x', center)
    if keys[pygame.K_y]:  # Reflect over Y-axis
        shape = reflect(shape, 'y', center)
    if keys[pygame.K_o]:  # Reflect over origin
        shape = reflect(shape, 'o', center)

    clock.tick(30)



import pygame
import sys

def draw_shape(points, color, screen):
    pygame.draw.polygon(screen, color, points, 2)

def shear(points, sx, sy, center):
    cx, cy = center
    sheared = []
    for x, y in points:
        # Shearing transformation
        new_x = x + sx * (y - cy)
        new_y = y + sy * (x - cx)
        sheared.append((new_x, new_y))
    return sheared

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("2D Shearing - Press X/Y to Shear")

# Initial shape (triangle)
shape = [(100, 100), (150, 50), (200, 100)]
center = (150, 100)  # Shearing center

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    draw_shape(shape, (0, 255, 0), screen)  # Green shape
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_x]:  # Shear in the X-direction
        shape = shear(shape, 0.5, 0, center)  # Horizontal shearing
    if keys[pygame.K_y]:  # Shear in the Y-direction
        shape = shear(shape, 0, 0.5, center)  # Vertical shearing

    clock.tick(30)
