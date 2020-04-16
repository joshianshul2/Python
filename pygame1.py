import pygame
pygame.init()
disp_width=800
disp_height=600
gameDisp=pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption("Fast and Furious!")
black(0,0,0)
white(255,255,255)
clock=pygame.time.Clock()
crashed=False

# defining a car
carImg=pygame.image.load('redcar.png')
car_height=100
car_width=50
x_change=0


def car(x,y):
    gameDisp.blit(carImg,(x,y))###
x=disp_width*0.5
y=disp_height*0.8

#gameloop
while not crashed:
#choose an  event
    for event in pygame.event.get():
# if window is closed  then
        if event.type==pygame.QUIT:
               crashed=True
    gameDisp.fill(white)
    pygame.display.update()
    clock.tick(60)
    pygame.quit()
quit()
