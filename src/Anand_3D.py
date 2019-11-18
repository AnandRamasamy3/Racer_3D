

import pygame,sys,time
from pygame.locals import *

from math import *


'''
class plot_3D:
    def __init__(self,VP=[0,0,0],angle=[0,0,0],TP=[0,0,0],R=[1000,600],S=[1000,600],distance=1000,WIDTH=1000,HEIGHT=600):
        self.VP=[VP[0],VP[1],VP[2]]      # camera point
        self.angle=[angle[0],angle[1],angle[2]]   # camera orientation along x, y, z
        self.TP=[TP[0],TP[1],TP[2]]      # target point
        self.R=[R[0],R[1],distance]       # recording display size width, height
        self.S=[S[0],S[1]]       # projecting display size width, height
        self.WIDTH,self.HEIGHT=WIDTH,HEIGHT
    def matrix_multiplication(self,mat1,mat2):
        result=[]
        for i in range(len(mat1)):
            temp=[]
            for j in range(len(mat2[i])):
                sum=0
                for k in range(len(mat1[i])):
                    #print (mat1[i][k],mat2[k][j])
                    #print (i,j,k)
                    sum+=(mat1[i][k]*mat2[k][j])
                temp.append(sum)
            result.append(temp)
        return result
    def move_VP(self,x=0,y=0,z=0):
        self.VP[0]+=x
        self.VP[1]+=y
        self.VP[2]+=z
    def move_TP(self,x=0,y=0,z=0):
        self.TP[0]+=x
        self.TP[1]+=y
        self.TP[2]+=z
    def move_angle(self,x=0,y=0,z=0):
        self.angle[0]=(self.angle[0]+x)%360
        self.angle[1]=(self.angle[1]+y)%360
        self.angle[2]=(self.angle[2]+z)%360
    def convert_to_2D(self,point):
        d=[]
        mat1=[
            [1,0,0],
            [0,cos(radians(self.angle[0])),sin(radians(self.angle[0]))],
            [0,(-1)*sin(radians(self.angle[0])),cos(radians(self.angle[0]))]
        ]
        mat2=[
            [cos(radians(self.angle[1])),0,(-1)*sin(radians(self.angle[1]))],
            [0,1,0],
            [sin(radians(self.angle[1])),0,cos(radians(self.angle[1]))]
        ]
        mat3=[
            [cos(radians(self.angle[2])),sin(radians(self.angle[2])),0],
            [(-1)*sin(radians(self.angle[2])),cos(radians(self.angle[2])),0],
            [0,0,1]
        ]
        mat4=[[point[0]-self.VP[0]],[point[1]-self.VP[1]],[point[2]-self.VP[2]]]
        temp=self.matrix_multiplication(mat1,mat2)
        temp=self.matrix_multiplication(temp,mat3)
        result=self.matrix_multiplication(temp,mat4)
        #print (result)
        dx,dy,dz=result[0][0],result[1][0],result[2][0]
        if dz==0:dz=1
        bx=((self.TP[2]*dx)/dz)+self.TP[0]
        by=((self.TP[2]*dy)/dz)+self.TP[1]
        #print ([bx,by])
        #print (self.SP[2]*dx,self.VP,self.SP)
        return [int(bx),int(by)]

'''


class workon_3D():
    def __init__(self,VP=[0,0,0],angle=[0,0,0],TP=[0,0,0],R=[1000,600],S=[1000,600],distance=1000,WIDTH=1000,HEIGHT=600):
        self.VP=[VP[0],VP[1],VP[2]]      # camera point
        self.angle=[angle[0],angle[1],angle[2]]   # camera orientation along x, y, z
        self.TP=[TP[0],TP[1],TP[2]]      # target point
        self.R=[R[0],R[1],distance]       # recording display size width, height
        self.S=[S[0],S[1]]       # projecting display size width, height
        self.WIDTH,self.HEIGHT=WIDTH,HEIGHT
    def matrix_multiplication(self,mat1,mat2):
        result=[]
        for i in range(len(mat1)):
            temp=[]
            for j in range(len(mat2[i])):
                sum=0
                for k in range(len(mat1[i])):
                    #print (mat1[i][k],mat2[k][j])
                    #print (i,j,k)
                    sum+=(mat1[i][k]*mat2[k][j])
                temp.append(sum)
            result.append(temp)
        return result
    def convert_to_2D(self,point):
        d=[]
        mat1=[
            [1,0,0],
            [0,cos(radians(self.angle[0])),sin(radians(self.angle[0]))],
            [0,(-1)*sin(radians(self.angle[0])),cos(radians(self.angle[0]))]
        ]
        mat2=[
            [cos(radians(self.angle[1])),0,(-1)*sin(radians(self.angle[1]))],
            [0,1,0],
            [sin(radians(self.angle[1])),0,cos(radians(self.angle[1]))]
        ]
        mat3=[
            [cos(radians(self.angle[2])),sin(radians(self.angle[2])),0],
            [(-1)*sin(radians(self.angle[2])),cos(radians(self.angle[2])),0],
            [0,0,1]
        ]
        mat4=[[point[0]-self.VP[0]],[point[1]-self.VP[1]],[point[2]-self.VP[2]]]
        temp=self.matrix_multiplication(mat1,mat2)
        temp=self.matrix_multiplication(temp,mat3)
        result=self.matrix_multiplication(temp,mat4)
        #print (result)
        dx,dy,dz=result[0][0],result[1][0],result[2][0]
        if dz==0:dz=1
        bx=((self.TP[2]*dx)/dz)+self.TP[0]
        by=((self.TP[2]*dy)/dz)+self.TP[1]
        #print ([bx,by])
        #print (self.SP[2]*dx,self.VP,self.SP)
        return [int(bx),int(by)]
    def draw_object(self,objects,surface):
        #plane=plot_3D(VP=[self.VP[0],self.VP[1],self.VP[2]],TP=[self.TP[0],self.TP[1],self.TP[2]],WIDTH=self.WIDTH,HEIGHT=self.HEIGHT)
        #print (objects)
        for line in objects:
            if line[0]=="draw_line":   # "draw_sphere" "draw_box" "draw_character" "draw_lines"
                points=[]
                for point in [line[1],line[2]]:
                    x,y,z=point[0],point[1],point[2]
                    if point[2]>=self.VP[2]+10:points.append(self.convert_to_2D([x,y,z]))
                    else:points.append(self.convert_to_2D([x,y,self.VP[2]]))
                #print ((surface,line[4],points,line[3]))
                pygame.draw.line(surface,line[4],points[0],points[1],line[3])
            elif line[0] in ["draw_sphere","draw_box","draw_character","draw_lines","others"]:
                pass
            else:
                points=[]
                for point in line[0]:
                    x,y,z=point[0],point[1],point[2]
                    if point[2]>=self.VP[2]+10:
                        points.append(self.convert_to_2D([x,y,z]))#
                    else:points.append(self.convert_to_2D([x,y,self.VP[2]]))
                #print (line[0],points)#len()
                if len(points)>2:pygame.draw.polygon(surface,line[1],points)

    def move_world(self,objects,x=0,y=0,z=0):
        for i in range(len(objects)):
            if objects[i][0]=="draw_character" and objects[i][-1]!="dont_change":
                objects[i][2][0]+=x
                objects[i][2][1]+=y
                objects[i][2][2]+=z
            elif objects[i][0]=="draw_sphere" and objects[i][-1]!="dont_change":
                objects[i][1][0]+=x
                objects[i][1][1]+=y
                objects[i][1][2]+=z
            elif objects[i][0]=="draw_box" and objects[i][-1]!="dont_change":
                objects[i][1][0]+=x
                objects[i][1][1]+=y
                objects[i][1][2]+=z
                objects[i][2][0]+=x
                objects[i][2][1]+=y
                objects[i][2][2]+=z
            elif objects[i][0]=="draw_line" and objects[i][-1]!="dont_change":
                objects[i][1][0]+=x
                objects[i][1][1]+=y
                objects[i][1][2]+=z
                objects[i][2][0]+=x
                objects[i][2][1]+=y
                objects[i][2][2]+=z
            elif objects[i][0]=="draw_lines" and objects[i][-1]!="dont_change":
                pass
            elif objects[i][0]=="others" and objects[i][-1]!="dont_change":
                pass
            elif objects[i][-1]!="dont_change":
                for j in range(len(objects[i][0])):
                    objects[i][0][j][0]+=x
                    objects[i][0][j][1]+=y
                    objects[i][0][j][2]+=z
        return objects

    def draw_character(self,objects,xyz=[100,100,200],length_x=100,width_z=80,height_y=200):
        x,y,z=xyz[0],xyz[1],xyz[2]
        points=[]
        for point in objects[0][0]:
            points.append(convert_to_2D([x+(point[0]*length_x),y+(point[1]*height_y),z]))
        pygame.draw.polygon(surface,object[0][1],points)
        points=[]
        for point in objects[0][0]:
            points.append(convert_to_2D([x+(point[0]*length_x),y+(point[1]*height_y),z-width_z]))
        pygame.draw.polygon(surface,(x,y,z),points)

    def draw_move_points(self,surface,color=(0,0,0)):
        pygame.draw.line(surface,color,(self.WIDTH*8.2/10,self.HEIGHT*1/10),(self.WIDTH*9.1/10,self.HEIGHT*1/10),3)
        pygame.draw.line(surface,color,(self.WIDTH*8.5/10,self.HEIGHT*0.3/10),(self.WIDTH*8.5/10,self.HEIGHT*1.4/10),3)
        pygame.draw.line(surface,color,(self.WIDTH*8.7/10,self.HEIGHT*0.5/10),(self.WIDTH*8.35/10,self.HEIGHT*1.3/10),3)
        pygame.draw.circle(surface,color,(int(self.WIDTH*8.2/10),int(self.HEIGHT*1/10)),5)
        pygame.draw.circle(surface,color,(int(self.WIDTH*9.1/10),int(self.HEIGHT*1/10)),5)
        pygame.draw.circle(surface,color,(int(self.WIDTH*8.5/10),int(self.HEIGHT*0.3/10)),5)
        pygame.draw.circle(surface,color,(int(self.WIDTH*8.5/10),int(self.HEIGHT*1.4/10)),5)
        pygame.draw.circle(surface,color,(int(self.WIDTH*8.7/10),int(self.HEIGHT*0.5/10)),5)
        pygame.draw.circle(surface,color,(int(self.WIDTH*8.35/10),int(self.HEIGHT*1.3/10)),5)

    def manage_mouse_click(self,objects,x=0,y=0,z=0):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        if click[0]==1:
            if (int(self.WIDTH*8.2/10)-5)<mouse[0]<(int(self.WIDTH*8.2/10)+5) and (int(self.HEIGHT*1/10)-5)<mouse[1]<(int(self.HEIGHT*1/10)+5):
                #x+=10
                for i in range(len(objects)):
                    if objects[i][0] not in ["draw_character","draw_sphere","draw_box","draw_line","others"] and objects[i][-1]!="dont_change":
                        points=[]
                        for j in range(len(objects[i][0])):
                            objects[i][0][j][0]+=x
            elif (int(self.WIDTH*9.1/10)-5)<mouse[0]<(int(self.WIDTH*9.1/10)+5) and (int(self.HEIGHT*1/10)-5)<mouse[1]<(int(self.HEIGHT*1/10)+5):
                #x-=10
                for i in range(len(objects)):
                    if objects[i][0] not in ["draw_character","draw_sphere","draw_box","draw_line","others"] and objects[i][-1]!="dont_change":
                        points=[]
                        for j in range(len(objects[i][0])):
                            objects[i][0][j][0]-=x
            elif (int(self.WIDTH*8.5/10)-5)<mouse[0]<(int(self.WIDTH*8.5/10)+5) and (int(self.HEIGHT*0.3/10)-5)<mouse[1]<(int(self.HEIGHT*0.3/10)+5):
                #y+=10
                for i in range(len(objects)):
                    if objects[i][0] not in ["draw_character","draw_sphere","draw_box","draw_line","others"] and objects[i][-1]!="dont_change":
                        points=[]
                        for j in range(len(objects[i][0])):
                            objects[i][0][j][1]+=y
            elif (int(self.WIDTH*8.5/10)-5)<mouse[0]<(int(self.WIDTH*8.5/10)+5) and (int(self.HEIGHT*1.4/10)-5)<mouse[1]<(int(self.HEIGHT*1.4/10)+5):
                #y-=10
                for i in range(len(objects)):
                    if objects[i][0] not in ["draw_character","draw_sphere","draw_box","draw_line","others"] and objects[i][-1]!="dont_change":
                        points=[]
                        for j in range(len(objects[i][0])):
                            objects[i][0][j][1]-=y
            elif (int(self.WIDTH*8.7/10)-5)<mouse[0]<(int(self.WIDTH*8.7/10)+5) and (int(self.HEIGHT*0.5/10)-5)<mouse[1]<(int(self.HEIGHT*0.5/10)+5):
                #z-=10;x-=10
                for i in range(len(objects)):
                    if objects[i][0] not in ["draw_character","draw_sphere","draw_box","draw_line"] and objects[i][-1]!="dont_change":
                        points=[]
                        for j in range(len(objects[i][0])):
                            objects[i][0][j][2]-=z
            elif (int(self.WIDTH*8.35/10)-5)<mouse[0]<(int(self.WIDTH*8.35/10)+5) and (int(self.HEIGHT*1.3/10)-5)<mouse[1]<(int(self.HEIGHT*1.3/10)+5):
                #z+=10;x+=10
                for i in range(len(objects)):
                    if objects[i][0] not in ["draw_character","draw_sphere","draw_box","draw_line","others"] and objects[i][-1]!="dont_change":
                        points=[]
                        for j in range(len(objects[i][0])):
                            objects[i][0][j][2]+=z
        return objects

    def move_an_object(self,objects,index=0,x=0,y=0,z=0):
        if objects[index][0] not in ["draw_character","draw_sphere","draw_box","draw_line","draw_lines","others"] and objects[i][-1]!="dont_change":
            points=[]
            for j in range(len(objects[index][0])):
                objects[index][0][j][0]+=x
                objects[index][0][j][1]+=y
                objects[index][0][j][2]+=z
        return objects

    def rotate_a_point(self,point,matrix):
        result=[]
        for i in range(len(matrix)):
            temp=[]
            for j in range(len(point[i])):
                sum=0
                for k in range(len(matrix[i])):
                    #print (mat1[i][k],mat2[k][j])
                    #print (i,j,k)
                    sum+=(matrix[i][k]*point[k][j])
                temp.append(sum)
            result.append(temp)
        return result[0][0],result[1][0],result[2][0]

    def rotate_world(self,objects,x=0,y=0,z=0):
        x_matrix=[[1,0,0],[0,cos(radians(x)),(-1)*(sin(radians(x)))],[0,sin(radians(x)),cos(radians(x))]]
        y_matrix=[[cos(radians(y)),0,sin(radians(y))],[0,1,0],[(-1)*(sin(radians(y))),0,cos(radians(y))]]
        z_matrix=[[cos(radians(z)),(-1)*(sin(radians(z))),0],[sin(radians(z)),cos(radians(z)),0],[0,0,1]]
        matrix=[]
        if x>0:
            for i in x_matrix:
                temp=[]
                for j in i:
                    temp.append(j)
                matrix.append(temp)
        elif y>0:
            for i in y_matrix:
                temp=[]
                for j in i:
                    temp.append(j)
                matrix.append(temp)
        elif z>0:
            for i in z_matrix:
                temp=[]
                for j in i:
                    temp.append(j)
                matrix.append(temp)
        for i in range(len(objects)):
            if objects[i][0]=="draw_character" and objects[i][-1]!="dont_change":
                objects[i][2][0],objects[i][2][1],objects[i][2][2]=rotate_a_point([[objects[i][2][0]],[objects[i][2][1]],[objects[i][2][2]]],matrix)
            elif objects[i][0]=="draw_sphere" and objects[i][-1]!="dont_change":
                objects[i][1][0],objects[i][1][1],objects[i][1][2]=rotate_a_point([[objects[i][1][0]],[objects[i][1][1]],[objects[i][1][2]]],matrix)
            elif objects[i][0]=="draw_box" and objects[i][-1]!="dont_change":
                objects[i][1][0],objects[i][1][1],objects[i][1][2]=rotate_a_point([[objects[i][1][0]],[objects[i][1][1]],[objects[i][1][2]]],matrix)
                objects[i][2][0],objects[i][2][1],objects[i][2][2]=rotate_a_point([[objects[i][2][0]],[objects[i][2][1]],[objects[i][2][2]]],matrix)
            elif objects[i][0]=="draw_line" and objects[i][-1]!="dont_change":
                objects[i][1][0],objects[i][1][1],objects[i][1][2]=rotate_a_point([[objects[i][1][0]],[objects[i][1][1]],[objects[i][1][2]]],matrix)
                objects[i][2][0],objects[i][2][1],objects[i][2][2]=rotate_a_point([[objects[i][2][0]],[objects[i][2][1]],[objects[i][2][2]]],matrix)
            elif objects[i][0]=="draw_lines" and objects[i][-1]!="dont_change":
                pass
            elif objects[i][0]=="others" and objects[i][-1]!="dont_change":
                pass
            elif objects[i][-1]!="dont_change":
                for j in range(len(objects[i][0])):
                    objects[i][0][j][0],objects[i][0][j][1],objects[i][0][j][2]=rotate_a_point([[objects[i][0][j][0]],[objects[i][0][j][1]],[objects[i][0][j][2]]],matrix)
        return objects


#------------
