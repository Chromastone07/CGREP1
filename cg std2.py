
import pygame
pygame.init()
w, h = 600, 600
s = pygame.display.set_mode((w, h))
c = pygame.Surface((w, h)); c.fill((0,0,0))
p = []

def P(x,y,col=(255,255,255)): 
    if 0<=x<w and 0<=y<h: c.set_at((x,y),col)

def D(x1,y1,x2,y2):
    dx,dy=x2-x1,y2-y1; s=max(abs(dx),abs(dy))
    x,y=x1,y1
    for _ in range(int(s)+1): P(round(x),round(y)); x+=dx/s; y+=dy/s

def B(x1,y1,x2,y2):
    dx,dy=abs(x2-x1),abs(y2-y1); x,y,sx,sy=x1,y1,1 if x2>x1 else -1,1 if y2>y1 else -1
    if dx>dy: e=dx/2; 
    else: e=dy/2
    while (x!=x2 if dx>dy else y!=y2):
        P(x,y,(0,255,0)); e-=(dy if dx>dy else dx)
        if e<0: (y:=y+sy) if dx>dy else (x:=x+sx); e+=(dx if dx>dy else dy)
        x+=sx if dx>dy else 0; y+=sy if dx<=dy else 0
    P(x,y,(0,255,0))

def C(cx,cy,r=50):
    x,y,p=0,r,1-r
    while x<=y:
        for dx,dy in [(x,y),(-x,y),(x,-y),(-x,-y),(y,x),(-y,x),(y,-x),(-y,-x)]: P(cx+dx,cy+dy,(255,0,0))
        x+=1; p+=2*x+1 if p<0 else 2*(x-y)+1; y-=0 if p<0 else 1

def F(x,y,t,n): 
    st=[(x,y)]
    while st:
        x,y=st.pop()
        if 0<=x<w and 0<=y<h and c.get_at((x,y))==t: P(x,y,n); st+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

def O(x,y,b,n): 
    st=[(x,y)]
    while st:
        x,y=st.pop()
        if 0<=x<w and 0<=y<h:
            col=c.get_at((x,y))
            if col!=b and col!=n: P(x,y,n); st+=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

while 1:
    s.blit(c,(0,0))
    for e in pygame.event.get():
        if e.type==pygame.QUIT: exit()
        if e.type==pygame.MOUSEBUTTONDOWN: p.append(e.pos)
        if e.type==pygame.KEYDOWN:
            if e.key==pygame.K_r: c.fill((0,0,0)); p=[]
            elif e.key==pygame.K_d and len(p)>1: D(*p[-2],*p[-1])
            elif e.key==pygame.K_b and len(p)>1: B(*p[-2],*p[-1])
            elif e.key==pygame.K_c and p: C(*p[-1])
            elif e.key==pygame.K_f and p: F(*p[-1],c.get_at(p[-1]),(0,0,255))
            elif e.key==pygame.K_o and p: O(*p[-1],(255,255,255),(255,0,0))
    pygame.display.flip()
