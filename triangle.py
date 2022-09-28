class Triangle:
  def __init__(self,X1,Y1,X2,Y2,X3,Y3):
    self.X1=X1
    self.Y1=Y1

    self.X2=X2
    self.Y2=Y2

    self.X3=X3
    self.Y3=Y3       

  def triangle_area(self):
    area=abs((0.5)*(self.X1*(self.Y2-self.Y3)+self.X2*(self.Y3-self.Y1)+self.X3*(self.Y1-self.Y2)))
    if area==0:
      print('triangle cannot be formed')
    else:
      print('area : ',area) 

  def rightangle(self):
     
    A = (int(pow((self.X2 - self.X1), 2)) +
         int(pow((self.Y2 - self.Y1), 2)))
    B = (int(pow((self.X3 - self.X2), 2)) +
         int(pow((self.Y3 - self.Y2), 2)))
    C = (int(pow((self.X3 - self.X1), 2)) +
         int(pow((self.Y3 - self.Y1), 2)))

    if ((A > 0 and B > 0 and C > 0) and
        (A == (B + C) or B == (A + C) or
         C == (A + B))):
        print("right angled triangle")
    else:
     print('Not a right angled triangle')

    
t1=Triangle(1,2,3,4,5,6)  
t1.triangle_area()  
#triangle cannot be formed as area is zero
t2=Triangle(0,0,1,2,2,-1)
t2.rightangle()    
t2.triangle_area()