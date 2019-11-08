
import pygame,sys,time,random
from pygame.locals import *
import sqlite3
conn=sqlite3.connect('./src/database_racer_3d.db')
cur=conn.cursor()

import src.Anand_3D


pygame.init()
WIDTH,HEIGHT=1000,600
surface=pygame.display.set_mode((WIDTH,HEIGHT),0,32)
fps=60
ft=pygame.time.Clock()
pygame.display.set_caption('Racer_3D')
white=(255,255,255)
black=(0,0,0)
gray=(128,128,128,128)
green=(0,160,0)
blue=(0,0,128)
walls=(50,0,0)

score_board_font=pygame.font.SysFont('Segoe Print',17,bold=True,italic=False)
timer_font=pygame.font.SysFont('Segoe Print',91,bold=True,italic=False)
replay_font=pygame.font.SysFont('Segoe Print',65,bold=True,italic=False)
city_image=pygame.image.load("./src/city.jpg")
city_image=pygame.transform.scale(city_image,(1000,403))

def set_new_lines(objects):
    for i in range(len(objects)):
        #print (objects[i][0])
        if objects[i][0]=="draw_line" and objects[i][-1]!="dont_change":
            #print ("ooops",objects[1][1][1])
            if objects[i][1][2]<100:
                objects[i][1][2]+=100000
                objects[i][2][2]+=100000
        objects[0][0][0][2],objects[0][0][1][2],objects[0][0][2][2],objects[0][0][3][2]=100000,100000,10,10
        objects[1][1][2],objects[1][2][2]=100,100000
        objects[2][1][2],objects[2][2][2]=100,100000
    return objects

def set_new_cars(objects,speed):
    for i in range(len(objects)):
        #print (objects[i][0])
        if objects[i][-1]=="cars":
            #print ("ooops",objects[1][1][1])
            objects[i][0][0][2]-=(20+speed)
            objects[i][0][1][2]-=(20+speed)
            objects[i][0][2][2]-=(20+speed)
            objects[i][0][3][2]-=(20+speed)
            if objects[i][0][0][2]<-1000:
                temp=random.randint(100000,120000)
                objects[i][0][0][2],objects[i][0][1][2],objects[i][0][2][2],objects[i][0][3][2]=temp,temp,temp,temp
    return objects

def draw_my_cars(objects,surface):
    cars=[]
    for car in objects:
        if car[0]=="others":
            #print (car)
            cars.append([car[0],[car[1]],blue])
    tool_3D.draw_object(cars)

def tilt_view(tool_3D,objects,from_to):
    if from_to=="right" and objects[1][1][0]<=400 and objects[2][1][0]>600:
        objects=tool_3D.move_world(objects,x=-25,y=0,z=0)
        if objects[1][1][0]%200==0:
            from_to="null"
    elif from_to=="left" and objects[1][1][0]<400 and objects[2][1][0]>=600:
        objects=tool_3D.move_world(objects,x=25,y=0,z=0)
        if objects[1][1][0]%200==0:
            from_to="null"
    return objects,from_to

def score_board(score,speed,life,highscore):
    my_score_text=score_board_font.render(str(score),True,blue)
    my_speed_text=score_board_font.render(str(speed)+"  km / h",True,blue)
    my_life_text=score_board_font.render("* "*life,True,blue)
    my_highscore_text=score_board_font.render(str(highscore),True,blue)
    score_text=score_board_font.render("score : ",True,blue)
    speed_text=score_board_font.render("speed : ",True,blue)
    life_text=score_board_font.render("life : ",True,blue)
    highscore_text=score_board_font.render("highscore : ",True,blue)
    surface.blit(score_text,(50,30))
    surface.blit(life_text,(650,30))
    surface.blit(speed_text,(650,60))
    surface.blit(highscore_text,(50,60))
    surface.blit(my_highscore_text,(180,60))
    surface.blit(my_score_text,(150,30))
    surface.blit(my_life_text,(750,30))
    surface.blit(my_speed_text,(750,60))

def set_timer(now):
    time_text=timer_font.render(now,True,walls)
    surface.blit(time_text,(450,230))

def check_crash(objects):
    crashed=0
    for i in range(len(objects)):
        if objects[i][-1]=="cars":
            if objects[i][0][0][0]==425 and objects[i][0][0][2]<125:
                crashed=1
                temp=random.randint(100000,120000)
                objects[i][0][0][2],objects[i][0][1][2],objects[i][0][2][2],objects[i][0][3][2]=temp,temp,temp,temp
    return crashed

def get_highscore():
    cursor=conn.execute("SELECT * from scores;")
    highscore=0
    for row in cursor:
        if row[0]>highscore:
            highscore=row[0]
    return highscore

def set_score(score,speed):
    cur.execute("INSERT into scores values (?,?,?);",(score,time.time(),speed))
    conn.commit()

def crashed_display(score,speed,life):
    roll=True
    #print ("in")
    temp_highscore=get_highscore()
    about_ride1=""
    if score>temp_highscore:
        about_ride="congradulations"
        about_ride1="master"
    else:
        about_ride=random.choice(["marvelous ride","excellent drive","fantastic cuts","extraordinary ride"])
    #about_ride="congradulations"
    #about_ride1="master"
    do_again="let's ride again"
    while roll:
        #surface.fill(white)
        #surface.blit(city_image,(0,0))
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F10:
                    return False
                if event.key==K_SPACE:
                    return True
                if event.key==K_RETURN:
                    return True
        #------work here------
        #score_board(score,speed,life,highscore)
        #print (about_ride)
        if about_ride1!="":
            ride_text=replay_font.render(about_ride,True,walls)
            surface.blit(ride_text,(260,150))
            ride_text=replay_font.render(about_ride1,True,walls)
            surface.blit(ride_text,(320,230))
        else:
            ride_text=replay_font.render(about_ride,True,walls)
            surface.blit(ride_text,(300,150))
        ride_text=replay_font.render(do_again,True,walls)
        surface.blit(ride_text,(300,400))
        #---------------------
        pygame.display.update()
        ft.tick(fps)

def run():
    play="run"
    tool_3D=src.Anand_3D.workon_3D(VP=[WIDTH/2,HEIGHT*5/6,100],TP=[WIDTH/2,HEIGHT*4/6,2500],WIDTH=1000,HEIGHT=600)
    objects=[
    [[[0,550,100000],[1000,550,100000],[1000,550,10],[0,550,10]],gray],
    ["draw_line",[0,550,100],[0,550,100000],3,black],
    ["draw_line",[1000,550,100],[1000,550,100000],3,black]
    ]
    score,level,life=0,0,3
    timer=["3","2","1","GO",""]
    timer_ind=0
    timer_diff=10
    next=10000
    for i in range(10,100000,2000):
        objects.append(["draw_line",[200,550,i],[200,550,i+1000],1,black])
        objects.append(["draw_line",[400,550,i],[400,550,i+1000],1,black])
        objects.append(["draw_line",[600,550,i],[600,550,i+1000],1,black])
        objects.append(["draw_line",[800,550,i],[800,550,i+1000],1,black])
    speed=20
    for i in range(3000,100000,20000):
        x=random.randint(i,i+20000)
        objects.append([[[25,475,x],[175,470,x],[175,550,x],[25,550,x]],blue,"cars"])
        x=random.randint(i,i+20000)
        objects.append([[[225,475,x],[375,470,x],[375,550,x],[225,550,x]],blue,"cars"])
        x=random.randint(i,i+20000)
        objects.append([[[425,475,x],[575,470,x],[575,550,x],[425,550,x]],blue,"cars"])
        x=random.randint(i,i+20000)
        objects.append([[[625,475,x],[775,470,x],[775,550,x],[625,550,x]],blue,"cars"])
        x=random.randint(i,i+20000)
        objects.append([[[825,475,x],[975,470,x],[975,550,x],[825,550,x]],blue,"cars"])
    from_to="null"
    run_status=True
    highscore=get_highscore()
    ind=0
    while play=="run":
        surface.fill(white)
        surface.blit(city_image,(0,0))
        ind+=1
        #print (ind,run_status)
        if timer_ind>len(timer)-2:
            run_status=False
        if not run_status:
            highscore=get_highscore()
            if score>highscore:
                highscore=score
            score+=(speed//10)
            if score>next:
                level+=1
                next+=10000
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==KEYDOWN:
                if event.key==K_F10:
                    play="exit"
                if event.key==K_SPACE:
                    if not run_status:
                        temp=True
                        while temp:
                            for event in pygame.event.get():
                                if event.type==QUIT:
                                    pygame.quit()
                                    sys.exit()
                                if event.type==KEYDOWN:
                                    if event.key==K_F10:
                                        temp=False
                                        play="exit"
                                    if event.key==K_SPACE:
                                        temp=False
                if event.key==K_UP:
                    if not run_status:
                        speed+=20
                if event.key==K_DOWN:
                    if not run_status:
                        speed-=20
                        if speed<20:
                            speed=0
                if event.key==K_RIGHT:
                    #objects=tool_3D.move_world(objects,x=-200,y=0,z=0)
                    if not run_status:
                        from_to="right"
                if event.key==K_LEFT:
                    #objects=tool_3D.move_world(objects,x=200,y=0,z=0)
                    if not run_status:
                        from_to="left"
        #------work here------
        pygame.draw.rect(surface,green,(0,402,1000,200))
        tool_3D.draw_object(objects,surface)
        if timer_ind<len(timer)-1:
            timer_diff-=1
            #print (timer_diff,timer_ind)
            if timer_diff<=0:
                timer_ind+=1
                timer_diff=10
            set_timer(timer[timer_ind])
        elif not run_status:
            objects=set_new_lines(objects)
            objects=tool_3D.move_world(objects,x=0,y=0,z=-speed)
            score_board(score,speed//4,life,highscore)
            objects=set_new_cars(objects,speed)
            life-=check_crash(objects)
            if life<=0:
                play="goto_congrats_page"
                #score_board(score,speed//4,life,highscore)
            objects,from_to=tilt_view(tool_3D,objects,from_to)
        #draw_my_cars(objects,surface)
        #print (len(objects))
        #print (score,next,level,score>next)
        #print (speed,from_to,score)
        #print (objects[210][0][0])
        #---------------------
        pygame.display.update()
        ft.tick(fps)
    #run()
    #print (play)
    play_again=False
    set_score(score,speed//4)
    if score>0 and play=="goto_congrats_page":play_again=crashed_display(score,speed//4,life)
    #print ("after")
    if play_again:
        run()

if __name__=="__main__":
	run()
