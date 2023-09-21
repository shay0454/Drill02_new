from pico2d import*
import math
open_canvas()
grass=load_image("grass.png")
character=load_image("character.png")
def run_rectangle():
    print('rect')
    pass
def run_circle():
    print('circle')
    #그림 그림
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400,90)
    delay(1)
    pass
while True:
    run_rectangle()
    run_circle()
    break

close_canvas()
