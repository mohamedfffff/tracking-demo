from time import sleep
from turtle import *
import random
import math

#used variables
screen_width = 700
screen_height = 700
points_number = 250
point_speed = 3
points = []
target = [0,0]

class point:
    #each point should be given an x,y value when initializing
    def __init__(self,x,y):
        self.x = x
        self.y = y

def set_up():
    #intializing window size and adding 20 to avoid points being on border
    setup(screen_width+20,screen_height+20)
    #intializing draw speed and setting it to 0 for max speed
    tracer(0)
    #hidding turtle from screen
    hideturtle()

def draw_set_up():
    #draw backgroud square
    color("white")
    penup()
    goto((int)(-screen_width/2),(int)(screen_height/2))
    pendown()
    begin_fill()
    forward(screen_width)
    right(90)
    forward(screen_height)
    right(90)
    forward(screen_width)
    right(90)
    forward(screen_height)
    right(90)
    end_fill()
    #draw vertival line
    penup()
    color("black")
    goto(0,(int)(-screen_height/2))
    pendown()
    goto(0,(int)(screen_height/2))
    #draw horizontal line
    penup()
    goto((int)(-screen_width/2),0)
    pendown()
    goto((int)(screen_width/2),0)

def create_points():
    #giving each point a random x,y and append it to the points list
    for i in range(points_number):
        x = (int)(random.random()*screen_width - screen_width/2)
        y = (int)(random.random()*screen_height - screen_height/2)
        p = point(x,y)
        points.append(p)

def search():
    #applying search algorithm for each point
    #to calculate new velocity and new x,y
    for p in points:
        #calculating x,y distance from point to target
        delta = [target[0]-p.x , target[1]-p.y]
        #calculating total differance from point to target
        total_difference = math.fabs(delta[0]) + math.fabs(delta[1])
        #updating x,y values
        if(total_difference != 0):
            #delta[]/difference determine how important the step to reach target
            #should the point move more on x or y based on the difference from point to target
            #point_speed determine the distance of each step
            p.x += delta[0]/total_difference * point_speed
            p.y += delta[1]/total_difference * point_speed

def draw_points():
    color("blue")
    #putting up pen to draw points with no lines
    penup()
    #iterating each point in points list to draw it
    for i in range(points_number):
        goto(points[i].x,points[i].y)
        dot(5)

def update_target(x,y):
    target[0] = x
    target[1] = y    

def magic():
    set_up()
    create_points()
    while True:
        onscreenclick(update_target) 
        # print(target)
        search()
        draw_set_up()
        draw_points()
        update()
        clear()

#magic goes brrrrrrrrrrrrrrrr
magic()
mainloop()



