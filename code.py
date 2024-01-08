import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# Global variables for car position and wheel rotation
car_pos_x = 0.0
car_pos_z = 1.0
wheel_rotation = 0.0

angle = 30.0  # Modified angle for light rotation

def init_light():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

def update_light_position():
    global angle
    radius = 5.0  # Radius of the circular path 
    x = radius * math.cos(math.radians(angle))
    z = radius * math.sin(math.radians(angle))
    light_position = (x, 5, z, 1)

    angle += 0.05  # Adjust the speed of rotation

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)

def draw_house():
    # Set the house color to yellow
    glColor3f(1.0, 1.0, 0.0)  # RGB values for yellow

    # Cube (house body)
    cube_size = 2.0
    glutSolidCube(cube_size)

    # Cone (roof)
    cone_diameter = 3.2
    cone_height = 1.0
    glColor3f(1.0, 0.75, 0.8)  # RGB values for pink
    glPushMatrix()
    glTranslatef(0, cube_size / 2 + cone_height / 2, 0)
    glRotatef(-90, 1, 0, 0)
    glutSolidCone(cone_diameter / 2, cone_height, 20, 20)
    glPopMatrix()

    # Chimney
    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)  # Set chimney color to yellow
    glTranslatef(0.7, cube_size / 2 + 1.0, 0)
    glScalef(0.2, 1.5, 0.2)
    glutSolidCube(1.0)
    glPopMatrix()

    # Brown door
    glColor3f(0.6, 0.4, 0.2)  # RGB values for brown
    glPushMatrix()
    glTranslatef(0, -cube_size / 2 + 0.2, cube_size / 2 + 0.01)  # Closer to the cube
    glScalef(0.6, 1.2, 0.01)  # Bigger door dimensions
    glutSolidCube(1.0)
    glPopMatrix()

    # Blue window (on the right side)
    glColor3f(0.0, 0.0, 1.0)  # RGB values for blue
    glPushMatrix()
    glTranslatef(cube_size / 2 + 0.01, 0, 0)  # To the right of the house
    glScalef(0.01, 0.6, 0.6)  # Window dimensions
    glutSolidCube(1.0)
    glPopMatrix()

    # Reset the colors
    glColor3f(1, 1, 1)

def draw_tree():
    trunk_height = 1.0
    foliage_height = 1.0
    foliage_radius = 0.5

    # Tree Trunk (brown cylinder)
    glColor3f(0.55, 0.27, 0.07)  # Brown color for the trunk
    glPushMatrix()
    glRotatef(-90, 1, 0, 0)  # Rotate to make the cylinder stand vertically
    glutSolidCylinder(0.1, trunk_height, 10, 10)  # Trunk dimensions
    glPopMatrix()

    # Tree Foliage (green cone)
    glColor3f(0.0, 0.5, 0.0)  # Dark green color for the foliage
    glPushMatrix()
    glTranslatef(0, trunk_height, 0)  # Move up by the trunk's height
    glRotatef(-90, 1, 0, 0)  # Rotate to make the cone point upwards
    glutSolidCone(foliage_radius, foliage_height, 10, 10)  # Foliage dimensions
    glPopMatrix()

    # Reset the color
    glColor3f(1, 1, 1)

def draw_car():
    global wheel_rotation

    # Set the car body color to red
    glColor3f(1.0, 0.0, 0.0)  # RGB values for red

    # Car body (horizontal rectangle)
    glPushMatrix()
    glTranslatef(car_pos_x, -0.5, car_pos_z)  # Use car_pos_x and car_pos_z for position
    glScalef(1.5, 0.5, 0.7)
    glutSolidCube(1.0)
    glPopMatrix()

    # Wheels (using darker gray)
    glColor3f(0.2, 0.2, 0.2)  # RGB values for dark gray

    cylinder_height = 0.2

    # Front left wheel
    glPushMatrix()
    glTranslatef(car_pos_x - 0.75 + 0.35, -0.75, car_pos_z - 0.35)
    glRotatef(wheel_rotation, 0, 0, 1)  # Rotate the wheel
    glutSolidCylinder(0.25, cylinder_height, 20, 20)
    glPopMatrix()

    # Front right wheel
    glPushMatrix()
    glTranslatef(car_pos_x + 0.75 - 0.35, -0.75, car_pos_z - 0.35)
    glRotatef(wheel_rotation, 0, 0, 1)  # Rotate the wheel
    glutSolidCylinder(0.25, cylinder_height, 20, 20)
    glPopMatrix()

    # Rear left wheel
    glPushMatrix()
    glTranslatef(car_pos_x - 0.75 + 0.35, -0.75, car_pos_z + 0.35)
    glRotatef(wheel_rotation, 0, 0, 1)  # Rotate the wheel
    glutSolidCylinder(0.25, cylinder_height, 20, 20)
    glPopMatrix()

    # Rear right wheel
    glPushMatrix()
    glTranslatef(car_pos_x + 0.75 - 0.35, -0.75, car_pos_z + 0.35)
    glRotatef(wheel_rotation, 0, 0, 1)  # Rotate the wheel
    glutSolidCylinder(0.25, cylinder_height, 20, 20)
    glPopMatrix()

    # Reset the color
    glColor3f(1, 1, 1)

def draw_ground():
    # Set the ground color to green
    glColor3f(0.0, 1.0, 0.0)  # RGB values for green
    glBegin(GL_QUADS)
    glVertex3f(-10, -10, -10)
    glVertex3f(10, -10, -10)
    glVertex3f(10, -10, 10)
    glVertex3f(-10, -10, 10)
    glEnd()

def draw_scene():
    # Your existing drawing code for the house, car, sky, and ground
    draw_ground()
    draw_house()
    glTranslatef(3, 0, 0)
    draw_car()
    draw_tree()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0.53, 0.81, 0.98, 1.0)  # Set the clear color to sky blue
    glLoadIdentity()
    gluPerspective(45, (1600 / 900), 0.1, 50.0)
    gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0)

    glEnable(GL_DEPTH_TEST)
    init_light()

    update_light_position()

    draw_scene()

    glfw.swap_buffers(window)

def key_callback(window, key, scancode, action, mods):
    global car_pos_x, car_pos_z, wheel_rotation
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_UP:
            car_pos_z -= 0.1  # Move forward
            wheel_rotation -= 10.0  # Rotate wheels
        elif key == glfw.KEY_DOWN:
            car_pos_z += 0.1  # Move backward
            wheel_rotation += 10.0  # Rotate wheels
        elif key == glfw.KEY_RIGHT:
            car_pos_x += 0.1  # Move right
        elif key == glfw.KEY_LEFT:
            car_pos_x -= 0.1  # Move left

def main():
    if not glfw.init():
        return

    global window
    window = glfw.create_window(1600, 900, "3D House and Car", None, None)  # Larger window size

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glEnable(GL_DEPTH_TEST)  # Enable depth testing

    # Ensure GLUT is initialized
    glutInit()

    gluPerspective(45, (1600 / 900), 0.1, 50.0)  # Adjust perspective for the larger window
    glTranslatef(0.0, 0.0, -5)

    # Set the key callback function
    glfw.set_key_callback(window, key_callback)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glRotatef(1, 3, 1, 1)
        display()

    glfw.terminate()

if __name__ == "__main__":
    main()
