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

def draw_stickman(x, y, color, pose="run", walk_phase=0):
    """Draws a stickman with a corrected 'one leg after the other' run."""
    t.pencolor(color)
    t.pensize(5)
    
    if pose == "meditate":
        # A larger, more imposing meditation pose
        hip_y = y + 30
        shoulder_y = y + 85
        head_y = y + 105
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x - 40, hip_y)
        t.goto(x, y)
        t.goto(x + 40, hip_y)
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.goto(x, head_y)
        t.dot(30)
        t.penup()
        t.goto(x, shoulder_y)
        t.pendown()
        t.goto(x - 55, shoulder_y)
        t.penup()
        t.goto(x, shoulder_y)
        t.pendown()
        t.goto(x + 55, shoulder_y)
    
    elif pose == "run":
        # Naruto run with a corrected, more realistic leg-lifting motion
        hip_y = y + 50
        shoulder_y = y + 70
        head_y = y + 80
        # Body is offset for a profile view and aggressive lean
        hip_x = x
        shoulder_x = x + 15
        head_x = x + 20
        
        # Angled Torso and Head
        t.penup()
        t.goto(hip_x, hip_y)
        t.pendown()
        t.goto(shoulder_x, shoulder_y)
        t.penup()
        t.goto(head_x, head_y)
        t.dot(30)
        
        # Arms: Swept straight back
        t.penup()
        t.goto(shoulder_x, shoulder_y)
        t.pendown()
        t.goto(x - 30, shoulder_y + 5)
        t.penup()
        t.goto(shoulder_x, shoulder_y)
        t.pendown()
        t.goto(x - 35, shoulder_y)
        
        # **Corrected Leg Animation**
        t.penup()
        if walk_phase == 0:
            # Planted leg is on the ground
            t.goto(hip_x, hip_y)
            t.pendown()
            t.goto(x - 15, y) 
            # Lifted/passing leg is bent and off the ground
            t.penup()
            t.goto(hip_x, hip_y)
            t.pendown()
            t.goto(x + 10, y + 20) # Knee
            t.goto(x + 5, y + 10)  # Foot (above ground)
        else: # Mirrored phase
            # Planted leg is on the ground
            t.goto(hip_x, hip_y)
            t.pendown()
            t.goto(x + 15, y)
            # Lifted/passing leg is bent and off the ground
            t.penup()
            t.goto(hip_x, hip_y)
            t.pendown()
            t.goto(x - 10, y + 20) # Knee
            t.goto(x - 5, y + 10)  # Foot (above ground)

def draw_scene(stickman_pos, stickman_pose, walk_phase=0):
    """Clears and redraws the entire scene for one frame of animation."""
    t.clear()
    t.pencolor("white")
    t.penup()
    t.goto(-400, GROUND_Y)
    t.pendown()
    t.goto(400, GROUND_Y)
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

    GROUND_Y = -150
    SWORD_X = 0
    stickman_pos = [-250, GROUND_Y]

    # Animation Part 1: Run to the center
    for i in range(25):
        stickman_pos[0] += 10
        draw_scene(stickman_pos, "run", walk_phase=i % 2)
        time.sleep(0.1)

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