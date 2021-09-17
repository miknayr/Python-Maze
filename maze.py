#tutorial followed from @tokyoedtech

import turtle

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("A Maze Game")
wn. setup(700,700)

#create Pen
class Pen(turtle.Turtle):
    def __init__(self):
      turtle.Turtle.__init__(self)
      self.shape("square")
      self.color("white")
      self.penup()
      self.speed(0)

class Player(turtle.Turtle):
  def __init__(self):
      turtle.Turtle.__init__(self)
      self.shape("square")
      self.color("blue")
      self.penup()
      self.speed(0)

  def go_up(self):
    #calculate the spot to move to
    move_to_x = player.xcor()
    move_to_y = player.ycor() + 24
    
    #check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)
  def go_down(self):
    move_to_x = player.xcor()
    move_to_y = player.ycor() - 24
    
    #check if the space has a wall
    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)

  def go_left(self):
    move_to_x = player.xcor() - 24
    move_to_y = player.ycor()

    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)
    
  def go_right(self):
    move_to_x = player.xcor() + 24
    move_to_y = player.ycor()

    if (move_to_x, move_to_y) not in walls:
      self.goto(move_to_x, move_to_y)


#create levels list
levels = [""]


#define first level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XP XXXXXXX          XXXXX",
"X  XXXXXXX  XXXXXX  XXXXX",
"X       XX  XXXXXX  XXXXX",
"X       XX  XXX        XX",
"XXXXXX  XX  XXX        XX", 
"XXXXXX  XX  XXXXXX  XXXXX",
"XXXXXX  XX    XXXX  XXXXX",
"X  XXX        XXXX  XXXXX",     
"X  XXX  XXXXXXXXXXXXXXXXX",
"X         XXXXXXXXXXXXXXX",
"X                XXXXXXXX",
"XXXXXXXXXXXX     XXXXX  X",
"XXXXXXXXXXXXXXX  XXXXX  X",
"XXX  XXXXXXXXXX         X",
"XXX                     X",
"XXX         XXXXXXXXXXXXX",
"XXXXXXXXXX  XXXXXXXXXXXXX",
"XXXXXXXXXX              X",
"XX   XXXXX              X",
"XX   XXXXXXXXXXXXX  XXXXX",
"XX    XXXXXXXXXXXX  XXXXX",
"XX          XXXX        X",
"XXXX                    X",
"XXXXXXXXXXXXXXXXXXXXXXXXX"
]

#ADD maze to mazes list
levels.append(level_1)



# create level setup function
def setup_maze(level):
  for y in range(len(level)):
    for x in range(len(level[y])):
      #get the character at each x,y coordinate
      #note the order of y and x in the next line
      character = level[y][x]
      #claculate the screen x,y coordinates
      screen_x = -288 + (x * 24)
      screen_y = 288 - (y * 24)
      #check if it is an x (representing a wall)
      if character == "X":
        pen.goto(screen_x, screen_y)
        pen.stamp()
        walls.append((screen_x, screen_y))
      if character == "P":
        player.goto(screen_x,screen_y)


#Create class instances
pen = Pen()
player = Player()

#create wall coordinate list
walls = []

#set up maze
setup_maze(levels[1])


#keyboard binding
turtle.listen()
turtle.onkey(player.go_left,"Left")
turtle.onkey(player.go_right,"Right")
turtle.onkey(player.go_up,"Up")
turtle.onkey(player.go_down,"Down")

# Main Game Loop
while True:
  wn.update()
