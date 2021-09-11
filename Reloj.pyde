y_position = 0
color_control = False

def setup():
    size(600,610)
    
def draw():
    global y_position 
    background(250)
    
    ellipse(width /1.15, y_position, 50, 50)
    if y_position > height:
       y_position = 0
    else:
       y_position = map(second(), 0, 59, 0, height)
    if color_control == True:
        fill(255)
    else:
        fill(0)
    ellipse(width / 5, y_position, 50, 50)
    if y_position > height:
       y_position = 0
    else:
       y_position = map(minute(), 0, 59, 0, height)
    if color_control  == True:
       fill(255)
    else:
       fill (0)
       
    ellipse(width / 1.85, y_position, 50, 50)
    if y_position > height:
       y_position = 0
    else:
       y_position = map(hour(), 0, 23, 0, height)
    if color_control == True:
       fill(255)
    else:
       fill(0)
       
    line(425, 0,425, 600)
    line(225,0,225,600)
    line(25,0,25,600)
    
    
def mousePressed(): 
    global color_control
    color_control = not color_control
