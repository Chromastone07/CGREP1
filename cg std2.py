import pygame
pygame.init()
w, h = 600, 600
s = pygame.display.set_mode((w, h))
c = pygame.Surface((w, h))
c.fill((0, 0, 0))
p = []
r = 50

def put(x, y, col=(255, 255, 255)):
    if 0 <= x < w and 0 <= y < h: c.set_at((x, y), col)

def dda(x1, y1, x2, y2):
    dx, dy = x2 - x1, y2 - y1
    steps = max(abs(dx), abs(dy))
    x, y = x1, y1
    for _ in range(int(steps)+1):
        put(round(x), round(y))
        x += dx/steps
        y += dy/steps

def bres(x1, y1, x2, y2):
    dx, dy = abs(x2 - x1), abs(y2 - y1)
    x, y, sx, sy = x1, y1, 1 if x2 > x1 else -1, 1 if y2 > y1 else -1
    if dx > dy:
        e = dx / 2
        while x != x2:
            put(x, y, (0, 255, 0))
            x += sx
            e -= dy
            if e < 0: y += sy; e += dx
    else:
        e = dy / 2
        while y != y2:
            put(x, y, (0, 255, 0))
            y += sy
            e -= dx
            if e < 0: x += sx; e += dy
    put(x, y, (0, 255, 0))

def circle(cx, cy, r):
    x, y, p = 0, r, 1 - r
    while x <= y:
        for dx, dy in [(x,y),(-x,y),(x,-y),(-x,-y),(y,x),(-y,x),(y,-x),(-y,-x)]:
            put(cx+dx, cy+dy, (255,0,0))
        x += 1
        if p < 0: p += 2*x+1
        else: y -= 1; p += 2*(x - y) + 1

def fill(x, y, old, new):
    stack = [(x,y)]
    while stack:
        x,y = stack.pop()
        if 0<=x<w and 0<=y<h and c.get_at((x,y)) == old:
            put(x,y,new)
            stack += [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

def bfill(x, y, b, f):
    stack = [(x,y)]
    while stack:
        x,y = stack.pop()
        col = c.get_at((x,y))
        if 0<=x<w and 0<=y<h and col != b and col != f:
            put(x,y,f)
            stack += [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

run = True
while run:
    s.fill((30, 30, 30))
    s.blit(c, (0,0))
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False
        elif e.type == pygame.MOUSEBUTTONDOWN: p.append(e.pos)
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r: c.fill((0,0,0)); p.clear()
            elif e.key == pygame.K_d and len(p) >= 2: dda(*p[-2], *p[-1])
            elif e.key == pygame.K_b and len(p) >= 2: bres(*p[-2], *p[-1])
            elif e.key == pygame.K_c and p: circle(*p[-1], r)
            elif e.key == pygame.K_f and p: fill(*p[-1], c.get_at(p[-1]), (0,0,255))
            elif e.key == pygame.K_o and p: bfill(*p[-1], (255,255,255), (255,0,0))
    pygame.display.flip()
pygame.quit()
