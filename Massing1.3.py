import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import math
def rotation(xmin,ymin,x,y,angle):
    #xmin, ymin are the coodinates of the bottom left corner of the rectangle
    #x, y are the width and height of the rectangle
    #angle(in degrees) is angel of the rotation in anti-clockwise direction.
    angle=angle/180*math.pi
    bottom_left=[xmin,ymin]
    top_left=[xmin,ymin+y]
    bottom_right=[xmin+x,ymin]
    top_right=[xmin+x,ymin+y]
    vertices=[bottom_left,bottom_right,top_right,top_left]
    result=[]
    #finding the new coordinates of all the vertices after rotation
    for vertice in vertices:
        x_before,y_before=vertice
        x_after=(x_before-xmin)*math.cos(angle)-(y_before-ymin)*math.sin(angle)+xmin
        y_after=(y_before-ymin)*math.cos(angle)+(x_before-xmin)*math.sin(angle)+ymin
        result.append([round(x_after,1),round(y_after,1)])
    return result

def vector(start_point, end_point):
    #start_point: a list containing the x and y coordinates for the starting point
    #end_point: a list containing the x and y coordinates for the end point
    #output: the vector connecting from start_point to end_point
    x=end_point[0]-start_point[0]
    y=end_point[1]-start_point[1]
    return [x,y]

def vector_product(vectorA,vectorB):
    #input: a list contains the x and y value of a vector
    #output: the cross product of vectorA and vectorB
    result=vectorA[0]*vectorB[1]-vectorB[0]*vectorA[1]
    return result

def intersected(A,B,C,D):
    #input: a list that contains the x and y coordinate of the point
    #output: check whether AB intersects with CD
    AC=vector(A,C)
    AD=vector(A,D)
    BC=vector(B,C)
    BD=vector(B,D)
    CA=vector(C,A)
    CB=vector(C,B)
    DA=vector(D,A)
    DB=vector(D,B)
    return (vector_product(AC,AD)*vector_product(BC,BD)<=0) and (vector_product(CA,CB)*vector_product(DA,DB)<=0)

def overlap(rectangleA,rectangleB):
    #input: a list contains the four coodinates of the rectangle
    #output: check whether the two rectangle overlaps by checking whether they have sides that intersects
    result=False
    Ax_list=[]
    Ay_list=[]
    Bx_list=[]
    By_list=[]
    for i in range(0,4):
        a=(i+1)%4
        Ax_list.append(rectangleA[i][0])
        Bx_list.append(rectangleB[i][0])
        Ay_list.append(rectangleA[i][1])
        By_list.append(rectangleB[i][1])
        for j in range(0,4):
            b=(j+1)%4
            if intersected(rectangleA[i],rectangleA[a],rectangleB[j],rectangleB[b])==True:
                result=True
                break
        if result==True:
            break
    Axmin=min(Ax_list)
    Axmax=max(Ax_list)
    Aymin=min(Ay_list)
    Aymax=max(Ay_list)
    Bxmin=min(Bx_list)
    Bxmax=max(Bx_list)
    Bymin=min(By_list)
    Bymax=max(By_list)
    if (Axmin>Bxmin and Axmax<Bxmax and Aymin>Bymin and Aymax<Bymax) or (Bxmin>Axmin and Bxmax<Axmax and Bymin>Aymin and Bymax<Aymax):
        result=True
    return result
        
def out_of_boundary(rectangle,x_boundary,y_boundary):
    #rectangle: a nested list contains the coodinates of the four vertices
    #x_boundary,y_boundary: a float that is the boundary in x or y direction
    #output: check whether the rectangle is out of boundary of the site area
    x_list=[]
    y_list=[]
    for i in range(0,4):
        x_list.append(rectangle[i][0])
        y_list.append(rectangle[i][1])
    xmin=min(x_list)
    xmax=max(x_list)
    ymin=min(y_list)
    ymax=max(y_list)
    if xmin<0 or xmax>x_boundary or ymin<0 or ymax>y_boundary:
        result=True
    else:
        result=False
    return result
        
def massing(site,building_list,iteration):
    #site is a list of two elements, the length and the width of the buiding site.
    #building_list is a nested list that contains all the buildings. For each building, it is a list contains two values: length and width.
    #iteration is the max iteration for this process
    color_list=['b','c','g','m','r','y']
    solution=[]
    score=1000000000 #the smallest area possible, set to a large number initially
    site_x,site_y=site
    curr_iter=0
    x_min_pre=[0] #The amount of distance has shrunk for each iteration
    y_min_pre=[0]
    while(curr_iter<iteration):
        curr_iter+=1
        position=[] #ramdomly generate the position of each building(Xmin,Ymin)
        z=0 #an indicator of whether the random design fits the constraints
        new_rectangle=[]
        for i in range(0,len(building_list)):
            x_ran=round(random.uniform(0,site_x),1)
            y_ran=round(random.uniform(0,site_y),1)
            angle=round(random.uniform(0,360),1)
            position.append([x_ran,y_ran,angle])
        for j in range(0,len(position)):
            xmin,ymin,angle=position[j]
            x,y=building_list[j]
            rectangle_after=rotation(xmin,ymin,x,y,angle)
            new_rectangle.append(rectangle_after)
            if out_of_boundary(rectangle_after,site_x,site_y)==True:
                z=1
                break
            for k in range(0,len(position)):
                if j==k:
                    pass
                else:
                    x_k_min,y_k_min,angle_k=position[k]
                    x_k,y_k=building_list[k]
                    rectangle_k_after=rotation(x_k_min,y_k_min,x_k,y_k,angle_k)
                    if overlap(rectangle_after,rectangle_k_after)==True:
                        z=1
                        break                            
            if z==1:
                    break
        if z==0:
            x_list=[]
            y_list=[]
            for l in range(0,len(new_rectangle)):
                for m in range(0,4):
                    x_list.append(new_rectangle[l][m][0])
                    y_list.append(new_rectangle[l][m][1])
            xmin=min(x_list)
            xmax=max(x_list)
            ymin=min(y_list)
            ymax=max(y_list)
            score_temp=(xmax-xmin)*(ymax-ymin)
            if score_temp<score:
                score=score_temp
                for n in position:
                    n[0]=n[0]+sum(x_min_pre)
                    n[1]=n[1]+sum(y_min_pre)
                x_min_pre.append(xmin)
                y_min_pre.append(ymin)
                solution=position
                site_x=xmax-xmin
                site_y=ymax-ymin

    fig,ax=plt.subplots()
    ax.set_xlim(0,300)
    ax.set_ylim(0,300)
    for m in range(0,len(solution)):
        xmin,ymin,angle=solution[m]
        x,y=building_list[m]
        rec=mpatches.Rectangle((xmin,ymin),x,y,angle,color=color_list[m])
        ax.add_patch(rec)
    plt.gca().set_aspect("equal")
    plt.show()
    return solution,round(score,2)
print(massing([300,300],[[30,50],[60,100],[90,150]],5000))       
