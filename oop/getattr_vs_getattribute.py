class GetattrVsGetattribute:
    b = 20
    
    def __init__(self, a):
        self.a = a
    
    # def __getattribute__(self, item):
    #     print('__getattribute__')
    #     return object.__getattribute__(self, item)
    
        
    def __setattr__(self, key, value):
        return object.__setattr__(self, key, value)
    
    def __getattr__(self, item):
        print('__getattr__')
        return False
    

        
g_attribute = GetattrVsGetattribute(10)
print(vars(g_attribute))

