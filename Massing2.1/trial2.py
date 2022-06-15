# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 03:02:47 2021

@author: Xiao Tianqi
"""
from scipy.optimize import minimize
import cv2
import numpy as np
# For this problem, there are 3 rectangles with the following sizes: 100x80, 50x40 and 30x20.
# The rectangles will be fit in a rectangular area with size 500X300

# initial guess

# x1 is the x coodinate of the vertice of the bottom left corner of the first rectangle
# y1 is the y coodinate of the vertice of the bottom left corner of the first rectangle
x1=0
y1=0


# x2 is the x coodinate of the vertice of the bottom left corner of the second rectangle
# y2 is the y coodinate of the vertice of the bottom left corner of the second rectangle
x2=100
y2=0

# x2 is the x coodinate of the vertice of the bottom left corner of the third rectangle
# y2 is the y coodinate of the vertice of the bottom left corner of the third rectangle
x3=150
y3=0

init_guess=[x1,x2,x3,y1,y2,y3]

def objective(x):
    x1,x2,x3,y1,y2,y3=x
    x_max=max(x1+100,x2+50,x3+30)
    x_min=min(x1,x2,x3)
    y_max=max(y1+80,y2+40,y3+20)
    y_min=min(y1,y2,y3)
    return (x_max-x_min)*(y_max-y_min)

# constraints
# rec1 and rec2 do not overlap
def constraint1(x):
    x1,x2,x3,y1,y2,y3=x
    return -(x1+100-x2)

def constraint2(x):
    x1,x2,x3,y1,y2,y3=x
    return -(x2+50-x1)

# rec1 and rec3 do not overlap
def constraint3(x):
    x1,x2,x3,y1,y2,y3=x
    return -(x1+100-x3)

def constraint4(x):
    x1,x2,x3,y1,y2,y3=x
    return -(x3+30-x1)

# rec2 and rec3 do not overlap
def constraint5(x):
    x1,x2,x3,y1,y2,y3=x
    return -(x3+30-x2)

def constraint6(x):
    x1,x2,x3,y1,y2,y3=x
    return -(x2+50-x3)


bnds=((0,400),(0,450),(0,470),(0,220),(0,260),(0,280))
con1={'type':'ineq','fun':constraint1}
con2={'type':'ineq','fun':constraint2}
con3={'type':'ineq','fun':constraint3}
con4={'type':'ineq','fun':constraint4}
con5={'type':'ineq','fun':constraint5}
con6={'type':'ineq','fun':constraint6}


cons=([con1,con2,con3,con4,con5,con6])
solution=minimize(objective,init_guess,method='SLSQP',bounds=bnds,constraints=cons)

# plotting the arrangement out
# cv2.rectangle only takes in integer coodinates of there might be some inconsistancy
print(solution)
x1,x2,x3,y1,y2,y3=solution.x
image=np.zeros((300,500,3),np.uint8)
color=(0,255,0)
cv2.rectangle(image,(int(x1),int(y1)),(int(x1+100),int(y1+80)),(0,255,0),thickness=-1)
cv2.rectangle(image,(int(x2),int(y2)),(int(x2+50),int(y2+40)),(255,0,0),thickness=-1)
cv2.rectangle(image,(int(x3),int(y3)),(int(x3+30),int(y3+20)),(0,0,255),thickness=-1)
cv2.imshow("Arrangement",image)
cv2.waitKey(0)
cv2.destroyAllWindows()
