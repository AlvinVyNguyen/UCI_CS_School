# A Hunter is both a Mobile_Simulton and a Pulsator in that it updates
#   like a Pulsator, but it also moves (either in a straight line
#   or in pursuit of Prey), and displays as a Pulsator.


from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from prey import Prey
from math import atan2


class Hunter(Pulsator,Mobile_Simulton):
    see_distance = 200
    
    def __init__(self,x,y):   
        Pulsator.__init__(self,x,y)
        width,height = self.get_dimension()
        Mobile_Simulton.__init__(self,x,y,width,height,0,5)
        self.randomize_angle()
        
        
    def update(self,model):
        if not model.find(lambda x : isinstance(x,Prey) and self.distance(x.get_location()) <= Hunter.see_distance):
            pass
        elif model.find(lambda x : isinstance(x,Prey) and self.distance(x.get_location()) <= Hunter.see_distance):
            list_for_min = []
            for i in model.find(lambda x : isinstance(x,Prey) and self.distance(x.get_location()) <= Hunter.see_distance):
                list_for_min.append((self.distance(i.get_location()),i))
            unused,who = min(list_for_min)
            x,y   = who.get_location()
            sx,sy = self.get_location()
            self.set_angle(atan2(y-sy,x-sx))
        self.move()
        return Pulsator.update(self,model)
