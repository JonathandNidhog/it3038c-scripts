# project1

This project is for project 1
it is an snake program, befor run this program user need install the pygame. Here is the method about install the pygame https://www.pygame.org/wiki/GettingStarted
follow the website install the game then run project1Snake to play the game.
Game can be controlled by derection button or W A S D change the direction of snake move.
Just like the usual snake game, when snake touch him self or touch the screen edge will lose the game.
For this projcet I only have basic sanke game which can show the score, start game finished the game.
For feature version I want to update more stuff like add voic in game.<br>

-------------------------------------------------------------------------------------------------------------------------<br>

# PROJECT2
For project 2, I add some voice in my game<br>
According to 
```python
pygame.mixer.Sound('the sound file name')
```
I played this sound when snake get a point, it sonds like 'Ding'<br>
This code enables different sounds to be made when the fraction is a multiple of ten：
```python
if score%10 == 0 :
                EndSound.play()
            else:
                collisionsound.play()
```
Also I changed the backgound of the game, it from pure color to an picture, when the game fninished it will turn to another picture<br>
Score system also appear in this version. The player's score will be displayed on the screen in real time, in the past version only the player can see his score when he dies.<br>
At same time, the ball color also be changed from red to green. I was try when the game end change the snake colore but failed.