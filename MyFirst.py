import pygame
import os
import math
import random

#initailize pygame modules
pygame.init()

#for display
run=True
WIDTH,HEIGHT=800,600
WHITE=(255,255,255)
win=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("HangMan Game")

#frame per second for display window
FPS=60
clock=pygame.time.Clock()

#game words
word_grp=["WORK","PLAY","DEVELOPER","PYTHON","SUMMER","DRINK","SLEEP","DISPLAY"]
word=[]
words=random.choice(word_grp)

#fonts
LETTER_FONT=pygame.font.SysFont('comicsans', 30, bold=False, italic=False)
LETTER_FONT3=pygame.font.SysFont('comicsans', 20, bold=False, italic=False)
LETTER_FONT2=pygame.font.SysFont('comicsans', 80, bold=False, italic=False)
TITLE_FONT=pygame.font.SysFont('comicsans', 90, bold=False, italic=True)

#for alphabates
RADIUS=20
GAP=15
latters=[]
starty=430
A=65
start_point=round((WIDTH-(RADIUS*2*13+GAP*12))/2)
for i in range(26):
    x=start_point+((RADIUS*2+GAP)*(i%13))
    y=starty+((RADIUS*2+GAP)*(i//13))
    latters.append([x,y,chr(A+i),True])


# draw alphabates with circle
def draw():
    win.fill(WHITE)
    text=TITLE_FONT.render("HANGMAN GAME",1,(0,0,0))
    win.blit(text,(110,50))
    developed_credit=LETTER_FONT3.render("@developed by ARYA",1,(0,0,0))
    win.blit(developed_credit,(WIDTH-developed_credit.get_width()-5, HEIGHT-developed_credit.get_height()-5))
    disp_word=" "
    for w in words :
        if(w in word):
           disp_word+=w
            
        else:
            disp_word+="_ "
        text=LETTER_FONT2.render(disp_word,1,(0,0,0))
        win.blit(text,(320,200))
    for latter in latters:
        x,y,ltr,visible=latter
        if visible:
            pygame.draw.circle(win, (0,0,0), (x,y), RADIUS, 3)
            text=LETTER_FONT.render(ltr,1, (0,0,0))
            win.blit(text,(x-RADIUS/3,y-RADIUS/3))
        win.blit(images[hangman_stat],(115,150))
    pygame.display.update()



# massege for game win or lose
def makeWord(msg,time,fonttype):
    win.fill(WHITE)
    text=fonttype.render(msg,3,(0,0,0))
    win.blit(text,(WIDTH/2-text.get_width()/2,HEIGHT/2-text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(time)         

#load images use in game
images=[]
hangman_stat=0
for i in range(7):
    image=pygame.image.load("images/hangman"+str(i)+".png")
    images.append(image)





# main loop for play game
while run:
    clock.tick(FPS)
    draw()
   
    #get() is for ques message
    for event in pygame.event.get():
        #Quit for quit action by mouse
        if(event.type==pygame.QUIT):
             run=False
             break
        if(event.type==pygame.MOUSEBUTTONDOWN):
            x,y=pygame.mouse.get_pos()
            for latter in latters:
                xltr,yltr,ltr,visible=latter
                distance=math.sqrt((x-xltr)**2+(y-yltr)**2)
                if(distance<=RADIUS):
                    latter[3]=False
                    if(ltr in words):
                        word.append(ltr)
                    else:
                        hangman_stat+=1
    won=True
    for wo in words:
        if(wo not in word):
            won=False
            break
    if won:
        makeWord("you Won",3000,LETTER_FONT2)
        word=[]
        words=random.choice(word_grp)
        hangman_stat=0

        for latter in latters:
            latter[3]=True

        makeWord("Play Once More",1000,LETTER_FONT2)
    if(hangman_stat==6):
        makeWord("you Lost",3000,LETTER_FONT2)
        word=[]
        words=random.choice(word_grp)
        hangman_stat=0
        for latter in latters:
            latter[3]=True

        makeWord("Try Again",1000,LETTER_FONT2)




                
                   

       
	

pygame.quit()