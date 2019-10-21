# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole):
    shrink = 30  

    def __init__(self,x,y):   
        Black_Hole.__init__(self,x,y)
        self._counter = 0
        
        
    def update(self,model):
        self._counter += 1
        ate = Black_Hole.update(self,model)
        if self._counter == Pulsator.shrink:
            self.change_dimension(-1,-1)
            if self.get_dimension()[0] != 0:
                pass
            else:
                model.remove(self)
            self._counter = 0
        elif not ate:
            pass
        else:
            self._counter = 0
            self.change_dimension(len(ate),len(ate))
        return ate