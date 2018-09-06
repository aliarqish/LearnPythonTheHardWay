class Person:
    def __init__(self):
    
        self.A = 'Yang Li'
        self.__B = 'Yingying Gu'
        
    def PrintName(self):
        print self.A
        print self.__B
        
P = Person()
