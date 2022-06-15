from scipy.optimize import minimize
import cv2
import numpy as np
# For this problem, there are 3 rectangles with the following sizes: 100x80, 50x40 and 30x20.
# The rectangles will be fit in a rectangular area with size 500X300

# initial guess

# x1-x4 are the x coodinate of the vertices of the first rectangle
# y1-y4 are the y coodinate of the vertices of the first rectangle
x1=0
x2=0
x3=100
x4=100
y1=0
y2=80
y3=80
y4=0

# x5-x8 are the x coodinate of the vertices of the second rectangle
# y5-y8 are the y coodinate of the vertices of the second rectangle
x5=150
x6=150
x7=200
x8=200
y5=0
y6=40
y7=40
y8=0

# x9-x12 are the x coodinate of the vertices of the third rectangle
# y9-y12 are the y coodinate of the vertices of the third rectangle
x9=300
x10=300
x11=330
x12=330
y9=0
y10=20
y11=20
y12=0

init_guess=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12]

def objective(x):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=x
    x_cood=x[0:12]
    y_cood=x[12:24]
    x_max=max(x_cood)
    x_min=min(x_cood)
    y_max=max(y_cood)
    y_min=min(y_cood)
    return (x_max-x_min)*(y_max-y_min)

# constraints
# make sure the four vertices form a rectangle: opposite sides equal to each other and diagonals equal to each other
# for the first rectangle
def constraint1(x):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    y1=x[12]
    y2=x[13]
    y3=x[14]
    y4=x[15]
    return (x2-x1)**2+(y2-y1)**2-(x3-x4)**2-(y3-y4)**2

def constraint2(x):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    y1=x[12]
    y2=x[13]
    y3=x[14]
    y4=x[15]
    return (x3-x2)**2+(y3-y2)**2-(x4-x1)**2-(y4-y1)**2

def constraint3(x):
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    y1=x[12]
    y2=x[13]
    y3=x[14]
    y4=x[15]
    return (x3-x1)**2+(y3-y1)**2-(x4-x2)**2-(y4-y2)**2

def constraint4(x):
    x1=x[0]
    x2=x[1]
    y1=x[12]
    y2=x[13]
    return (x2-x1)**2+(y2-y1)**2-80**2

def constraint5(x):
    x2=x[1]
    x3=x[2]
    y2=x[13]
    y3=x[14]
    return (x3-x2)**2+(y3-y2)**2-100**2


# for the second rectangle
def constraint6(x):
    x5=x[4]
    x6=x[5]
    x7=x[6]
    x8=x[7]
    y5=x[16]
    y6=x[17]
    y7=x[18]
    y8=x[19]
    return (x6-x5)**2+(y6-y5)**2-(x7-x8)**2-(y7-y8)**2

def constraint7(x):
    x5=x[4]
    x6=x[5]
    x7=x[6]
    x8=x[7]
    y5=x[16]
    y6=x[17]
    y7=x[18]
    y8=x[19]
    return (x7-x6)**2+(y7-y6)**2-(x8-x5)**2-(y8-y5)**2

def constraint8(x):
    x5=x[4]
    x6=x[5]
    x7=x[6]
    x8=x[7]
    y5=x[16]
    y6=x[17]
    y7=x[18]
    y8=x[19]
    return (x7-x5)**2+(y7-y5)**2-(x8-x6)**2-(y8-y6)**2

def constraint9(x):
    x5=x[4]
    x6=x[5]
    y5=x[16]
    y6=x[17]
    return (x6-x5)**2+(y6-y5)**2-40**2

def constraint10(x):
    x6=x[5]
    x7=x[6]
    y6=x[17]
    y7=x[18]
    return (x7-x6)**2+(y7-y6)**2-50**2

# for the third rectangle
def constraint11(x):
    x9=x[8]
    x10=x[9]
    x11=x[10]
    x12=x[11]
    y9=x[20]
    y10=x[21]
    y11=x[22]
    y12=x[23]
    return (x10-x9)**2+(y10-y9)**2-(x11-x12)**2-(y11-y12)**2

def constraint12(x):
    x9=x[8]
    x10=x[9]
    x11=x[10]
    x12=x[11]
    y9=x[20]
    y10=x[21]
    y11=x[22]
    y12=x[23]
    return (x11-x10)**2+(y11-y10)**2-(x12-x9)**2-(y12-y9)**2

def constraint13(x):
    x9=x[8]
    x10=x[9]
    x11=x[10]
    x12=x[11]
    y9=x[20]
    y10=x[21]
    y11=x[22]
    y12=x[23]
    return (x11-x9)**2+(y11-y9)**2-(x12-x10)**2-(y12-y10)**2

def constraint14(x):
    x9=x[8]
    x10=x[9]
    y9=x[20]
    y10=x[21]
    return (x10-x9)**2+(y10-y9)**2-20**2

def constraint15(x):
    x10=x[9]
    x11=x[10]
    y10=x[21]
    y11=x[22]
    return (x11-x10)**2+(y11-y10)**2-30**2

# No rotation(just for now)
def constraint16(x):
    return x[0]-x[1]

def constraint17(x):
    return x[4]-x[5]

def constraint18(x):
    return x[8]-x[9]

# rec1 and rec2 do not overlap
def constraint19(x):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=x
    rec1_xmax=max(x1,x2,x3,x4)
    rec2_xmax=max(x5,x6,x7,x8)
    rec1_xmin=min(x1,x2,x3,x4)
    rec2_xmin=min(x5,x6,x7,x8)
    return -1*(rec1_xmax-rec2_xmin)*(rec2_xmax-rec1_xmin)

def constraint20(x):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=x
    rec1_ymax=max(y1,y2,y3,y4)
    rec2_ymax=max(y5,y6,y7,y8)
    rec1_ymin=min(y1,y2,y3,y4)
    rec2_ymin=min(y5,y6,y7,y8)
    return -1*(rec1_ymax-rec2_ymin)*(rec2_ymax-rec1_ymin)

# rec1 and rec3 do not overlap
def constraint21(x):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=x
    rec1_xmax=max(x1,x2,x3,x4)
    rec3_xmax=max(x9,x10,x11,x12)
    rec1_xmin=min(x1,x2,x3,x4)
    rec3_xmin=min(x9,x10,x11,x12)
    return -1*(rec1_xmax-rec3_xmin)*(rec3_xmax-rec1_xmin)

def constraint22(x):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=x
    rec1_ymax=max(y1,y2,y3,y4)
    rec3_ymax=max(y9,y10,y11,y12)
    rec1_ymin=min(y1,y2,y3,y4)
    rec3_ymin=min(y9,y10,y11,y12)
    return -1*(rec1_ymax-rec3_ymin)*(rec3_ymax-rec1_ymin)

# rec2 and rec3 do not overlap
def constraint23(x):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=x
    rec2_xmax=max(x5,x6,x7,x8)
    rec3_xmax=max(x9,x10,x11,x12)
    rec2_xmin=min(x5,x6,x7,x8)
    rec3_xmin=min(x9,x10,x11,x12)
    return -1*(rec3_xmax-rec2_xmin)*(rec2_xmax-rec3_xmin) 

def constraint24(x):
    x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=x
    rec2_ymax=max(y5,y6,y7,y8)
    rec3_ymax=max(y9,y10,y11,y12)
    rec2_ymin=min(y5,y6,y7,y8)
    rec3_ymin=min(y9,y10,y11,y12)
    return -1*(rec3_ymax-rec2_ymin)*(rec2_ymax-rec3_ymin)

x_bound=(0,500)
y_bound=(0,300)
bnds=(x_bound,x_bound,x_bound,x_bound,x_bound,x_bound,x_bound,x_bound,x_bound,x_bound,x_bound,x_bound,y_bound,y_bound,y_bound,y_bound,y_bound,y_bound,y_bound,y_bound,y_bound,y_bound,y_bound,y_bound)
con1={'type':'eq','fun':constraint1}
con2={'type':'eq','fun':constraint2}
con3={'type':'eq','fun':constraint3}
con4={'type':'eq','fun':constraint4}
con5={'type':'eq','fun':constraint5}
con6={'type':'eq','fun':constraint6}
con7={'type':'eq','fun':constraint7}
con8={'type':'eq','fun':constraint8}
con9={'type':'eq','fun':constraint9}
con10={'type':'eq','fun':constraint10}
con11={'type':'eq','fun':constraint11}
con12={'type':'eq','fun':constraint12}
con13={'type':'eq','fun':constraint13}
con14={'type':'eq','fun':constraint14}
con15={'type':'eq','fun':constraint15}
con16={'type':'eq','fun':constraint16}
con17={'type':'eq','fun':constraint17}
con18={'type':'eq','fun':constraint18}
con19={'type':'eq','fun':constraint19}
con20={'type':'eq','fun':constraint20}
con21={'type':'eq','fun':constraint21}
con22={'type':'eq','fun':constraint22}
con23={'type':'eq','fun':constraint23}
con24={'type':'eq','fun':constraint24}


cons=([con1,con2,con3,con4,con5,con6,con7,con8,con9,con10,con11,con12,con13,con14,con15,con16,con17,con18,con19,con20,con21,con22,con23,con24])
solution=minimize(objective,init_guess,method='SLSQP',bounds=bnds,constraints=cons)

# plotting the arrangement out
# cv2.rectangle only takes in integer coodinates of there might be some inconsistancy
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12=solution.x
print(solution)
image=np.zeros((300,500,3),np.uint8)
color=(0,255,0)
cv2.rectangle(image,(int(x1),int(y1)),(int(x3),int(y3)),(0,255,0),thickness=-1)
cv2.rectangle(image,(int(x5),int(y5)),(int(x7),int(y7)),(255,0,0),thickness=-1)
cv2.rectangle(image,(int(x9),int(y9)),(int(x11),int(y11)),(0,0,255),thickness=-1)
cv2.imshow("Arrangement",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

    