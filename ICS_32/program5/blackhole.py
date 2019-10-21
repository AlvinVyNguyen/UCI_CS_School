# A Black_Hole is a Simulton; it updates by removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey


class Black_Hole(Simulton):
    radius = 10
    
    def __init__(self,x,y): 
        black_hole_radius = 2*Black_Hole.radius  
        Simulton.__init__(self,x,y,black_hole_radius,black_hole_radius)
        
    def update(self,model):
        combined = model.find(lambda s : isinstance(s,Prey) and self.contains(s.get_location()))
        for i in combined:
            model.remove(i)
        return combined
 
    def contains(self,xy):
        dimension = self.get_dimension()[0]
        correct_dimension = dimension/2
        return self.distance(xy) <= correct_dimension
     
    def display(self,canvas):
        w,h = self.get_dimension()
        width = w/2
        height = h/2
        canvas.create_oval(self._x+width, self._y+height,
                               self._x-width, self._y-height,
                               fill='black')