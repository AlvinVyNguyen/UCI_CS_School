from goody import type_as_str  # Useful in some exceptions

class DictList:
    def __init__(self,*args):
        assert len(args) > 0, 'DictList.__init__: #args 0: must be >= 1'
        for d in args:
            assert type(d) is dict, "DictList.__init__: "+type_as_str(d)+" is not a dictionary"
            assert len(d) >=1, "DictList.__init__: empty dictionary is not a legal argument"
        self.dl = list(args)
        

    def _all_keys(self):
        return {k for d in self.dl for k in d}
    
 
    def __len__(self):
        return len(self._all_keys())
    

    def __bool__(self):
        return len(self.dl) > 1
    

    def __repr__(self):
        return 'DictList('+', '.join([str(d) for d in self.dl])+')'
    
    
    def __contains__(self,key):
        for d in self.dl:
            if key in d:
                return True
        return False
    

    def __getitem__(self,item):
        for d in reversed(self.dl):
            if item in d:
                return d[item]
        raise KeyError("DictionaryList.__getitem__: item("+str(item)+") is in no dictionary")
    

    def __setitem__(self,key,value):
        for d in reversed(self.dl):
            if key in d:
                d[key] = value
                return
        self.dl.append({key: value})
    

    def __delitem__(self,key):
        for d in reversed(self.dl):
            if key in d:
                del d[key]
                return
        raise KeyError('DictList__delitem__: key('+str(key)+') not found')
    

    def __call__(self,key):
        return [(i,self.dl[i][key]) for i in range(len(self.dl)) if key in self.dl[i]]

  
    def __iter__(self):
        keys_seen = set()
        for d in reversed(self.dl):
            for k in sorted(d):
                if k not in keys_seen:
                    keys_seen.add(k)
                    yield k
                    
 
    def items(self):
        for k in self:
            yield (k,self[k])
                
                
    def collapse(self):
        return {k:v for k,v in self.items()}
    
    
    def __eq__(self,right):
        keys_self  = self._all_keys()
        if type(right) is DictList:
            keys_right = self._all_keys()
        elif type(right) is dict:
            keys_right = {k for k in right}
        else:
            raise TypeError('DictList.__eq__: incompatible type for left('+type_as_str(self)+') and right('+type_as_str(right)+')')
        return keys_self == keys_right and all((self[a]==right[a] for a in keys_self))
        

    def __lt__(self,right):
        keys_self  = self._all_keys()
        if type(right) is DictList:
            keys_right = right._all_keys()
        elif type(right) is dict:
            keys_right = {k for k in right}
        else:
            raise TypeError('DictList.__lt__: incompatible type for left('+type_as_str(self)+') and right('+type_as_str(right)+')')
        return keys_self < keys_right and all(self[a]==right[a] for a in keys_self)
        

    def __gt__(self,right):
        keys_self  = self._all_keys()
        if type(right) is DictList:
            keys_right = right._all_keys()
        elif type(right) is dict:
            keys_right = {k for k in right}
        else:
            raise TypeError('DictList.__gt__: incompatible type for left('+type_as_str(self)+') and right('+type_as_str(right)+')')
        return keys_self > keys_right and all((self[a]==right[a] for a in keys_right))
        

    def __add__(self,right):
        from itertools import chain
        if type(right) is DictList:
            return DictList(*[dict(d) for d in chain(self.dl,right.dl)])
        elif type(right) is dict:
            return DictList(*([dict(d) for d in self.dl]+[dict(right)]))
        else:
            raise TypeError('DictList.__add__: incompatible type for left('+str(self)+' and right('+str(right)+')')
        
    def __radd__(self,left):
        if type(left) is dict:
            return DictList(dict(left),*[dict(d) for d in self.dl])
        else:
            raise TypeError('DictList.__radd__: incompatible type for left('+str(left)+' and right('+str(self)+')')
        
    
    #if your __settattr__ does not work, comment it out so that it won't affect other
    #tests
    def __setattr__(self,name,value):
        assert name == 'dl' and 'dl' not in self.__dict__, 'DictList.__setattr__ attempted to set/reset attribute:'+name
        self.__dict__[name] = value
            
if __name__ == '__main__':
    #Simple tests before running driver
    #Put your own test code here to test DictList before doing bsc tests

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
    
    print()
    import driver
    driver.default_file_name = 'bsc2.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
