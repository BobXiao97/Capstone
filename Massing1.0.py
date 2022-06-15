import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

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
        for i in range(0,len(building_list)):
            x_ran=round(random.uniform(0,site_x),1)
            y_ran=round(random.uniform(0,site_y),1)
            position.append([x_ran,y_ran])
        
        for j in range(0,len(position)):
            xmin,ymin=position[j]
            x,y=building_list[j]
            if xmin+x>site_x or ymin+y>site_y:
                z=1
                break
            for k in range(0,len(position)):
                if j==k:
                    pass
                else:
                    x_k_min,y_k_min=position[k]
                    x_k,y_k=building_list[k]
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
            for l in range(0,len(position)):
                xmin,ymin=position[l]
                x,y=building_list[l]
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
        xmin,ymin=solution[m]
        x,y=building_list[m]
        rec=mpatches.Rectangle((xmin,ymin),x,y,color=color_list[m])
        ax.add_patch(rec)
    plt.show()
    return solution,round(score,2)
print(massing([300,300],[[30,50],[60,100],[90,150]],100000))       
