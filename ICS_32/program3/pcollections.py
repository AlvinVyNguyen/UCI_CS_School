# Submitter: alvinvn(Nguyen, Alvin)
import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable=False):
    def show_listing(s):
        for i, l in enumerate(s.split('\n'), 1):
            print('{num: >4} {txt}'.format(num= i, txt= l.rstrip()))

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    def legal_name(a): 
        if type(a) is str:
            if a in keyword.kwlist:
                None
            else:
                if re.match('^([a-z]|[A-Z])(\w*)$',a):
                    return True
        else:
            return False

    def unique_generator(a):
        b = set()
        for i in a:
            if i in b:
                continue
            else: 
                b.add(i)
                yield i
    
    # Validate arguments
    if not legal_name(type_name):
        raise SyntaxError()
    elif type(field_names) is str:
        field_names = field_names.replace(',', ' ')
        field_names = field_names.split()
    elif type(field_names) is not list:
        raise SyntaxError()
    
    list_of_uniques = []
    for a in unique_generator(field_names):
        list_of_uniques.append(a)
        
    for a in list_of_uniques:
        if not legal_name(a):
            raise SyntaxError()
        
    # Define templates to be filled in, becoming definitions
    class_template = '''\
class {type_name}:
    def __init__(self, {fields}):
        {ints_to_initialize}
        self._fields = [{str_field}]
        self._mutable = {mutable}

    def __repr__(self):
        repr = '{type_name}({repr})'
        repr_to_return = repr.format({self_get})
        return repr_to_return
        
    def __getitem__(self,index):
        if type(index) == int:
            if 0 <= index < len(self._fields):
                return 
            else:
                pass
        elif index in self._fields:
            return self.__dict__[index]
        else:
            raise IndexError()

    def __eq__(self,right): #overload the eq operator
        if type(right) is {type_name}:
            pass
        elif type(right) is not {type_name}:
            return False
            
        for i in self._fields:
            if self[i] == right[i]:
                pass
            else:
                return False
        return True
        
    def _replace(self,**kargs):
        if self._mutable != False:
            for a,b in kargs.items():
                self.__dict__[a] = b
            return
        else:
            for a in self._fields:
                if a in kargs:
                    pass
                else:
                    kargs[a] = self.__dict__[a]
            return {type_name}(**kargs)     
'''
    
    get_template = '''\
    def get_{name}(self):
        return self.{name}
''' 
    # Fill-in the class template
    list_fields = []
    for a in field_names:
        list_fields.append(a)
        
    str_list = []
    for b in field_names:
        str_list.append("'"+b+"'")   
    
    init_template = 'self.{name} = {name}'
    repr_template = '{name}'
    self_template = '{name}=self.{name}'
    
    class_definition = class_template.format(
        type_name = type_name,
        fields = ','.join(list_fields),
        str_field = ','.join(str_list),
        ints_to_initialize = ('\n'+(1+2+3+2)*' ').join(init_template.format(name=i) for i in field_names),
        mutable = str(mutable),
        repr = ','.join(i+'={'+repr_template.format(name=i)+'}' for i in field_names),
        self_get = ','.join(self_template.format(name=i) for i in field_names)
    )

    get = ''.join([get_template.format(name=i) for i in field_names])

    class_definition  += get
    # For initial debugging, always show the source code of the class
    #show_listing(class_definition)
    
    # Execute the class_definition string in a local namespace, binding the
    #   name source_code in its dictionary to the class_defintion; return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
    name_space = dict(__name__='pnamedtuple_{type_name}'.format(type_name= type_name))
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except(SyntaxError, TypeError):
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test pnamedtuple in script: e.g., Point = pnamedtuple('Point', 'x y')

    import driver
    driver.driver()
