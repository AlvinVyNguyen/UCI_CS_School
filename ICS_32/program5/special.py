#Because Christmas is coming up, I have created balls that change to Christmas colors constantly ("red", "orange", "yellow", "green", "blue", "violet")
from prey import Prey
import random

class Special(Prey):
    radius = 5

    def __init__(self,x,y):
        ball_radius = Special.radius*2
        Prey.__init__(self,x,y,ball_radius,ball_radius,0,5)
        self.randomize_angle()

        
    def update(self,model):
        self.move()

 
    def display(self,canvas):
        color = ["red", "orange", "yellow", "green", "blue", "violet"]
        canvas.create_oval(self._x+Special.radius, self._y+Special.radius,
                               self._x-Special.radius, self._y-Special.radius,
                               fill = random.choice(color))
