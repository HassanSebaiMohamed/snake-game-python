#import modules 
#random places for food the snake eat it 
import random 
#the place the snake's shape appears 
import curses
#timer
import time
#score you achive it 
score = 0
#create our screen initilaize the curses 
screen=curses.initscr()

#hide mouse curses / set curses state 
curses.curs_set(0)
# get max of resolution( h , w) 
screen_height,screen_width=screen.getmaxyx()#getmax the Maximum height/width 
#create a new window # (0 to  x  all of the lenght of screen from  ,0 to y  all of the lenght from y   )
window=curses.newwin(screen_height,screen_width,0,0)
#allow window to recive input from the ketboard (← & → & ↑ & ↓ )
window.keypad(1)
#deremine the x,y coordinate of the initial postion of snake 
snak_x=screen_width//4 # integer division  500//4=125
snak_y=screen_height//2 # 500//2=250
#define the initial poisition of the snake body 
snake=[
  [snak_y,snak_x] ,# head
  [snak_y,snak_x-1]  ,#body
  [snak_y,snak_x-2] #tail
]

#create the food in the middle of the screen (window)
food=[
    screen_height//2,
    screen_width//2
    #food=[800//2,400//2]=[400,200]
]

#create the food DIMONDA (y,x,)
window.addch(food[0],food[1],curses.ACS_DIAMOND)
#set initial first dir to left
key=curses.KEY_RIGHT
# update screen speed (initial delay)
window.timeout(100)
#start time storage Current time
start_time = time.time()
#creat game loop until player loses or quits the game 
while True :
    #get the next key that will be pressed by user 
    next_key=window.getch()
    #if user does not input anything , key remains same . else key will be set to 
    #the new pressed key 
    if next_key ==-1 : 
        key = key
    else :
        key = next_key
# calculate elapsed time since game start
    elapsed_time = int(time.time() - start_time)
#check if snake collided with the walls of itself 
    if snake[0][0] in [0,screen_height] or snake[0][1] in [0,screen_width] or snake[0] in snake[1:] :
#if it collides close the window and exit the game / program
        curses.endwin()
        print("Game Over!")
        print(f"Final Score: {score}")
        print(f"You survived: {elapsed_time} seconds")
        quit()
#set the new poistion of the snake head based on the direction 
    new_head=[snake[0][0],snake[0][1]]
    if key == curses.KEY_DOWN:
      
      new_head[0] += 1
    elif key == curses.KEY_UP:
      
      new_head[0] -= 1
    elif key == curses.KEY_LEFT:
     
     new_head[1] -= 1
    elif key == curses.KEY_RIGHT:
     
     new_head[1] += 1

#insert the new head to the first poistion of snake list
    snake.insert(0,new_head)
#check if snake ate the food or not 
    if snake[0] == food:
        food = None #remove the food the snake at it 
        score += 1
#generate new food in a random place while food is remove 
        while food is None : 
            new_food=[
                random.randint(1,screen_height-1),#-1 cause the food not get on the either side of screen 
                random.randint(1,screen_width-1)
            ]
#the The probability of a random location coinciding with the snake's location
# #set new food not in snake bodt and it to screen 
# food=new_food if new_food not in snake else None
            if new_food not in snake :
                food = new_food
            else:
                food=None
        window.addch(food[0],food[1],curses.ACS_DIAMOND)
#romve the last place of snake body  
    else :
        tail=snake.pop()
        window.addch(tail[0],tail[1],' ')#(y,x,replace)
# update the position of the snake on the screen 
    window.addch(snake[0][0], snake[0][1],curses.ACS_CKBOARD)
    window.addstr(0, 2, f"Score: {score}")
    #caunt the time /Current time - start time = the time 
    window.addstr(0, 20, f"Time: {elapsed_time}s")
    #delay for updataing screen to take decision the snake top or bottom or right or left 
    window.timeout(max(50, 100 - score * 2))





          



        
        




   
    






    


