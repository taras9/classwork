# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PADDING = 15


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    horiz_vel = random.randrange(120, 240)/60
    vert_vel = random.randrange(60, 180)/60
    if direction:
        ball_vel = [horiz_vel, -vert_vel] 
    else:
        ball_vel = [-horiz_vel, -vert_vel]
 

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = [0, 0]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, 0]
    paddle2_vel = [0, 0]
    paddle1_vel = [0, 0]
    spawn_ball(LEFT)

def reset():
   new_game()


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    paddle1_pos[1] += paddle1_vel[1]   
    paddle2_pos[1] += paddle2_vel[1]
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] == BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] == (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]      
        
    
        
    elif ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if ball_pos[1] > paddle1_pos[1] + PAD_HEIGHT:
            score1 = score1 + 1
            spawn_ball(LEFT)
        elif ball_pos[1] < paddle1_pos[1]:
            score1 = score1 + 1
            spawn_ball(LEFT)
        else:
            ball_vel[0] = -ball_vel[0] * 1.1

    elif ball_pos[0] + BALL_RADIUS >= (600 - PAD_WIDTH):  
        if ball_pos[1] > paddle2_pos[1] + PAD_HEIGHT:
            score2 = score2 + 1
            spawn_ball(RIGHT)
        elif ball_pos[1] < paddle2_pos[1]:
            score2 = score2 + 1
            spawn_ball(RIGHT)
        else:
            ball_vel[0] = -ball_vel[0]# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PADDING = 15


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [300, 200]
    horiz_vel = random.randrange(120, 240)/60
    vert_vel = random.randrange(60, 180)/60
    if direction:
        ball_vel = [horiz_vel, -vert_vel] 
    else:
        ball_vel = [-horiz_vel, -vert_vel]
 

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    paddle1_pos = [0, 0]
    paddle2_pos = [WIDTH - HALF_PAD_WIDTH, 0]
    paddle2_vel = [0, 0]
    paddle1_vel = [0, 0]
    spawn_ball(LEFT)

def reset():
   new_game()


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    paddle1_pos[1] += paddle1_vel[1]   
    paddle2_pos[1] += paddle2_vel[1]
        
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[1] == BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] == (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]      
        
  
            
        
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

   
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[1] < 0:
        paddle1_pos[1] = 0
    if paddle1_pos[1] > HEIGHT - PAD_HEIGHT:
        paddle1_pos[1] = HEIGHT - PAD_HEIGHT       
        
    if paddle2_pos[1] < 0:
        paddle2_pos[1] = 0
    if paddle2_pos[1] > HEIGHT - PAD_HEIGHT:
        paddle2_pos[1] = HEIGHT - PAD_HEIGHT
    
    # draw paddles
    canvas.draw_line([paddle1_pos[0] + HALF_PAD_WIDTH , paddle1_pos[1]], [paddle1_pos[0] + HALF_PAD_WIDTH , paddle1_pos[1] + PAD_HEIGHT], 8, "Aqua")
    canvas.draw_line([paddle2_pos[0], paddle2_pos[1]], [paddle2_pos[0], paddle2_pos[1] + PAD_HEIGHT], 8, "Aqua")

    # determine whether paddle and ball collide   
    
    
    if ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if ball_pos[1] > paddle1_pos[1] + PAD_HEIGHT:
            score1 = score1 + 1
            spawn_ball(LEFT)
        elif ball_pos[1] < paddle1_pos[1]:
            score1 = score1 + 1
            spawn_ball(LEFT)
        else:
            ball_vel[0] = -ball_vel[0] * 1.1

    elif ball_pos[0] + BALL_RADIUS >= (600 - PAD_WIDTH):  
        if ball_pos[1] > paddle2_pos[1] + PAD_HEIGHT:
            score2 = score2 + 1
            spawn_ball(RIGHT)
        elif ball_pos[1] < paddle2_pos[1]:
            score2 = score2 + 1
            spawn_ball(RIGHT)
        else:
            ball_vel[0] = -ball_vel[0] * 1.1
    
    # draw scores
    
    canvas.draw_text(str(score1), [175, 30], 24, "Pink")
    canvas.draw_text(str(score2), [400, 30], 24, "Pink") 
    
        
def keydown(key):
    global paddle1_vel, paddle2_vel   

    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = -10
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 10      
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = -10
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 10

def keyup(key):
    global paddle1_vel, paddle2_vel

    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel[1] = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel[1] = 0      
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel[1] = 0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel[1] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Reset", reset, 100)


# start frame
new_game()
frame.start()

