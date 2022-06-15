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

def bounding(rectangle):
    #rectangle is the 4 coodinates of the rectangle (bottom left, bottom right, top right, top left)
    x=[]
    y=[]
    for i in range(0,len(rectangle)):
        x.append(rectangle[i][0])
        y.append(rectangle[i][1])
    xmin=min(x)
    ymin=min(y)
    width=max(x)-min(x)
    height=max(y)-min(y)
    return xmin,ymin,width,height

def massing(site,building_list,iteration):
    #site is a list of two elements, the length and the width of the buiding site.
    #building_list is a nested list that contains all the buildings. For each building, it is a list contains two values: length and width.
    #iteration is the max iteration for this process
    color_list=['b','c','g','m','r','y']
    solution=[]
    score=1000000000 #the smallest area possible, set to a large number initially
    site_x,site_y=site
    curr_iter=0
    while(curr_iter<iteration):
        curr_iter+=1
        position=[] #ramdomly generate the position of each building(Xmin,Ymin)
        z=0 #an indicator of whether the random design fits the constraints
        new_position=[]
        new_building=[]
        for i in range(0,len(building_list)):
            x_ran=round(random.uniform(0,site_x),1)
            y_ran=round(random.uniform(0,site_y),1)
            angle=round(random.uniform(0,360),1)
            position.append([x_ran,y_ran,angle])
        
        for j in range(0,len(position)):
            xmin,ymin,angle=position[j]
            x,y=building_list[j]
            rectangle_after=rotation(xmin,ymin,x,y,angle)
            xmin,ymin,x,y=bounding(rectangle_after)
            new_position.append([xmin,ymin])
            new_building.append([x,y])
            if xmin+x>site_x or ymin+y>site_y or xmin<0 or ymin<0:
                z=1
                break
            for k in range(0,len(position)):
                if j==k:
                    pass
                else:
                    x_k_min,y_k_min,angle_k=position[k]
                    x_k,y_k=building_list[k]
                    rectangle_k_after=rotation(x_k_min,y_k_min,x_k,y_k,angle_k)
                    x_k_min,y_k_min,x_k,y_k=bounding(rectangle_k_after)
                    if xmin>x_k_min+x_k or xmin+x<x_k_min or ymin+y<y_k_min or ymin>y_k_min+y_k:
                        pass                            
                    else:
                        z=1
                        break
            if z==1:
                    break
        if z==0:
            xmin_list=[]
            xmax_list=[]
            ymin_list=[]
            ymax_list=[]
            for l in range(0,len(new_position)):
                xmin,ymin=new_position[l]
                x,y=new_building[l]
                xmax=xmin+x
                ymax=ymin+y
                xmin_list.append(xmin)
                ymin_list.append(ymin)
                xmax_list.append(xmax)
                ymax_list.append(ymax)
            xmin=min(xmin_list)
            xmax=max(xmax_list)
            ymin=min(ymin_list)
            ymax=max(ymax_list)
            score_temp=(xmax-xmin)*(ymax-ymin)
            if score_temp<score:
                score=score_temp
                solution=position

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
print(massing([300,300],[[30,50],[60,100],[90,150]],100000))       
