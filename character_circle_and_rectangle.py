from pico2d import*
import math
open_canvas()
grass=load_image("grass.png")
character=load_image("character.png")
def render_frame(x,y):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        delay(0.01)    
def run_rectangle():
    print('rect')
    x,y=400,90
    for x in range(50,750+1,10):render_frame(x,y)
    for y in range(90,510+1,10):render_frame(750,y)
    for x in range(750,50-1,-10):render_frame(x,550)
    for y in range(510,90-1,-10):render_frame(50,y)
def run_circle():
    print('circle')
    #그림 그림
    grass.draw_now(400,30)
    character.draw_now(400,90)
    cx,cy,r=400,300,200
    for deg in range(0,360+1,5):
        x=cx+r*math.cos(math.radians(deg-90))
        y=cy+r*math.sin(math.radians(deg-90))
        render_frame(x,y)
while True:
    run_rectangle()
    #run_circle()
    break

close_canvas()
