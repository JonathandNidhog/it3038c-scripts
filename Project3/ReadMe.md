# project3

This is my project3, he is a flappy bird game made using python language. 
Befor run this program user need install the pygame. Here is the method about install the pygame https://www.pygame.org/wiki/GettingStarted
The operation of the game is very simple, at the beginning of the game the player presses any key to start the game,
during the game the player can press any key to play, after the player dies by mouse to restart the game. 
In this project there are sound effects, score display, game start and end, and player score summary.<br>
-------------------------------------------------------------------------------------------------------------------------<br>
The difference between the first two projects is that I have used UE4 and Unity to make flappy bird, 
so I am familiar with the features needed to make the project. However, even though I was familiar with 
the content of the project, I still had a lot of problems when using different programming languages to 
create the project.<br>
One example of this is that when creating a score screen that displays in real time, the
scores have not been able to be refreshed in real time.<br>
Initially I put the code to get the score in the pipeline generation function<br>
```python
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
        if pipes[n][0] == bird[0]:
            score += 1
            scoreC == score
            print(score)
   ```
However, since the score display function is in
 ```python
   def gameLoop():
 ```
 This results in the score not being transferred to the gameLoop() function when the score is refreshed, 
 so my score is always 0<br>
So I moved the fraction function to gameloop to determine if the pipe coordinates overlap with the bird coordinates, and if they do, then the fraction is added by one
 ```python
             # Check if bird passed through a pipe
            for pipe in pipes:
                if pipe[0] == bird[0]:
                    score += 1
                    scoreC = score
                    score_sound.play()
                    print(score)
```
However, the score refresh was still problematic, and that's when I discovered that the score display section needed to be re-rendered after the score refresh before the score could be updated to the screen, so I added：
 ```python
            scoreC_text = font.render(f"Score: {scoreC}", True, (255, 255, 255))
            scoreC_rect = score_text.get_rect(center=(map_w//2, map_h//2-200))                  
            gameScreen.blit(scoreC_text, scoreC_rect) 
```
After reloading the score screen the scores were finally able to be updated in real time.<br>
Also found some interesting things in the production of this project, for example, in python, the interface hierarchy is based on the loading of the interface by seeking, if I generate the code of the game interface is
 ```python
             draw_bird(bird[0], bird[1])
             draw_pipes()
             gameScreen.blit(background, (0, 0))
 ```
Then in my game interface, I can only see the background image, because the background image is the last to be loaded, so the pipe and bird images will cover the background, which I did not expect.<br>
It seems that in Pygame there is only xy-axis but not Z-axis, so it is impossible to set the image coordinates of Z-axis only according to the loading order of the image to place the image hierarchy.<br>
Finally, by using a different way (programming language or engine) to make flappy bird helped me to get better acquainted with the new language by using the one I already knew. For me, using a new language to make Flappy bird is a good way to verify my proficiency in a language.
