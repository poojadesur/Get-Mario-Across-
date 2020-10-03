
import pygame
import random

from pygame import mixer
from config import *

pygame.init()
pygame.font.init()
done = False

pygame.display.update()

clock = pygame.time.Clock()

#background image
bg = pygame.image.load("bg2.jpg").convert()

# mario music in background
mixer.music.load("SuperMarioBros.wav")
mixer.music.play(0)

#starting out coordinates for each icon
yoshix = 25  
yoshiy = 25
myoshix = 25 + 5
myoshiy = 25 + 10
yoshi2x = 900  
yoshi2y = 940
myoshi2x = 900 + 5
myoshi2y = 940 + 10


obstacles = pygame.sprite.Group()

sObstacles = pygame.sprite.Group()

classYoshi = pygame.sprite.Group()

mcounterx = 0
mcountery = 0
scounterx = 0
scountery = 0
movex = 0
movey = 200
staticy = 110

#creating moving obstacles
while mcountery < 5:

    while mcounterx < 7:
        obst = Obstacle(movex, movey)
        obstacles.add(obst)
        movex += 200
        mcounterx += 1

    movey += 150
    mcountery += 1
    mcounterx = 0

#creating static obstacles
while scountery < 6:

    limit = random.randint(3, 5)
    rlist = [
        0,
        50,
        100,
        150,
        200,
        250,
        300,
        350,
        400,
        450,
        500,
        550,
        600,
        650,
        700,
        750,
        800,
        850,
        900,
        950]

    while scounterx < limit:
        staticx = random.choice(rlist)
        sobst = sObstacle(staticx, staticy)
        sObstacles.add(sobst)
        scounterx += 1
    staticy += 150
    scountery += 1
    scounterx = 0

#counters to keep track of how long player1 and player2 are playing
time1 = 0
time2 = 0

#this flag represents which player is currently playing, flag 0 is for player1 and flag1 is for player2
flag = 0 

#position of first boundary and river from top
p1wood = 185  
p1water = 275
score1 = 0

#position of first boundary and river from bottom
p2wood = 875  
p2water = 785
score2 = 0

noOfRounds = 0
nor = 1 

speed1 = 1
speed2 = 1

#number of wins player 1 has
won1 = 0  
#number of wins player 2 has
won2 = 0  

end_it=False
done2 = False
while (end_it==False):
    screen.blit(bg,[0,0])
    
    nlabel=myfont3.render("Welcome to Mario and Yoshi!!!", 1, (0, 0, 0))
    text = myfont.render("How To Play",1,(0,0,0))
    instr = pygame.image.load("instr.jpeg")
    instr = pygame.transform.scale(instr, (500, 500))
    screen.blit(text,(350,200))
    screen.blit(instr,(250,300))
    text3 = myfont.render("Press Space to Start!",1,(0,0,0))
    screen.blit(text3,(250,900))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                end_it=True
    screen.blit(nlabel,(50,100))
    pygame.display.flip()
    

while not done:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    #when 3 rounds have finished, to declare the winner of the game
    if nor == 4:
        pygame.display.flip()
        if won2 > won1:
            p2winner()
        else:
            p1winner()

        pygame.display.flip()
        pygame.time.wait(2500)
        time1 = 0
        time2 = 0
        flag = 0
        p1wood = 185
        p1water = 275
        score1 = 0
        p2wood = 875
        p2water = 785
        score2 = 0
        noOfRounds = 0
        nor = 1
        speed1 = 1
        speed2 = 1
        won1 = 0
        won2 = 0
        yoshix = 25 
        yoshiy = 25
        myoshix = 25 + 5
        myoshiy = 25 + 10

    #the outcome of each round
    if noOfRounds == nor:
        if score2 < score1:
            p1roundwinner()
            won1 += 1
        if score2 > score1:
            p2roundwinner()
            won2 += 1
        if score2 == score1:
            if time2 > time1:
                p1roundwinner()
                won1 += 1
            else:
                p2roundwinner()
                won2 += 1
        speed1 += 1
        speed2 += 1
        score1 = 0
        score2 = 0
        nor += 1
        time1 = 0
        time2 =0
        pygame.display.flip()
        pygame.time.delay(1000)
        if nor == 4:
            continue

    if 1 < 2:  # background
        screen.blit(bg,[0,0])
        pygame.draw.lines(
            screen, colorsafe, False, [
                (0, 150), (1000, 150)], 60)
        pygame.draw.lines(
            screen, colorsafe, False, [
                (0, 300), (1000, 300)], 60)
        pygame.draw.lines(
            screen, colorsafe, False, [
                (0, 450), (1000, 450)], 60)
        pygame.draw.lines(
            screen, colorsafe, False, [
                (0, 600), (1000, 600)], 60)
        pygame.draw.lines(
            screen, colorsafe, False, [
                (0, 750), (1000, 750)], 60)
        pygame.draw.lines(
            screen, colorsafe, False, [
                (0, 900), (1000, 900)], 60)

    #keyboard movements for player one is up,down,left and right arrow keys
    #keyboard movements for player two is w,s,a,d respectively
    pressed = pygame.key.get_pressed()
   
    #while player1 is being moved
    if flag is 0:
        if pressed[pygame.K_UP]:
            if yoshiy >= 0:
                yoshiy -= 3
                myoshiy -= 3
        if pressed[pygame.K_DOWN]:
            if yoshiy <= 950:
                yoshiy += 3
                myoshiy += 3
        if pressed[pygame.K_LEFT]:
            if yoshix >= 0:
                yoshix -= 3
                myoshix -= 3
        if pressed[pygame.K_RIGHT]:
            if yoshix <= 925:
                yoshix += 3
                myoshix += 3

    #while player2 is being moved
    if flag is 1:
        if pressed[ord('w')]:
            if yoshi2y >= 0:
                yoshi2y -= 3
                myoshi2y -= 3
        if pressed[ord('s')]:
            if yoshi2y <= 950:
                yoshi2y += 3
                myoshi2y += 3
        if pressed[ord('a')]:
            if yoshi2x >= 0:
                yoshi2x -= 3
                myoshi2x -= 3
        if pressed[ord('d')]:
            if yoshi2x <= 925:
                yoshi2x += 3
                myoshi2x += 3

    #when player 1 is playing
    if flag is 0:

        #timer of player1 starts incrementing
        #text on upper right hand corner updates
        
        time1 += 1

        text = myfont.render('START', False, (0, 0, 0))
        screen.blit(text, (425, 25))
        text = myfont.render('END', False, (0, 0, 0))
        screen.blit(text, (425, 950))
        text = myfont2.render('PLAYER 1\'s TURN', False, (0, 0, 0))
        screen.blit(text, (700, 50))
        text = myfont2.render('PLAYER 1 SCORE: ' + str(score1), False, (0, 0, 0))
        screen.blit(text, (700, 75))
        text = myfont2.render('Level ' + str(nor), False, (0, 0, 0))
        screen.blit(text, (700, 25))

        yoshi = Yoshi(yoshix, yoshiy)
        classYoshi.add(yoshi)
        yoshi2 = Yoshi(yoshi2x, yoshi2y)
        classYoshi.add(yoshi2)

        xmoveflag = 0
        ymoveflag = 0

        #collision code for moving obstacles
        for obst in obstacles:

            if obst.movex + 45 >= myoshix and obst.movex + 45 <= myoshix + 60:
                xmoveflag = 1
            if obst.movey + 45 >= myoshiy and obst.movey + 45 <= myoshiy + 60:
                ymoveflag = 1               
            if xmoveflag == 1 and ymoveflag == 1:
                text = myfont2.render('time:' + str(time1), False, (0, 0, 0))
                screen.blit(text, (815, 25))
                pygame.display.flip()
                p1water = 275
                p1wood = 185
                yoshi.hit()
                yoshix = 25
                yoshiy = 25
                myoshix = 25 + 5
                myoshiy = 25 + 10
                flag = 1

            xmoveflag = 0
            ymoveflag = 0

            if obst.movex + 5 <= myoshix + 60 and obst.movex + 5 >= myoshix:
                xmoveflag = 1
            if obst.movey + 5 <= myoshiy + 60 and obst.movey + 5 >= myoshiy:
                ymoveflag = 1
            if xmoveflag == 1 and ymoveflag == 1:
                text = myfont2.render('time:' + str(time1), False, (0, 0, 0))
                screen.blit(text, (815, 25))
                pygame.display.flip()
                flag = 1
                p1water = 275
                p1wood = 185
                yoshi.hit()
                yoshix = 25
                yoshiy = 25
                myoshix = 25 + 5
                myoshiy = 25 + 10

            xmoveflag = 0
            ymoveflag = 0

            #update screen
            obst.movex += speed1
            obst.movex %= 1000
            obst.render(screen)
            yoshi.render2(screen)
            yoshi2.render(screen)

        # ALL CODE FOR STATIC OBST STARTS HERE
        xstaticflag = 0
        ystaticflag = 0
        
        #collision code for stationary obstacles while player1 is playing
        for sobst in sObstacles:

            if sobst.staticx + 60 >= myoshix and sobst.staticx + 60 <= myoshix + 75:
                xstaticflag = 1
            if sobst.staticy + 72 >= myoshiy and sobst.staticy + 72 <= myoshiy + 75:
                ystaticflag = 1
            if xstaticflag == 1 and ystaticflag == 1:
                text = myfont2.render('time:' + str(time1), False, (0, 0, 0))
                screen.blit(text, (815, 25))
                pygame.display.flip()
                flag = 1
                p1water = 275
                p1wood = 185
                yoshi.hit()
                yoshix = 25
                yoshiy = 25
                myoshix = 25 + 5
                myoshiy = 25 + 10

            xstaticflag = 0
            ystaticflag = 0
            if sobst.staticx + 15 <= myoshix + 75 and sobst.staticx + 15 >= myoshix:
                xstaticflag = 1
            if sobst.staticy + 2 <= myoshiy + 75 and sobst.staticy + 2 >= myoshiy:
                ystaticflag = 1
            if xstaticflag == 1 and ystaticflag == 1:
                text = myfont2.render('time:' + str(time1), False, (0, 0, 0))
                screen.blit(text, (815, 25))
                pygame.display.flip()
                p1water = 275
                p1wood = 185
                flag = 1
                yoshi.hit()
                yoshix = 25
                yoshiy = 25
                myoshix = 25 + 5
                myoshiy = 25 + 10

            xstaticflag = 0
            ystaticflag = 0

            #update screen
            sobst.render(screen)
            yoshi.render2(screen)
            yoshi2.render(screen)

        #as long as player1 has not died yet
        if flag == 0:
            if yoshiy >= 940:
                yoshi.success()
                flag = 1
                yoshix = 25
                yoshiy = 25
                myoshix = 25 + 5
                myoshiy = 25 + 10
                p1water = 275
                p1wood = 185
            #crossing the stationary obstacles
            if myoshiy >= p1wood - 3:
                score1 += 5
                p1wood += 150
            #crossing the moving obstacles
            if myoshiy >= p1water - 3:
                score1 += 10
                p1water += 150

        pygame.display.flip()
        continue

    
    #when player 2 is playing
    if flag is 1:

        time2 += 1
        
        text = myfont.render('END', False, (0, 0, 0))
        screen.blit(text, (425, 25))
        text = myfont.render('START', False, (0, 0, 0))
        screen.blit(text, (425, 950))
        text = myfont2.render('PLAYER 2\'s TURN', False, (0, 0, 0))
        screen.blit(text, (700, 50))
        text = myfont2.render('PLAYER 2 SCORE: ' + str(score2), False, (0, 0, 0))
        screen.blit(text, (700, 75))
        text = myfont2.render('Level ' + str(nor), False, (0, 0, 0))
        screen.blit(text, (700, 25))

        yoshi = Yoshi(yoshix, yoshiy)
        classYoshi.add(yoshi)
        yoshi2 = Yoshi(yoshi2x, yoshi2y)
        classYoshi.add(yoshi2)

        yoshi.render2(screen)
        yoshi2.render(screen)

        xmoveflag = 0
        ymoveflag = 0

        #collision code for moving obstacles while player2 is playing
        for obst in obstacles:

            if obst.movex + 45 >= myoshi2x and obst.movex + 45 <= myoshi2x + 60:
                xmoveflag = 1
            if obst.movey + 45 >= myoshi2y and obst.movey + 45 <= myoshi2y + 60:
                ymoveflag = 1
            if xmoveflag == 1 and ymoveflag == 1:
                text = myfont2.render('time:' + str(time2), False, (0, 0, 0))
                screen.blit(text, (815, 25))
                pygame.display.flip()
                flag = 0
                p2wood = 875
                p2water = 785
                noOfRounds += 1
                yoshi.hit()
                yoshi2x = 900
                yoshi2y = 940
                myoshi2x = 900 + 5
                myoshi2y = 940 + 10
                pygame.time.wait(1000)

            xmoveflag = 0
            ymoveflag = 0

            if obst.movex + 5 <= myoshi2x + 60 and obst.movex + 5 >= myoshi2x:
                xmoveflag = 1
            if obst.movey + 5 <= myoshi2y + 60 and obst.movey + 5 >= myoshi2y:
                ymoveflag = 1
            if xmoveflag == 1 and ymoveflag == 1:
                text = myfont2.render('time:' + str(time2), False, (0, 0, 0))
                screen.blit(text, (815, 25))
                pygame.display.flip()
                flag = 0
                p2wood = 875
                p2water = 785
                noOfRounds += 1
                yoshi.hit()
                yoshi2x = 900
                yoshi2y = 940
                myoshi2x = 900 + 5
                myoshi2y = 940 + 10

            xmoveflag = 0
            ymoveflag = 0

            obst.movex += speed2
            obst.movex %= 1000
            obst.render(screen)
            yoshi.render2(screen)
            yoshi2.render(screen)

        # ALL CODE FOR STATIC OBST STARTS HERE
        xstaticflag = 0
        ystaticflag = 0
        
        #collision code for stationary obstacles while player1 is playing
        for sobst in sObstacles:

            if sobst.staticx + 60 >= myoshi2x and sobst.staticx + 60 <= myoshi2x + 75:
                xstaticflag = 1
            if sobst.staticy + 72 >= myoshi2y and sobst.staticy + 72 <= myoshi2y + 75:
                ystaticflag = 1
            if xstaticflag == 1 and ystaticflag == 1:
                text = myfont2.render('time:' + str(time2), False, (0, 0, 0))
                screen.blit(text, (815, 25))
                pygame.display.flip()
                flag = 0
                p2wood = 875
                p2water = 785
                noOfRounds += 1
                yoshi.hit()
                yoshi2x = 900
                yoshi2y = 940
                myoshi2x = 900 + 5
                myoshi2y = 940 + 10

            xstaticflag = 0
            ystaticflag = 0
            if sobst.staticx + 15 <= myoshi2x + 75 and sobst.staticx + 15 >= myoshi2x:
                xstaticflag = 1
            if sobst.staticy + 2 <= myoshi2y + 75 and sobst.staticy + 2 >= myoshi2y:
                ystaticflag = 1
            if xstaticflag == 1 and ystaticflag == 1:
                text = myfont2.render('time:' + str(time2), False, (0, 0, 0))
                screen.blit(text, (815, 25))
                pygame.display.flip()
                flag = 0
                p2wood = 875
                p2water = 785
                noOfRounds += 1
                yoshi.hit()
                yoshi2x = 900
                yoshi2y = 940
                myoshi2x = 900 + 5
                myoshi2y = 940 + 10

            xstaticflag = 0
            ystaticflag = 0

            sobst.render(screen)
            yoshi.render2(screen)
            yoshi2.render(screen)

        #as long as player2 has not died
        if flag == 1:
            if yoshi2y <= 50:
                yoshi2.success()
                flag = 0
                yoshi2x = 900
                yoshi2y = 940
                myoshi2x = 900 + 5
                myoshi2y = 940 + 10
                noOfRounds += 1
            #crossing the stationary obstacles
            if myoshi2y + 75 <= p2wood + 3:
                score2 += 5
                p2wood -= 150
            #crossing the moving obstacles
            if myoshi2y + 75 <= p2water + 3:
                score2 += 10
                p2water -= 150

    pygame.display.flip()
    
    clock.tick(60)
