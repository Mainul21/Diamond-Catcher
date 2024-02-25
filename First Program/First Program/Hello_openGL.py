from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


catcherX = 250
catcherY = 30
diamondX = random.randint(50,350)
diamondY = 500
fallingSpeed = 1
stop = False
score = 0



def draw_points(x, y):
    glPointSize(1) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
    glEnd()

def midpoint_Line_Drawing(zone,x1,y1,x2,y2):
    dx = x2-x1
    dy = y2-y1
    d = 2*dy-dx
    d_diff = 2*(dy-dx)

    x = x1
    y= y1

    while x<=x2:
        a,b = orginalZone(zone,x,y)
        draw_points(a,b)
        
        if d <= 0:
            d+= d+2*dy
            x+=1
        else:
            x+=1
            y+=1
            d = d+ d_diff

def findZone(x1,y1,x2,y2):
    dx= x2-x1
    dy= y2-y1

    if abs(dx) > abs(dy):
        if dx>0 and dy>0:
            return 0
        elif dx<0 and dy>0:
            return 3
        elif dx<0 and dy<0:
            return 4
        else:
            return 7
        
    else:
        if dx>0 and dy>0:
            return 1
        elif dx<0 and dy > 0:
            return 2
        elif dx<0 and dy<0:
            return 5
        else:
            return 6
        
def zeroZone(zone,x,y):
    if zone == 0:
        return x,y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y,x
    elif zone == 3:
        return -x,y
    elif zone == 4:
        return -x,-y
    elif zone == 5:
        return -y,-x
    elif zone == 6:
        return -y,x
    elif zone == 7:
        return x,-y
    
def orginalZone(zone,x,y):
    if zone == 0:
        return x,y
    elif zone == 1:
        return y, x
    elif zone == 2:
        return -y,-x
    elif zone == 3:
        return -x,y
    elif zone == 4:
        return -x,-y
    elif zone == 5:
        return -y,-x
    elif zone == 6:
        return y,-x
    elif zone == 7:
        return x,-y
    
def drawline(x1,y1,x2,y2):
    zone = findZone(x1,y1,x2,y2)
    x1, y1 = zeroZone(zone,x1,y1)
    x2,y2 = zeroZone(zone,x2,y2)
    midpoint_Line_Drawing(zone,x1,y1,x2,y2)

        
def draw_catcher():
    global catcherX, catcherY

    drawline(catcherX-40,catcherY,catcherX+40,catcherY)
    drawline(catcherX-40,catcherY,catcherX-30,catcherY-20)
    drawline(catcherX+40,catcherY,catcherX+30,catcherY-20)
    drawline(catcherX-30,catcherY-20,catcherX+30,catcherY-20)

def draw_diamond():
    global diamondX, diamondY,fallingSpeed,stop,score

    drawline(diamondX,diamondY,diamondX+5,diamondY-10)
    drawline(diamondX,diamondY,diamondX-5,diamondY-10)
    drawline(diamondX-5,diamondY-10,diamondX,diamondY-20)
    drawline(diamondX,diamondY-20,diamondX+5,diamondY-10)

    diamondY-=fallingSpeed

    if diamondY-20<catcherY  and catcherX-50<= diamondX<=catcherX+50:
        diamondX = random.randint(100,350)
        diamondY = 500
        score+=1
        fallingSpeed+=0.3
        print(score)

    elif diamondY-20 <0:
        fallingSpeed = 0
        diamondY = 20
        totalscore = score
        score = 0
        stop = True
        print('GAME OVER')
        print(totalscore)
        glutLeaveMainLoop()
def draw_cross():
    drawline(390,580,370,560)
    drawline(370,580,390,560)

def mouseListener(key, state,x,y):
    if key == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        if 370<=x<=390 and 560<= y<= 580:
            glutLeaveMainLoop()


def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)
    glutPostRedisplay()
    
def specialKeyboardListener(key,x,y):
    global catcherX
    if key == GLUT_KEY_LEFT:
        catcherX-=20
    elif key == GLUT_KEY_RIGHT:
        catcherX+=20
    catcherX = max(45, min(360,catcherX))



def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
     #konokichur color set (RGB)
    #call the draw methods here
    
    if stop:
        draw_cross()
        glColor3f(1.0,0.0,1.0)
        draw_diamond()
        glColor3f(1.0,0.0,1.0)
        draw_catcher()
    else:
        draw_cross()
        glColor3f(1.0,0.0,1.0)
        draw_catcher()
        glColor3f(random.uniform(0,1), random.uniform(0,1), random.uniform(0,1))
        draw_diamond()
    
    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutTimerFunc(0,timer,0)
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyboardListener)
glutMainLoop()