class A:
    pass

class B(A):
    pass 

class D: 
    pass 

class C(B, A,D):
    pass 


n = C()