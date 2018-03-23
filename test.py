glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)


##################
    glColor3f(1,0,0)

    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,2.5*.5)
    glRotate(y,0,0,1)
    glutWireTorus(.12,.4,12,8)

    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,-2.5*.65)
    glRotate(y,0,0,1)

    glutWireTorus(.12,.4,12,8)

    glLoadIdentity()
    glTranslate(x-2.25,-2.5*.25,2.5*.5)
    glRotate(y,0,0,1)
    glutWireTorus(.12,.4,12,8)

    glLoadIdentity()
    glTranslate(x-2.25,-2.5*.25,-2.5*.55)
    glRotate(y,0,0,1)

    glutWireTorus(.12,.4,12,8)

#################

    glColor3f(0,color+.5,1)
    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,0.1)
    glutSolidSphere(.25,10,40)

    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,-1)
    glutSolidSphere(.25,10,40)


    if(x > 10 ):
        co = -co
    elif(x<-10):
        co = -co
    x-=.02*co
    y+= .1*co

    if(color >=.5 and color >0):
        color += .5*co
    else:
        color += .5*co

    glPopAttrib()
    glPopMatrix()