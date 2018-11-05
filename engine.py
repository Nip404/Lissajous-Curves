import pygame
import random
import math

class Circle:
    def __init__(self,pos,radius,speed=1,theta=0):
        self.pos = pos
        self.radius = radius
        
        self.speed = speed
        self.theta = theta
        self.outer_pos = self.get_outer_pos()
        
        self.colour = [random.randint(50,255) for i in range(3)]

    def get_outer_pos(self):
        return [i*self.radius + self.pos[p] for p,i in enumerate([math.cos(math.radians(self.theta)),math.sin(math.radians(self.theta))])]

    def move(self):
        self.theta += self.speed
        self.outer_pos = self.get_outer_pos()

class Display:
    line_colour = (40,60,80)
    
    def __init__(self,surf):
        self.surf = surf
        self.cumulative_shapes = [] # [[pos,colour],]

    def init_y_circles(self,y_circles):
        self.y_circles = y_circles
        
    def init_x_circles(self,x_circles):
        self.x_circles = x_circles

    def animate(self):
        for i in self.x_circles:
            i.move()
        for i in self.y_circles:
            i.move()

    def draw_sources(self):
        for i in self.x_circles+self.y_circles:
            pygame.draw.circle(self.surf,i.colour,i.pos,i.radius,1)

    def draw_drawn_shapes(self):
        for i in self.cumulative_shapes:
            pygame.draw.circle(self.surf,i[1],list(map(int,i[0])),1,0)

    def draw_lines(self):
        for px,x in enumerate(self.x_circles):
            for py,y in enumerate(self.y_circles):
                pygame.draw.circle(self.surf,(255,255,255),list(map(int,x.outer_pos)),5,0)
                pygame.draw.circle(self.surf,(255,255,255),list(map(int,y.outer_pos)),5,0)

                line1_a = [0,y.outer_pos[1]]
                line1_b = [self.surf.get_width(),y.outer_pos[1]]
                line2_a = [x.outer_pos[0],0]
                line2_b = [x.outer_pos[0],self.surf.get_height()]
                    
                pygame.draw.line(self.surf,self.line_colour,line1_a,line1_b,2)
                pygame.draw.line(self.surf,self.line_colour,line2_a,line2_b,2)

                point = [self.calculate_intersection(line1_a,line1_b,line2_a,line2_b),self.average_colour(x.colour,y.colour)]

                if not point in self.cumulative_shapes:
                    self.cumulative_shapes.append(point)

    @staticmethod
    def calculate_intersection(a1,a2,b1,b2):
        return [
            (((a2[0]*a1[1] - a1[0]*a2[1])*(b2[0]-b1[0]))-((b2[0]*b1[1] - b1[0]*b2[1])*(a2[0]-a1[0])))/(((a2[0]-a1[0])*(b2[1]-b1[1]))-((b2[0]-b1[0])*(a2[1]-a1[1]))),
            (((a2[0]*a1[1] - a1[0]*a2[1])*(b2[1]-b1[1]))-((b2[0]*b1[1] - b1[0]*b2[1])*(a2[1]-a1[1])))/(((a2[0]-a1[0])*(b2[1]-b1[1]))-((b2[0]-b1[0])*(a2[1]-a1[1])))]

    @staticmethod
    def average_colour(c1,c2):
        return [int((c1[i]+c2[i])/2) for i in range(3)]

