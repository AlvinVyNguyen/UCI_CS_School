# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage

from prey import Prey
from random import random


class Floater(Prey):
    radius = 5
    
    def __init__(self,x,y):
        floater_radius = 2*Floater.radius
        Prey.__init__(self,x,y,floater_radius,floater_radius,0,5)
        self.randomize_angle()

        
    def update(self,model):
        seventy_percent_threshold = .7
        thirty_percent_threshold = .3
        halved = .5
        if random() <= seventy_percent_threshold:
            pass
        elif random() <= thirty_percent_threshold:
            speed = min(7,3)
            self.set_velocity(speed, self.get_angle()+random()*halved)
        self.move()

    def display(self,canvas):
        canvas.create_oval(self._x-Floater.radius, self._y-Floater.radius,
                               self._x+Floater.radius, self._y+Floater.radius,
                               fill='red')