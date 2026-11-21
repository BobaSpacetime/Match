import pygame
pygame.init()
WIDTH = 650
HEIGHT = 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill("#1008216C")

font = pygame.font.SysFont("comicsansms", 17)
cc = pygame.image.load("Match/images/candycrush.jpg")
screen.blit(cc, (45,25))
l = pygame.image.load("Match/images/ludo.png")
screen.blit(l, (45, 125))
ss = pygame.image.load("Match/images/subwaysurfer.png")
screen.blit(ss, (45, 225))
tr = pygame.image.load("Match/images/templerun.png")
screen.blit(tr, (45, 325))

cct  = font.render("Candy Crush", True, "#FFFFFF")
screen.blit(cct, (445, 160))
sst  = font.render("Subway Surfers", True, "#FFFFFF")
screen.blit(sst, (445, 360))
lt  = font.render("Ludo", True, "#FFFFFF")
screen.blit(lt, (445, 260))
trt  = font.render("Temple Run", True, "#FFFFFF")
screen.blit(trt, (445, 60))

ccr = pygame.Rect(45, 25, 90, 90)
ssr = pygame.Rect(45, 125, 90, 90)
lr = pygame.Rect(45, 225, 90, 90)
trr = pygame.Rect(45, 325, 90, 90)

cctr = pygame.Rect(445, 60, 100, 25)
sstr = pygame.Rect(445, 160, 110, 25)
ltr = pygame.Rect(445, 260, 45, 25)
trtr = pygame.Rect(445, 360, 145, 25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()