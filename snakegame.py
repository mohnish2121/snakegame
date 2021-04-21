import pygame
import random
import time
SIZE=36

class Apple:
    def __init__(self, parent_screen):
        self.apple=pygame.image.load('resources/apple.jpg')
        self.parent_screen=parent_screen
        self.x= SIZE*6
        self.y=SIZE*3
    def drawapple(self):
        
        self.parent_screen.blit(self.apple,(self.x, self.y))
        pygame.display.update()
    def move(self):
        self.x=random.randint(0,19)*SIZE
        self.y=random.randint(0,14)*SIZE
class Snake:
    def __init__(self, parent_screen, length):
        self.length=length
        self.parent_screen= parent_screen
        self.block=pygame.image.load('resources/download.jpeg')
        self.direction='right'
        self.x=[SIZE]*self.length
        self.y=[SIZE]*self.length

        
    def increaselength(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)

    
    def draw(self):
        for i in range (self.length):
            
            self.parent_screen.blit(self.block,(self.x[i],self.y[i]))
        pygame.display.update()

    def moveup(self):
        self.direction='up'

    def movedown(self):
        self.direction='down'

    def moveright(self):
        self.direction='right'

    def moveleft(self):
        self.direction='left'    

    def walk(self):
        for i in range (self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]
        
        if self.direction == 'up' :
            self.y[0]-=SIZE
            self.draw()
        if self.direction == 'down' :
            self.y[0]+=SIZE
            self.draw()
        if self.direction == 'right' :
            self.x[0]+=SIZE
            self.draw()
        if self.direction == 'left' :
            self.x[0]-=SIZE
            self.draw()

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Snake Game')
        
        self.background=pygame.display.set_mode((720, 540))
        self.bgimage()
        self.snake=Snake(self.background, 1)
        self.snake.draw()
        self.apple=Apple(self.background)
        self.apple.drawapple()
    
    def bgimage(self):
        self.bgimg=pygame.image.load("resources/bg.png")
        self.background.blit(self.bgimg, (0,0))
        
    def iscollision(self, x1, y1, x2, y2):
        if x1>=x2 and x1<x2+SIZE:
            if y1>=y2 and y1<y2+SIZE:
                return True
        
        else:
            return False
    
    def wallcollision(self):
        if self.snake.x[0] < 0 or self.snake.x[0] + SIZE > 720 or self.snake.y[0] < 0 or self.snake.y[0] + SIZE > 540:
            return True
        else :
            return False
    def play(self):
        self.bgimage()
        self.snake.walk()
        self.apple.drawapple()
        self.display_score()
        pygame.display.update()
        if self.iscollision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            
            self.apple.move()
            self.snake.increaselength()

        for i in range(3, self.snake.length):
            if self.iscollision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "game over"
   
        if self.wallcollision():
            raise "game over"

    def display_score(self):
        font=pygame.font.SysFont('arial',30)
        score=font.render(f"Score: {self.snake.length}",True,(255,255,255))
        self.background.blit(score, (600,10))
    
    def gameovermsg(self):
        self.bgimage()
        font=pygame.font.SysFont('arial',30)
        line1=font.render(f"Game is Over your Score: {self.snake.length}",True,(255,255,255))
        self.background.blit(line1,(100,270))
        line2=font.render(f"to play again press Enter, to exit press Escape",True , (255, 255, 255))
        self.background.blit(line2,(100,320))
        pygame.display.update()

    def reset(self):
        self.snake=Snake(self.background, 1)
        
        self.apple=Apple(self.background)

    def run(self):
        running=True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running=False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running=False

                    if event.key == pygame.K_RETURN:
                        pause=False


                    if pause == False :
                        if self.snake.direction != 'down':
                            if event.key == pygame.K_UP:
                                self.snake.moveup()
                        
                        if self.snake.direction != 'up':
                            if event.key == pygame.K_DOWN:
                                self.snake.movedown()

                        if self.snake.direction != 'left':
                            if event.key == pygame.K_RIGHT:
                                self.snake.moveright()
                        if self.snake.direction != 'right':
                            if event.key == pygame.K_LEFT:
                                self.snake.moveleft()
            try :
                if not pause:
                    self.play()
            except Exception as e:
                self.gameovermsg()
                pause=True
                self.reset()
            if self.snake.length <= 6:
                time.sleep(0.2)
            elif self.snake.length <=12 and self.snake.length >6:
                time.sleep(0.1)
            elif self.snake.length > 12 and self.snake.length <=20:
                time.sleep(0.075)
            elif self.snake.length > 20:
                time.sleep(0.05) 
if __name__ == "__main__":
    game=Game()
    game.run()



    
    
    
    
    
    
    

    

       
        
            


                

