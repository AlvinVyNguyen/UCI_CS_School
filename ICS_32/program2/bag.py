from collections import defaultdict
from goody import type_as_str

class Bag:
    
    def __init__(self, bags=[]):
        self.bag_int = defaultdict(int)
        for i in bags:
            self.bag_int[i] += 1
    
    def __repr__(self):
        list1 = []
        string1 = ''
        for a,b in self.bag_int.items():
            list1 += b*[a] #3*[4] = [3,3,3,3]
        string1 += 'Bag(' + str(list1) + ')'
        return string1
    
    def __str__(self):
        s = ''
        s += 'Bag('+', '.join([str(a)+'['+str(b)+']' for a,b in self.bag_int.items()])+')'
        return s
    
    def __len__(self):
        return sum(self.bag_int.values())
    
    def unique(self):
        return len(self.bag_int.keys())
    
    def __contains__(self, arg):
        return arg in self.bag_int
    
    def count(self, arg):
        if arg in self.bag_int:
            return self.bag_int[arg]
        else:
            return 0
    
    def add(self, arg):
        self.bag_int[arg] += 1
        
    def __add__(self, arg):
        pass
    
    def remove(self, arg):
        if arg in self.bag_int:
            self.bag_int[arg] -= 1
            if self.bag_int[arg] == 0:
                del self.bag_int[arg]
        else:
            raise ValueError()
        
    def __eq__(self,arg):
        if type(arg) != Bag:
            return False
        else:
            for i in self.bag_int:
                if i not in arg or self.bag_int[i] != arg.bag_int[i]:
                    return False
            return True
    
    def __ne__(self, arg):
        return not (self==arg)
    
    def __iter__(self):
        def gen(arg):
            for a,b in arg.items():
                for c in range(b):
                    yield a  
                    
        return gen(dict(self.bag_int))
        
        

if __name__ == '__main__':
    #driver tests
    import driver
    driver.default_file_name = 'bsc1.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
