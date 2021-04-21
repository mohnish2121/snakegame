import pygame
import time
LINECOLOR=(220, 245, 215)
WHITE= (255,255,255)
BLACK= (0,0,0)
class Player1:
    def __init__(self,surface):
        self.surface=surface
        self.crossimg=pygame.image.load("tic_resources/cross.jpg")

    def draw(self,x,y):
        self.surface.blit(self.crossimg,(x,y))
    def exactdraw(self, i, j):
        if i==0 and j==0:
            self.draw(10,10)
        if i==0 and j==1:
            self.draw(210,10)
        if i==0 and j==2:
            self.draw(410,10)
        if i==1 and j==0:
            self.draw(10,210)
        if i==1 and j==1:
            self.draw(210,210)
        if i==1 and j==2:
            self.draw(410,210)
        if i==2 and j==0:
            self.draw(10,410)
        if i==2 and j==1:
            self.draw(210,410)
        if i==2 and j==2:
            self.draw(410,410)
        
        
class Player2:
    def __init__(self, surface):
        self.surface= surface
        self.circleimg=pygame.image.load("tic_resources/circle.jpg")

    def draw(self,x,y):
        self.surface.blit(self.circleimg, (x,y))

    def exactdraw(self, i, j):
        if i==0 and j==0:
            self.draw(10,10)
        if i==0 and j==1:
            self.draw(210,10)
        if i==0 and j==2:
            self.draw(410,10)
        if i==1 and j==0:
            self.draw(10,210)
        if i==1 and j==1:
            self.draw(210,210)
        if i==1 and j==2:
            self.draw(410,210)
        if i==2 and j==0:
            self.draw(10,410)
        if i==2 and j==1:
            self.draw(210,410)
        if i==2 and j==2:
            self.draw(410,410)
        
class Yellow:
    def __init__(self, surface):
        self.surface = surface
        self.color = (242,227,58)

    def draw_box(self, x, y):
        pygame.draw.line(self.surface, self.color, (x, y), (x,y+180),10)
        pygame.draw.line(self.surface, self.color, (x,y+180), (x+180,y+180),10)
        pygame.draw.line(self.surface, self.color, (x+180,y+180), (x+180,y),10)
        pygame.draw.line(self.surface, self.color, (x+180,y), (x, y),10)


class Game:
    def __init__(self):
        pygame.init()
        self.surface= pygame.display.set_mode((600,600))
        pygame.display.set_caption('TIC TAC TOE')
        self.surface.fill(WHITE)
        pygame.draw.line(self.surface, LINECOLOR, (10,200),(590,200), 10)
        self.player1=Player1(self.surface)
        self.player2= Player2(self.surface)
        self.yellow= Yellow(self.surface)
        self.x=10
        self.q=0
        self.t=0
        self.pause= False
        self.y= 10
        self.a=[[0,0,0],[0,0,0],[0,0,0]]
        self.toss= True
        self.draw_screen()
        self.yellow.draw_box(self.x, self.y)
        
        pygame.display.update()
    def draw_screen(self):
        self.surface.fill(WHITE)
        pygame.draw.line(self.surface, LINECOLOR, (0,200),(600,200), 10)
        pygame.draw.line(self.surface, LINECOLOR, (0,400),(600,400), 10)
        pygame.draw.line(self.surface, LINECOLOR, (200,0),(200,600), 10)
        pygame.draw.line(self.surface, LINECOLOR, (400,0),(400,600), 10)

    
    def actual(self):
        b=1
        if self.toss:
            b=1
        else:
            b=2
       
        
        if self.x == 10 and self.y == 10:
            if self.a[0][0]==0:
                self.a[0][0]=b
            else:
                self.toss= not self.toss
        elif self.x == 210 and self.y == 10:
            if self.a[0][1]==0:
                self.a[0][1]=b
            else:
                self.toss= not self.toss
        elif self.x == 410 and self.y == 10:
            if self.a[0][2]==0:
                self.a[0][2]=b
            else:
                self.toss= not self.toss
        elif self.x == 10 and self.y == 210:
            if self.a[1][0]==0:
                self.a[1][0]=b
            else:
                self.toss= not self.toss
        elif self.x == 210 and self.y == 210:
            if self.a[1][1]==0:
                self.a[1][1]=b
            else:
                self.toss= not self.toss
        elif self.x == 410 and self.y == 210:
            if self.a[1][2]==0:
                self.a[1][2]=b
            else:
                self.toss= not self.toss
        elif self.x == 10 and self.y == 410:
            if self.a[2][0]==0:
                self.a[2][0]=b
            else:
                self.toss= not self.toss
        elif self.x == 210 and self.y == 410:
            if self.a[2][1]==0:
                self.a[2][1]=b
            else:
                self.toss= not self.toss
        elif self.x == 410 and self.y == 410:
            if self.a[2][2]==0:
                self.a[2][2]=b
            else:
                self.toss= not self.toss

    def printloop(self):
        for i in range(3):
            for j in range(3):
                if self.a[i][j]==1:
                    self.player1.exactdraw(i,j)
                    pygame.display.update()

                if self.a[i][j]==2:
                    self.player2.exactdraw(i,j)
                    pygame.display.update()

                if self.a[i][j]==0:
                    pygame.display.update()
    
    def blackline(self,x,y,x1,y1):
        pygame.draw.line(self.surface, BLACK, (x,y),(x1,y1),4)
    
    def lastline(self):
        if self.t == 1:
            self.blackline(100,100,500,100)
        if self.t == 2:
            self.blackline(100,300,500,300)
        if self.t == 3:
            self.blackline(100,500,500,500)
        if self.t == 4:
            self.blackline(100,100,100,500)
        if self.t == 5:
            self.blackline(300,100,300,500)
        if self.t == 6:
            self.blackline(500,100,500,500)
        if self.t == 7:
            self.blackline(100,100,500,500)
        if self.t == 8:
            self.blackline(500,100,100,500)
        
    def winning(self):
        if self.a[0][0] == self.a[0][1] == self.a[0][2] != 0:
            self.t=1
            self.q=self.a[0][0]
            raise "gameover"
        if self.a[1][0] == self.a[1][1] == self.a[1][2] != 0:
            self.t=2
            self.q=self.a[1][0]
            raise "gameover"
        if self.a[2][0] == self.a[2][1] == self.a[2][2] != 0:
            self.t=3
            self.q=self.a[2][0]
            raise "gameover"
        if self.a[0][0] == self.a[1][0] == self.a[2][0] != 0:
            self.t=4
            self.q=self.a[0][0]
            raise "gameover"
        if self.a[0][1] == self.a[1][1] == self.a[2][1] != 0:
            self.t=5
            self.q=self.a[0][1]
            raise "gameover"
        if self.a[0][2] == self.a[1][2] == self.a[2][2] != 0:
            self.t=6
            self.q=self.a[0][2]
            raise "gameover"
        if self.a[0][0] == self.a[1][1] == self.a[2][2] != 0:
            self.t=7
            self.q=self.a[0][0]
            raise "gameover"
        if self.a[0][2] == self.a[1][1] == self.a[2][0] != 0:
            self.t=8
            self.q=self.a[0][2]
            raise "gameover"
      
    def reset(self):
        self.draw_screen()
        self.x= 10
        self.y= 10
        self.yellow.draw_box(self.x, self.y)
        self.q=0
        self.t=0
        self.a=[[0,0,0],[0,0,0],[0,0,0]]
        self.toss= True
        pygame.display.update()

    def gameovermsg(self, w):
        self.draw_screen()
        
        font= pygame.font.SysFont("arial",30)
        if w ==1 :
            line1= font.render("GAME OVER PLAYER1 WINS", True, (0,0,0))
        elif w == 2:
            line1 = font.render("GAME OVER PLAYER2 WINS", True, (0,0,0))
        self.surface.blit(line1, (100,270))
        line2= font.render("SPACE TO PLAY , ESCAPE TO EXIT", True, (0,0,0))
        self.surface.blit(line2, (80, 320))
        pygame.display.update()
        

    def run(self):
        running=True
        while running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running= False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                    if event.key == pygame.K_RETURN:
                        self.actual()
                        self.toss = not self.toss
                        
                    if event.key == pygame.K_SPACE:
                        
                        self.reset()
                        self.pause= False    
                    if not self.pause:
                        if self.x< 410:
                            if event.key == pygame.K_RIGHT:
                                self.x+=200
                                self.draw_screen()
                                self.yellow.draw_box(self.x, self.y)
                                pygame.display.update()
                            
                        if self.x > 10:
                            if event.key ==pygame.K_LEFT:
                                self.x-=200
                                self.draw_screen()
                                self.yellow.draw_box(self.x, self.y)
                                pygame.display.update()

                        if self.y > 10:
                            if event.key == pygame.K_UP:
                                self.y-=200
                                self.draw_screen()
                                self.yellow.draw_box(self.x, self.y)
                                pygame.display.update()

                        if self.y < 410:
                            if event.key == pygame.K_DOWN:
                                self.y +=200
                                self.draw_screen()
                                self.yellow.draw_box(self.x, self.y)
                                pygame.display.update()

                    
            if not self.pause:
                try:
                    self.printloop()
                    self.winning()
                except Exception as e:
                    self.lastline()
                    pygame.display.update()
                    time.sleep(1)
                    self.pause=True
                    self.gameovermsg(self.q)
                    


if __name__ == "__main__":
    game=Game()
    game.run()
    