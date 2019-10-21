# Defines a special exception for use with the Graph class methods
# Use like any exception: e.g., raise GraphError('Graph.method: ...error indication...')
class GraphError(Exception):
    pass # Inherit all methods, including __init__
 
 
class Graph:
    def __init__(self,*args):
        self.edges = {}
        # You may not define any other attributes
        # Other methods will examine/update the edges attribute
 

    def __setitem__(self,o,d):
        if type(o) == str and type(d) == str:
            if d not in self.edges:
                self.edges[d] = [set(), set()]
            if o not in self.edges:
                self.edges[o] = [set(), set()]
            self.edges[o][0] = {d}
            self.edges[d][1] = {o}
        else:
            raise GraphError
 
 
    def __getitem__(self,item):
        print(item)
        if len(item) == 1:
            return self.edges[item][0]
        if len(item) > 1:
            return item in self.edges.values()
        else:
            raise GraphError     
     

    def __len__(self):
        a = set()
        for i in self.edges.keys():
            for x in self.edges[i][0]:
                a.add((i,x))
        return len(a)    
 
     
    def __call__(self,d):
        return self.edges[d][1]    


    def degree(self,n):
        pass     
 
     
    def __contains__(self,item):
        pass     
     

    def __iter__(self):
        for o in sorted(self.edges):
            if self.edges[o] == {}: #and not any(o in d for d in self.edges.values()):
                yield o
            else:
                for d in sorted(self[o]):
                    yield (o,d,self[o,d])     


    def __le__(self,right):
        pass     
         
 
    def __delitem__(self,item):
        pass     
 
 
     
##############################
 
 
if __name__ == '__main__':
    # Put code here for simpler debugging of exceptions (comapred to bsc.txt)


    
    import driver
    #Uncomment the following lines to see MORE details on exceptions
    #But probably better to write code above
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
    driver.driver()
