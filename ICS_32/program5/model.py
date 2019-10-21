import controller, sys
import model   #strange, but we need a reference to this module to pass this module to update

from ball      import Ball
from floater   import Floater
from blackhole import Black_Hole
from pulsator  import Pulsator
from hunter    import Hunter
from special import Special

# Global variables: declare them global in functions that assign to them: e.g., ... = or +=
steps  = False
click_object = None
cycles     = 0;
simultons  = set()
starting   = False


#return a 2-tuple of the width and height of the canvas (defined in the controller)
def world():
    return (controller.the_canvas.winfo_width(),controller.the_canvas.winfo_height())

#reset all module variables to represent an empty/stopped simulation
def reset ():
    global steps,starting,simultons,cycles
    steps = False
    starting = False
    simultons   = set()
    cycles = 0;

#start running the simulation
def start ():
    global starting
    starting = True

#stop running the simulation (freezing it)
def stop ():
    global starting
    starting = False

#tep just one update in the simulation
def step ():
    global steps,starting
    steps = True
    starting = True

#remember the kind of object to add to the simulation when an (x,y) coordinate in the canvas
#  is clicked next (or remember to remove an object by such a click)   
def select_object(model_shape):
    global clicking
    clicking = model_shape
    print(model_shape,'is now selected object for clicking')

#add the kind of remembered object to the simulation (or remove any objects that contain the
#  clicked (x,y) coordinate
def mouse_click(x,y):
    if clicking == None:
        print('Select an object to create first')
    elif clicking != 'Remove':
        simultons.add(eval(clicking+'('+str(x)+','+str(y)+')'))
    else:
        for s in find(lambda s : s.contains((x,y))):
            simultons.discard(s)                             

#add simulton s to the simulation
def add(s):
    global simultons
    simultons.add(s)

# remove simulton s from the simulation    
def remove(s):
    global simultons
    simultons.discard(s)

#find/return a set of simultons that each satisfy predicate p    
def find(p):
    #empty = {}
    #for s in simultons:
    #    if p(s):
    #        empty.update(s)
    return {s for s in simultons if p(s)}

#call update for every simulton in the simulation
def update_all():
    global starting, steps
    if not starting:
        pass
    else:
        global cycles,world
        cycles += 1
        
        # if a simulton has been removed. don't call update on it
        original_simultons = set(simultons)
        for s in original_simultons:
            if s not in simultons:
                pass
            else:
                s.update(model)
        if not steps:
            pass
        else:
            starting = False
            steps = False


#delete from the canvas every simulton in the simulation, and then call display for every
#  simulton in the simulation to add it back to the canvas possibly in a new location: to
#  animate it; also, update the progress label defined in the controller
def display_all():
    number_of_simultons = str(len(simultons))
    
    for i in controller.the_canvas.find_all():
        controller.the_canvas.delete(i)
    
    for i in simultons:
        i.display(controller.the_canvas)
        
    controller.the_progress.config(text=str(cycles)+' cycles/'+number_of_simultons+' simultons')
