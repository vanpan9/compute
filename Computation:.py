import math
import cmath
class Computation:
    def __init__(self,N,C):
        self.N=N
        self.C=C
    def int_div(self):
        print(f'integer division of {self.N} and {self.C} :',self.N//self.C)
    def remainder(self):
        print('remainder: ', self.N%self.C    )
    def root(self):
        print(f'square root of {self.N} :',math.sqrt(self.N))  
    def complex_no(self):
        c=complex(self.N,self.C)   
        fifth_pow=c**1/5      
        print('complex number: ',c)
        print(f'fifth power of: {c} : ',fifth_pow) 
    def float_div(self):
      div=self.N/self.C
      print(f'float division of {self.N} and {self.C} :',div)
      print(f'{div} raised to the power 3.1415 :',math.pow(div,3.1415))

c=Computation(724,366)
c.int_div()
c.remainder()
c.root()
c.complex_no()       
c.float_div()