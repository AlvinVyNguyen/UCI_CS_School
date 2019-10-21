from goody import type_as_str  # Useful for some exceptions

class DictList:
    def __init__(self,*args):
        assert len(args) > 0, ''
        for i in args:
            assert len(i) > 1, ""
            assert type(i) is dict, ""
        #print('HELLO')
        self.dl = list(args)
        #print(args)
        #print('.')
        #print(self.dl)
    
    def __len__(self):
        a = {i for x in self.dl for i in x}
        return len(a)
    
    def __bool__(self):
        return len(self.dl) > 1
    
    def __repr__(self):
        #print('.')
        #print([str(d) for d in self.dl])
        return 'DictList('+', '.join([str(i) for i in self.dl])+')'
    
    def __contains__(self, arg):
        for i in self.dl:
            if arg in i:
                return True
        return False
        
    def __getitem__(self,arg):
        for i in reversed(self.dl):
            if arg in i:
                return i[arg]
        raise KeyError()
    
    def __setitem__(self,k,v):
        for i in reversed(self.dl):
            if k in i:
                i[k] = v
                return
        set1 = {k:v}
        self.dl.append(set1)
        
    def __delitem__(self,k):
        for i in reversed(self.dl):
            if k in i:
                del i[k]
                return
        raise KeyError()
    
    def __call__(self, k):
        list1 = []
        for i in range(len(self.dl)):
            #print(i)
            #print('step1')
            if k in self.dl[i]:
                #print(k)
                #print('step2')
                #print(self.dl[i])
                #print('step3')
                list1.append((i,self.dl[i][k]))
        return list1
    
    def __iter__(self): 
        empty_set = set()
        for i in reversed(self.dl):
            for k in sorted(i):
                if k not in empty_set:
                    empty_set.add(k)
                    yield k
                    
    def items(self):
        for k in self:
            yield (k,self[k])
            
    def collapse(self):
        pass
    
    def __eq__(self,x):
        a = {k for d in self.dl for k in d}
        if type(x) is dict:
            b = {k for k in x}
        elif type(x) is DictList:
            b = {k for d in self.dl for k in d}
        else:
            raise TypeError()
        return a == b and all(self[i]==x[i] for i in a)
    
    def __lt__(self,k):
        pass
    
    def __gt__(self,k):
        pass
    
    def __add__(self,k):
        pass
    
    def _radd__(self,k):
        pass
    
    
    
        
            
if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test DictList before doing bsc tests
    '''
    d = DictList(dict(a=1,b=2), dict(b=12,c=13))
    print('len(d): ', len(d))
    print('bool(d):', bool(d))
    print('repr(d):', repr(d))
    print(', '.join("'"+x+"'" + ' in d = '+str(x in d) for x in 'abcx'))
    print("d['a']:", d['a'])
    print("d['b']:", d['b'])
    print("d('b'):", d('b'))
    print('iter results:', ', '.join(i for i in d))
    print('item iter results:', ', '.join(str(i) for i in d.items()))
    print('d.collapse():', d.collapse())
    print('d==d:', d==d)
    print('d+d:', d+d)
    print('(d+d).collapse():', (d+d).collapse())
    '''
    
    print()
    import driver
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
