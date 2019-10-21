# Submitter: alvinvn(Nguyen, Alvin)
from goody import type_as_str
import inspect

class Check_All_OK:
    """
    Check_All_OK class implements __check_annotation__ by checking whether each
      annotation passed to its constructor is OK; the first one that
      fails (by raising AssertionError) prints its problem, with a list of all
      annotations being tried at the end of the check_history.
    """
       
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_All_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value,check_history):
        for annot in self._annotations:
            check(param, annot, value, check_history+'Check_All_OK check: '+str(annot)+' while trying: '+str(self)+'\n')


class Check_Any_OK:
    """
    Check_Any_OK implements __check_annotation__ by checking whether at least
      one of the annotations passed to its constructor is OK; if all fail 
      (by raising AssertionError) this classes raises AssertionError and prints
      its failure, along with a list of all annotations tried followed by the
      check_history.
    """
    
    def __init__(self,*args):
        self._annotations = args
        
    def __repr__(self):
        return 'Check_Any_OK('+','.join([str(i) for i in self._annotations])+')'

    def __check_annotation__(self, check, param, value, check_history):
        failed = 0
        for annot in self._annotations: 
            try:
                check(param, annot, value, check_history)
            except AssertionError:
                failed += 1
        if failed == len(self._annotations):
            assert False, repr(param)+' failed annotation check(Check_Any_OK): value = '+repr(value)+\
                         '\n  tried '+str(self)+'\n'+check_history                 



class Check_Annotation():
    # set below name to True for checking to occur
    checking_on  = True
  
    # self._checking_on must also be true for checking to occur
    def __init__(self,f):
        self._f = f
        self._checking_on = True
        
    # Check whether param's annot is correct for value, adding to check_history
    #    if recurs; defines many local function which use it parameters.  
    def check(self,param,annot,value,check_history=''):
        
        # Define local functions for checking, list/tuple, dict, set/frozenset,
        #   lambda/functions, and str (str for extra credit)
        # Many of these local functions called by check, call check on their
        #   elements (thus are indirectly recursive)

        # Decode your annotation here; then check it 
        def check_set_or_frozenset(x,y):
            assert isinstance(value,x), repr(param)+' failed annotation check(wrong type): value = '+repr(value)+\
                                           '\n  was type '+type_as_str(value)+' ...should be type ' +y+'\n'+check_history                 
            if len(annot) == 1:
                empty_list = []
                for a in annot:
                    empty_list.append(a)
                for v in value:
                    self.check(param,empty_list[0],v,check_history+y+' value check: '+str(empty_list[0])+'\n')
                                                     
            else:
                assert False, repr(param)+' annotation inconsistency: '+y+' should have 1 value but had '+str(len(annot))+\
                              '\n  annotation = '+str(annot)+'\n'+check_history
                    
        
                    
        def check_dict():
            assert isinstance(value,dict), repr(param)+' failed annotation check(wrong type): value = '+repr(value)+\
                                           '\n  was type '+type_as_str(value)+' ...should be type dict\n'+check_history                 
            if len(annot) == 1:
                for a in annot.keys():
                    pass
                for b in annot.values():
                    pass
                for x,y in value.items():
                    self.check(param,a,x, check_history+'dict key check: '  +str(a)+'\n')
                    self.check(param,b,y, check_history+'dict value check: '+str(b)+'\n')
                              
            else:
                assert False, repr(param)+' annotation inconsistency: dict should have 1 item but had '+str(len(annot))+\
                              '\n  annotation = '+str(annot)+'\n'+check_history              
                              
                              
        def check_list_or_tuple(x,y):
            assert isinstance(value,x), repr(param)+' failed annotation check(wrong type): value = '+repr(value)+\
                                           '\n  was type '+type_as_str(value)+' ...should be type '+y+'\n'+check_history        
            
            lenght_of_annotation = len(annot)
            lenght_of_value = len(value)         
            if lenght_of_annotation != 1:
                assert lenght_of_annotation == lenght_of_value, repr(param)+' failed annotation check(wrong number of elements): value = '+repr(value)+\
                                                 '\n  annotation had '+str(lenght_of_annotation)+ ' elements'+str(annot)+'\n'+check_history                 
                count = 0
                zipped_annotation_values = zip(annot,value)
                for a,b in zipped_annotation_values:
                    self.check(param,a,b, check_history+y+'['+str(count)+'] check: '+str(annot[count])+'\n')
                    count += 1
            else:
                count = 0
                first_annotation = annot[0]
                for i in value:
                    self.check(param,first_annotation,i,check_history+y+'['+str(count)+'] check: '+str(first_annotation)+'\n')
                    count += 1         

        if annot == None:
            pass
        elif type(annot) is type:
            assert isinstance(value,annot), repr(param)+' failed annotation check(wrong type): value = '+repr(value)+\
                                        '\n  was type '+type_as_str(value)+' ...should be type '+str(annot)[8:11]+'\n'+check_history
        elif type(annot) is set:        check_set_or_frozenset(set,'set')
        elif type(annot) is frozenset:  check_set_or_frozenset(frozenset,'frozenset')                
        elif isinstance(annot,dict):    check_dict()
        elif type(annot) is list:       check_list_or_tuple(list,'list')
        elif type(annot) is tuple:      check_list_or_tuple(tuple,'tuple')
        
        
        else:
            try:
                annot.__check_annotation__(self.check,param,value,check_history)
            except Exception as message:
                if message.__class__ is not AssertionError:
                    assert False, repr(param)+' annotation protocol('+str(annot)+') raised exception'+\
                                 '\n  exception = '+str(message.__class__)[8:11]+': '+str(message)+'\n'+check_history
                else:
                    raise

                    
    # Return result of calling decorated function call, checking present
    #   parameter/return annotations if required
    def __call__(self, *args, **kargs):
        
        # Return a dictionary of the parameter/argument bindings (actually an
        #    ordereddict, in the order parameters occur in the function's header)
        def param_arg_bindings():
            f_signature  = inspect.signature(self._f)
            bound_f_signature = f_signature.bind(*args,**kargs)
            for param in f_signature.parameters.values():
                if param.name not in bound_f_signature.arguments:
                    bound_f_signature.arguments[param.name] = param.default
            return bound_f_signature.arguments

        # If annotation checking is turned off at the class or function level
        #   just return the result of calling the decorated function
        # Otherwise do all the annotation checking
        if Check_Annotation.checking_on == False and self.checking_on == False:
            return self._f(*args,**kargs)
        # On first AssertionError, print the source lines of the function and reraise 
        self._args = param_arg_bindings()
        annot = self._f.__annotations__
        try:
            # Check the annotation for every parameter (if there is one)
            for i in self._args.keys():
                if i not in annot:
                    pass
                else:
                    self.check(i,annot[i],self._args[i])        
            # Compute/remember the value of the decorated function
            answer = self._f(*args,**kargs)
            # If 'return' is in the annotation, check it
            if 'return' not in annot:
                pass
            else:
                self._args['_return'] = answer
                self.check('return',annot['return'],answer)
            # Return the decorated answer
            return answer
        
        # On first AssertionError, print the source lines of the function and reraise 
        except AssertionError:
            #print(80*'-')
            #for l in inspect.getsourcelines(self._f)[0]: # ignore starting line #
            #    print(l.rstrip())
            #print(80*'-')
            raise




  
if __name__ == '__main__':     
    # an example of testing a simple annotation  
    #def f(x:{str}): pass
    #f = Check_Annotation(f)
    #f(3)
    #f({'a',1})
    #f('a')
           
    import driver
    driver.driver()
