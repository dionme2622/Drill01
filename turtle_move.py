import turtle as t

def move_left() :
    t.seth(0)
    t.forward(50)
    t.stamp()
def move_right() :
    t.seth(180)
    t.forward(50)
    t.stamp()
def move_up() :
    t.seth(90)
    t.forward(50)
    t.stamp()
def move_down() :
    t.seth(270)
    t.forward(50)
    t.stamp()
def reset() :
    t.reset()

    
t.shape("turtle")

t.onkey(move_left, 'd')
t.onkey(move_right, 'a')
t.onkey(move_up, 'w')
t.onkey(move_down, 's')
t.onkey(reset,'Escape')
t.listen()
