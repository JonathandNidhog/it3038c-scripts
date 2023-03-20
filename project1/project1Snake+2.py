import pygame,sys,time,random
from pygame.locals import *

# define color
ballColour = pygame.Color(255,0,0)
bgColour = pygame.Color(0,0,0)
snakeColour = pygame.Color(255,255,255)
wordColour = pygame.Color(111,111,111)

#gameover screen
def gameOver(playSurface,score):
    #the font and size of game over text
    gameOverFont = pygame.font.SysFont('Times New Roman .fon',120) 
    #game over
    gameOverSurf = gameOverFont.render('Game Over!', True, wordColour) 
    gameOverRect = gameOverSurf.get_rect()
    # position
    gameOverRect.midtop = (500, 10) 
    playSurface.blit(gameOverSurf, gameOverRect)
    #show score
    scoreFont = pygame.font.SysFont('Times New Roman .fon',60) 
    scoreSurf = scoreFont.render('Score:'+str(score), True, wordColour)
    scoreRect = scoreSurf.get_rect()
    scoreRect.midtop = (500, 100)
    playSurface.blit(scoreSurf, scoreRect)
    
    #reflesh
    pygame.display.flip() 
    #wait 5 second then exit
    time.sleep(5) 
    pygame.quit()
    sys.exit()

# difine main fanction
def main():

    pygame.init()
    pygame.mixer.init()#add mixer in game
    collisionsound = pygame.mixer.Sound('Ding.wav')
    fpsClock = pygame.time.Clock()
    # create pygame layer
    playSurface = pygame.display.set_mode((1000,800))
    pygame.display.set_caption('Project1SnakeGame')
    # Initialize variable
    snakePosition = [100,100]
    snakeSegments = [[100,100],[80,100],[60,100]]
    ballPosition = [300,300] #init ball position
    ballSpawned = 1 #number
    direction = 'right' #init derection
    changeDirection = direction
    score = 0 #init score

    while True:
        # check pygame status
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # player controller
                if event.key == K_RIGHT or event.key == ord('d'):
                    changeDirection = 'right'
                if event.key == K_LEFT or event.key == ord('a'):
                    changeDirection = 'left'
                if event.key == K_UP or event.key == ord('w'):
                    changeDirection = 'up'
                if event.key == K_DOWN or event.key == ord('s'):
                    changeDirection = 'down'
                if event.key == K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT))
        # avoid derection bug
        if changeDirection == 'right' and not direction == 'left':
            direction = changeDirection
        if changeDirection == 'left' and not direction == 'right':
            direction = changeDirection
        if changeDirection == 'up' and not direction == 'down':
            direction = changeDirection
        if changeDirection == 'down' and not direction == 'up':
            direction = changeDirection
        # change derection
        if direction == 'right':
            snakePosition[0] += 20
        if direction == 'left':
            snakePosition[0] -= 20
        if direction == 'up':
            snakePosition[1] -= 20
        if direction == 'down':
            snakePosition[1] += 20
        # when snake get point
        snakeSegments.insert(0,list(snakePosition))
        if snakePosition[0] == ballPosition[0] and snakePosition[1] == ballPosition[1]:
            collisionsound.play()
            ballSpawned = 0
            score +=1
        else:
            snakeSegments.pop()
        # spawn new balls
        if ballSpawned == 0:
            x = random.randrange(1,30)
            y = random.randrange(1,23)
            ballPosition = [int(x*20),int(y*20)]
            ballSpawned = 1
            
        # creat game screen
        playSurface.fill(bgColour)
        for position in snakeSegments:
            pygame.draw.rect(playSurface,snakeColour,Rect(position[0],position[1],20,20))
            pygame.draw.rect(playSurface,ballColour,Rect(ballPosition[0], ballPosition[1],20,20))

        scoreFont = pygame.font.SysFont('Times New Roman .fon',60) 
        scoreSurf = scoreFont.render('Score:'+str(score), True, wordColour)
        scoreRect = scoreSurf.get_rect()
        scoreRect.midtop = (500, 100)
        playSurface.blit(scoreSurf, scoreRect)

        # reflesh game screen
        pygame.display.flip()

        # dead
        if snakePosition[0] > 1000 or snakePosition[0] < 0:
            gameOver(playSurface,score)
        if snakePosition[1] > 800 or snakePosition[1] < 0:
            gameOver(playSurface,score)
        #if snake touch itself
        for snakeBody in snakeSegments[1:]:
            if snakePosition[0] == snakeBody[0] and snakePosition[1] == snakeBody[1]:
                gameOver(playSurface,score)
        # Game speed
        fpsClock.tick(5)

if __name__ == "__main__":
    main()