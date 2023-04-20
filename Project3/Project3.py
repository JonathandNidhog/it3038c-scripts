import pygame 
from time import sleep
from random import randrange
# Initialize Pygame
pygame.init()
pygame.mixer.init()
# Set screen width and height
map_w = 284  
map_h = 512  

# Set frame and FPS
frame = 0  # Current frame number
FPS = 60  # Frames per second

# Set pipes
pipes = [[180,4]]
# Set Bird position 
bird = [40,map_h//2-50]
# Set gravity
gravity = 0.2
# Set Velocity
velocity = 0

# Set Status
game_status = "not_started"

# Create game window and load background image
gameScreen = pygame.display.set_mode((map_w, map_h))  
clock = pygame.time.Clock() 
background = pygame.image.load("images/background.png")  
pipe_b = pygame.image.load("images/pipe_body.png")
pipe_e = pygame.image.load("images/pipe_end.png")
# Load bird asset
bird_up = bird_up_copy =  pygame.image.load("images/bird_wing_up.png") 
bird_down = bird_down_copy =  pygame.image.load("images/bird_wing_down.png") 

# Load Sound
score_sound = pygame.mixer.Sound('sound/score.mp3')
hit_sound = pygame.mixer.Sound('sound/hit.mp3')
fly_sound = pygame.mixer.Sound('sound/fly.mp3')
#Draw pipes
score = 0
scoreC = 0
def draw_pipes():
    global pipes, score
    for n in range(len(pipes)):
        for m in range(pipes[n][1]):
            gameScreen.blit(pipe_b,(pipes[n][0], m*32))
        for m in range (pipes[n][1]+6, 16):
            gameScreen.blit(pipe_b,(pipes[n][0], m*32))
        gameScreen.blit(pipe_e,(pipes[n][0],(pipes[n][1])*32))
        gameScreen.blit(pipe_e,(pipes[n][0],(pipes[n][1]+5)*32))
        pipes[n][0] -= 1
        #if pipes[n][0] == bird[0]:
            #score += 1
            #scoreC == score
            #print(score)
            
        
# Define the function to draw the bird
def draw_bird(x,y):
    global frame 
    if 0 <= frame<=30:
        gameScreen.blit(bird_up,(x,y))
        frame +=1
    elif 30<frame<=60:
        gameScreen.blit(bird_down,(x,y))
        frame +=1
        if frame == 60 : frame = 0    
# Define the function about did the bird touch the pipes
def safe():
    if bird[1]>map_h - 35:
        print("hit floor")
        return False
    if bird[1]<0:
        print("hit celling")
        return False
    if pipes[0][0]-30 < bird[0] < pipes[0][0] + 79:
        if bird[1]<(pipes[0][1]+1)*32 or bird[1]>(pipes[0][1]+4)*32:
            print("hit pipe")
            return False
    return True 
# Reset Game function 
def reset():
    global frame,map_h,map_w,FPS,pipes,bird,gravity,velocity
    frame = 0
    FPS = 60 
    map_w = 284  
    map_h = 512 
    pipes.clear()
    bird.clear()
    pipes = [[180,4]] 
    bird = [40,map_h//2-50]
    gravity = 0.2
    velocity = 0
def show_score_screen():
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(map_w//2, map_h//2))
    gameScreen.blit(text, text_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def show_start_screen():
    font = pygame.font.Font(None, 36)
    text = font.render("Press any key to start", True, (255, 255, 255))
    text_rect = text.get_rect(center=(map_w//2, map_h//2))
    gameScreen.blit(text, text_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                return
def show_end_screen(score):
    font = pygame.font.Font(None, 36)
    text = font.render("Game over! Score: {}".format(score), True, (255, 255, 255))
    text_rect = text.get_rect(center=(map_w//2, map_h//2))
    gameScreen.blit(text, text_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                return

# Define the main game loop
def gameLoop():
    global background, velocity, bird_up, bird_down, game_status,score,scoreC
    
    # Set font and font size
    font = pygame.font.SysFont(None, 30)

    # Start screen
    start_text = font.render("Press any key to start", True, (255, 255, 255))
    start_rect = start_text.get_rect(center=(map_w//2, map_h//2))
    
    # End screen
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    score_rect = score_text.get_rect(center=(map_w//2, map_h//2-40))
    scoreC_text = font.render(f"Score: {scoreC}", True, (255, 255, 255))
    scoreC_rect = score_text.get_rect(center=(map_w//2, map_h//2-200))                  
    gameover_text = font.render("Game Over", True, (255, 255, 255))
    gameover_rect = gameover_text.get_rect(center=(map_w//2, map_h//2+40))
    reset_text = font.render("Click to reset", True, (1, 1, 1))
    reset_rect = gameover_text.get_rect(center=(map_w//2, map_h//2+80))
    while True:
        if game_status == "not_started":
            # Display start screen
            gameScreen.blit(background, (0, 0))
            gameScreen.blit(start_text, start_rect)
            pygame.display.update()

            # Wait for player to press any key
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    game_status = "playing"
        
        elif game_status == "playing":
         
            # Add random pipes
            if len(pipes) < 4:
                x = pipes[-1][0] + 200
                open_pos = randrange(1, 9)
                pipes.append([x, open_pos])
            if pipes[0][0] < -100:
                pipes.pop(0)
                
            # Close the game when the Close button is clicked
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # Control bird
                    bird[1] -= 40
                    velocity = 0
                    fly_sound.play()
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            # Add gravity to bird
            velocity += gravity
            bird[1] += velocity

            # Turn Bird Head
            bird_down = pygame.transform.rotate(bird_down_copy, -90*(velocity/15))
            bird_up = pygame.transform.rotate(bird_up_copy, -90*(velocity/15))

            # Draw the background image onto the game screen
            gameScreen.blit(background, (0, 0))

            # Draw the bird
            draw_bird(bird[0], bird[1])

            # Draw pipes
            draw_pipes()
            gameScreen.blit(scoreC_text, scoreC_rect)  

            # Check if bird passed through a pipe
            for pipe in pipes:
                if pipe[0] == bird[0]:
                    score += 1
                    scoreC = score
                    score_sound.play()
                    print(score)
            scoreC_text = font.render(f"Score: {scoreC}", True, (255, 255, 255))
            scoreC_rect = score_text.get_rect(center=(map_w//2, map_h//2-200))                  
            gameScreen.blit(scoreC_text, scoreC_rect) 
            # Update the display
            pygame.display.update() 
            # Check player alive or not
            if not safe():
                hit_sound.play()
                sleep(1)
                reset()
                game_status = "game_over"

            # Set the game's FPS
            clock.tick(FPS)
            
        elif game_status == "game_over":
            # Display end screen
            gameScreen.blit(background, (0, 0))
            gameScreen.blit(gameover_text, gameover_rect)
            gameScreen.blit(scoreC_text, score_rect)
            gameScreen.blit(reset_text, reset_rect)
            pygame.display.update()

            # Wait for player to press any key
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    game_status = "playing"
# Call the main game loop function
gameLoop()
