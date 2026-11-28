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
score = 0

cct  = font.render("Candy Crush", True, "#FFFFFF")
screen.blit(cct, (445, 160))
sst  = font.render("Subway Surfers", True, "#FFFFFF")
screen.blit(sst, (445, 360))
lt  = font.render("Ludo", True, "#FFFFFF")
screen.blit(lt, (445, 260))
trt  = font.render("Temple Run", True, "#FFFFFF")
screen.blit(trt, (445, 60))
score = font.render("Score = " + str(score) + "/4", True, "#FFFFFF") 
screen.blit(score, (550, 20))

ccr = pygame.Rect(45, 25, 90, 90)
ssr = pygame.Rect(45, 125, 90, 90)
lr = pygame.Rect(45, 225, 90, 90)
trr = pygame.Rect(45, 325, 90, 90)

cctr = pygame.Rect(445, 60, 100, 25)
sstr = pygame.Rect(445, 160, 110, 25)
ltr = pygame.Rect(445, 260, 45, 25)
trtr = pygame.Rect(445, 360, 145, 25)

correctanswers = [(ccr, cctr), (ssr, sstr), (lr, ltr), (trr,  trtr)]
start_pos = None
end_pos = None
start_rect = None
end_rect = None

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_pos = pygame.mouse.get_pos()
            clicked_on_valid_area = False
            for x,y in correctanswers:
                if x.collidepoint(start_pos):
                    clicked_on_valid_area = True
                    start_rect = x
                    break
            if clicked_on_valid_area == True:
                pygame.draw.circle(screen, "#EB90B0", start_pos, 5)
        if event.type == pygame.MOUSEBUTTONUP:
            end_pos = pygame.mouse.get_pos()
            released_on_valid_area = False
            for x,y in correctanswers:
                if y.collidepoint(end_pos):
                    released_on_valid_area = True
                    end_rect = y
                    break
            if released_on_valid_area == True and clicked_on_valid_area == True:
                pygame.draw.circle(screen, "#88C67F", end_pos, 5)
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()