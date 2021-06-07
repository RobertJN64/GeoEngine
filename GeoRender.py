import GeoTools
import warnings
import pygame

pygame.init()


def render(objlist, sf = 1):
    maxx = 0
    maxy = 0

    for objcolor in objlist:
        obj = objcolor[0]
        if type(obj) is GeoTools.rect:
            maxx = max(obj.rightx, maxx)
            maxy = max(obj.bottomy, maxy)
        #TODO - other types

    display = pygame.display.set_mode((maxx * sf, maxy * sf))
    pygame.display.set_caption("GeoRender")

    done = False
    while not done:
        display.fill((200,200,200))
        for objcolor in objlist:
            obj = objcolor[0]
            color = objcolor[1]

            if type(obj) is GeoTools.rect:
                pygame.draw.rect(display, color, (round(obj.leftx * sf), round(obj.topy * sf),
                                                  round(obj.width * sf), round(obj.height * sf)))

            elif type(obj) is GeoTools.line:
                pygame.draw.line(display, color, (obj.a.x * sf, obj.a.y * sf),
                                 (obj.b.x * sf, obj.b.y * sf))

            elif type(obj) is GeoTools.circle:
                pygame.draw.circle(display, color, (obj.center.x * sf, obj.center.y * sf), obj.rad)

            else:
                warnings.warn("Unexpected type: " + str(type(obj)))



        pygame.display.flip()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True