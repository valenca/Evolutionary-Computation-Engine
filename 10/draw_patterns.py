import turtle

def color_quad(pos_x, pos_y, side, cor):
    turtle.pu()
    turtle.goto(pos_x, pos_y)
    turtle.pd()
    turtle.fillcolor(cor)
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(side)
        turtle.rt(90) 
    turtle.end_fill()
    turtle.ht()    


def white_quad(pos_x, pos_y, side):
    turtle.pu()
    turtle.goto(pos_x, pos_y)
    turtle.pd()
    for i in range(4):
        turtle.fd(side)
        turtle.rt(90)
    turtle.ht()
             
def black_quad(pos_x, pos_y, side):
    turtle.pu()
    turtle.goto(pos_x, pos_y)
    turtle.pd()
    turtle.fillcolor('black')
    turtle.begin_fill()
    for i in range(4):
        turtle.fd(side)
        turtle.rt(90) 
    turtle.end_fill()
    turtle.ht()
    
def draw_pattern(pattern):
    turtle.speed(0)
    side = 10
    size_x = len(pattern[0])
    size_y = len(pattern)
    pos_y = 0
    for i in range(size_y):
        pos_x = 0
        for j in range(size_x):
            if pattern[i][j] == 1:
                black_quad(pos_x, pos_y,side)
            else:
                white_quad(pos_x, pos_y,side)
            pos_x += side
        pos_y -= side
        
   
def draw_binary_pattern(pattern, color_1, color_2):
    turtle.speed(0)
    side = 10
    size_x = len(pattern[0])
    size_y = len(pattern)
    pos_y = 0
    for i in range(size_y):
        pos_x = 0
        for j in range(size_x):
            if pattern[i][j] == 1:
                color_quad(pos_x, pos_y,side, color_1)
            else:
                color_quad(pos_x, pos_y,side,color_2)
            pos_x += side
        pos_y -= side 
        
        



def draw_color_pattern(pattern, colors):
    """ colors is a dictionary with key = number, value = color."""
    turtle.speed(0)
    side = 10
    size_x = len(pattern[0])
    size_y = len(pattern)
    pos_y = 0
    for i in range(size_y):
        pos_x = 0
        for j in range(size_x):
            color_key = pattern[i][j]
            color_quad(pos_x,pos_y, side, colors[color_key])
            pos_x += side
        pos_y -= side
        
        
        
if __name__ == '__main__':
    """
    zero = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    
    one = [[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,1,1,1,1,0,0,0]]
    
    square = [[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[0,0,0,0,0,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1]]
    
    three = [[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,1,0,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,1,1,1,1,0,0],[0,0,0,0,1,1,1,1,0,0],[0,0,0,0,0,0,0,1,1,0],[0,0,0,0,0,0,0,1,1,0], [0,0,0,0,0,0,0,1,1,0],[0,0,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,1,0,0]] 
    """
    
    one = [[0,0,1,0],[0,1,1,0,],[0,0,1,0],[0,0,1,0],[0,0,1,0]]
    two = [[0,1,1,1],[0,0,0,1],[0,0,1,0],[0,1,0,0],[0,1,1,1]]
    three = [[0,1,1,1],[0,0,0,1],[0,0,1,1],[0,0,0,1],[0,1,1,1]]
    four = [[1,0,0,0],[1,0,0,0],[1,0,1,0],[1,1,1,1],[0,0,1,0]]
    five = [[1,1,1,0],[1,0,0,0],[0,1,1,0],[0,0,1,0],[1,1,1,0]]
    six = [[0,1,1,0],[1,0,0,0],[1,1,1,0],[1,0,0,1],[0,1,1,1]]
    seven = [[0,1,1,1],[0,0,0,1],[0,0,1,0],[0,0,1,0],[0,0,1,0]]
    eight = [[0,1,1,0],[1,0,0,1],[0,1,1,0],[1,0,0,1],[0,1,1,0]]    
    
    colors = {0:'red',1:'green',3:'blue'}
    #print(colors[1])
    color_zero = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,1,0,0],[0,1,1,1,1,1,1,1,1,0],[0,1,1,3,3,3,3,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,0,0,0,0,1,1,0],[0,1,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,1,0,0],[0,0,0,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    #white_quad(0,0,50)
    #black_quad(100,100,50)
    draw_pattern(eight)
    #draw_binary_pattern(zero,'red','yellow')
    #draw_color_pattern(color_zero, colors)
    
    turtle.exitonclick()