from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# globals for animation, ball position
# and direction of motion
global anim, x, y, h_velocity, v_velocity, radius , up  , left
up =0
left = 0

# initial position of the center of the ball
x = -0.67
y = 0.34
z = -1
dtime = 0.005  # delta_time (try 0.005 and 0.00005)
radius = 0.1  # Ball's Raduis
h_velocity = 0.75  # try 3.0 and 0.25 # Horizontal Velocity of the ball
v_velocity = 3.0  # Vertical Velocity of the ball

# Window dimensions
width = height = 600
axrng = 1.0

# No animation to start
anim = 0


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    # Make axrng larger and see what happens!
    glOrtho(-axrng, axrng, -axrng, axrng, -2, 2)

    glMatrixMode(GL_MODELVIEW)


def bounce():
    global x, y, h_velocity, v_velocity, anim,z

    glColor(0, 1, 0)
    glClear(GL_COLOR_BUFFER_BIT)

    if anim == 1:
        # changes x and y
        x = x + h_velocity * dtime
        z= z+ h_velocity *dtime
        # earth's gravity -9.8 meters per second*second
        v_velocity = v_velocity - 9.8 * dtime
        y = y + v_velocity * dtime

        # This if statement keeps the ball from falling below the window!
        if y < -axrng + radius:
            v_velocity  = - v_velocity


        if x > axrng - radius or x <= -axrng + radius:
            h_velocity = -h_velocity
        # Collision detection!
        # What happens here and why does this work?
        # Collision response can be even more complicated if we want the physics to be accurate!



            # Keep the motion mathematics
    # Move the ball location based on x and y
    glLoadIdentity()
    glTranslate(x, y, z)
    glutWireTorus(radius, 10, 30 , 30)
    glutSolidSphere(radius, 50, 50)

    glutSwapBuffers()


def keyboard(key, xx, yy):
    # Allows us to quit by pressing 'q'
    # We can animate by "a" and stop by "s"
    global anim

    if key == b"a":
        # Notice we are making anim = 1
        # What does this mean? Look at the idle function
        anim = 1
    if key == b"s":
        # STOP the ball!
        anim = 0

    if key == b"q":
        sys.exit()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"PyBounce0")
    glutDisplayFunc(bounce)
    glutKeyboardFunc(keyboard)
    glutIdleFunc(bounce)
    init()
    glutMainLoop()


main()