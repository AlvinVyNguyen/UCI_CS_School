from collections import defaultdict
from goody import type_as_str

class Bag:
    def __init__(self,values=[]):
        self.counts = defaultdict(int)
        for v in values:
            self.counts[v] += 1

    
    def __str__(self):
        return 'Bag('+', '.join([str(k)+'['+str(v)+']' for k,v in self.counts.items()])+')'


    def __repr__(self):
        param = []
        for k,v in self.counts.items():
            param += v*[k]
        return 'Bag('+str(param)+')'


    def __len__(self):
        return sum(self.counts.values())

        
    def unique(self):
        return len(self.counts)

        
    def __contains__(self,v):
        return v in self.counts

    
    def count(self,v):
        return self.counts[v] if v in self.counts else 0


    def add(self,v):
        self.counts[v] += 1
 
    
    def __add__(self,right):
        if type(right) is not Bag:
            raise TypeError("TypeError: unsupported operand type(s) for +: '"+str(type(self))+"' and'"+str(type(right))+"'")
        return Bag([v for v in self]+[v for v in right])

    
    def remove(self,v):
        if v in self.counts:
            self.counts[v] -= 1
            if self.counts[v] == 0:
                del self.counts[v]
        else:
            raise ValueError('Bag.remove('+str(v)+'): not in Bag')


    def _same(self,right):
        if len(self) != len(right):
            return False
        else:
            for i in self.counts:
                # check not in to avoid creating count of 0 via defaultdict
                if i not in right or self.counts[i] != right.counts[i]:
                    return False
            return True
    
 
    def __eq__(self,right):
        if type(right) != Bag:
            return False
        else:
            return self._same(right)
        

    def __ne__(self,right):
        return not (self == right)


    def __iter__(self):
        def gen(adict):
            for k,v in adict.items():
                for _i in range(v):
                    yield k  
                    
        return gen(dict(self.counts))
    
if __name__ == '__main__':
    #driver tests
    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
