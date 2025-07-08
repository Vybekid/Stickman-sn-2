import turtle
import time

def draw_sword(x, y):
    """Draws a single sword standing upright in the ground."""
    t.pencolor("silver")
    t.pensize(3)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y + 60) # Blade
    t.pencolor("gold")
    t.penup()
    t.goto(x - 10, y + 15) # Guard
    t.pendown()
    t.goto(x + 10, y + 15)

def draw_stickman(x, y, color, pose="walk", walk_phase=0):
    """Draws a stickman in either a walking or meditating pose."""
    t.pencolor(color)
    t.pensize(5)
    hip_y = y + 50
    head_y = y + 100

    if pose == "meditate":
        t.penup()
        t.goto(x, y) # Start at base for legs
        t.pendown()
        t.goto(x - 30, y + 30) # Crossed leg
        t.goto(x, y)
        t.goto(x + 30, y + 30) # Other crossed leg
        t.goto(x, y)
        t.goto(x, head_y) # Torso
        t.dot(30) # Head
        t.goto(x - 30, y + 30) # Arm
        t.penup()
        t.goto(x, y + 50) # Shoulder
        t.pendown()
        t.goto(x + 30, y + 30) # Other arm
    elif pose == "walk":
        # Torso and Head
        t.penup()
        t.goto(x, hip_y)
        t.pendown()
        t.goto(x, head_y)
        t.dot(30)
        t.goto(x, head_y - 20) # Neck
        # Alternating arms and legs for walking
        if walk_phase == 0:
            t.goto(x + 15, y + 20) # Forward arm
            t.penup()
            t.goto(x, head_y - 20)
            t.pendown()
            t.goto(x - 15, y + 20) # Back arm
            t.penup()
            t.goto(x, hip_y)
            t.pendown()
            t.goto(x - 20, y) # Back leg
            t.penup()
            t.goto(x, hip_y)
            t.pendown()
            t.goto(x + 20, y) # Forward leg
        else: # Mirrored phase
            t.goto(x - 15, y + 20)
            t.penup()
            t.goto(x, head_y - 20)
            t.pendown()
            t.goto(x + 15, y + 20)
            t.penup()
            t.goto(x, hip_y)
            t.pendown()
            t.goto(x + 20, y)
            t.penup()
            t.goto(x, hip_y)
            t.pendown()
            t.goto(x - 20, y)

def draw_scene(stickman_pos, stickman_pose, walk_phase=0):
    """Clears and redraws the entire scene for one frame of animation."""
    t.clear()
    # Draw ground
    t.pencolor("white")
    t.penup()
    t.goto(-400, GROUND_Y)
    t.pendown()
    t.goto(400, GROUND_Y)
    # Draw scene elements
    draw_stickman(stickman_pos[0], stickman_pos[1], "red", stickman_pose, walk_phase)
    draw_sword(SWORD_X - 70, GROUND_Y)
    draw_sword(SWORD_X + 70, GROUND_Y)
    screen.update()

# --- Main Program ---
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Story of Stickman: Episode 2 - Flawless Victory")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()

    # Define positions
    GROUND_Y = -150
    SWORD_X = 0
    stickman_pos = [-250, GROUND_Y] # Start off-screen

    # Animation Part 1: Walk to the center
    for i in range(25):
        stickman_pos[0] += 10 # Move stickman to the right
        draw_scene(stickman_pos, "walk", walk_phase=i % 2)
        time.sleep(0.08)

    # Animation Part 2: Sit down and meditate
    draw_scene(stickman_pos, "meditate")
    time.sleep(1)

    # Final text reveal
    t.pencolor("gold")
    t.penup()
    t.goto(0, 200)
    t.write("Flawless Victory", align="center", font=("Impact", 40, "normal"))
    screen.update()
    
    turtle.done()