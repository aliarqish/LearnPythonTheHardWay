class A:
    def A(self):
        print 'I am A'
        
class B:
    def A(sefl):
        print 'I am a'
    def B(self):
        print 'I am B'
        
class C(A,B):
    def C(self):
        print 'I am C'
        
C=C();
C.A()
C.B()
C.C()
