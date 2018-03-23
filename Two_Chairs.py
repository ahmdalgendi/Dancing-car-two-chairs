from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *

def Init():
    #glOrtho(-10,10,-10,10,-10,10)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60,1,1.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
    glClearColor(1,1,1,1)

def chair():
    x=0

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    ############
    glColor(0, 0, 1)
    glTranslate(x,0,0)
    glScale(1, .2, 1)
    glutWireCube(4)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glColor(0, 0, 1)
    glScale(1, 1, .2)
    glTranslate(0+x, 2, -8)
    glutWireCube(4)

    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    #leg(-2+x,-4, 2)

    glScale(.2, 1, .2)
    glTranslate(-2+x, -4, 2)
    glColor(0,0,1)
    glutWireCube(4)

    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    #leg(-20+x,-4, 2)
    glScale(.2, 1, .2)
    glTranslate(-20+x , -4, 2)
    glColor(0, 0, 1)
    glutWireCube(4)

    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    #leg(-2+x,-4 -20 )
    glColor(0, 0, 1)
    glScale(.2, 1, .2)
    glTranslate(-2 + x, -4, -20)
    glutWireCube(4)

    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    #leg(-20+x,-4, -20)
    glScale(.2, 1, .2)
    glColor(0, 0, 1)
    glTranslate(-20 + x, -4, -20)
    glutWireCube(4)

    glPopAttrib()
    glPopMatrix()

    glPopAttrib()
    glPopMatrix()


def Anime():
    global x,y,co,color
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glTranslate(-5,0,0)
    chair()
    glLoadIdentity()
    glTranslate(5,0,0)
    chair()


    glFlush()








glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,600)
glutCreateWindow(b"hey")
Init()
glutDisplayFunc(Anime)
#glutIdleFunc(Anime)
glutMainLoop()