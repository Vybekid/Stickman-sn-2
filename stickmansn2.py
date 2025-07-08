import turtle
import time

def draw_sword(x, y):
    """Draws a single sword standing upright in the ground."""
    t.pencolor("silver")
    t.pensize(3)
    t.penup()
    
    # Blade
    t.goto(x, y)
    t.pendown()
    t.goto(x, y + 60)
    
    # Guard
    t.pencolor("gold")
    t.penup()
    t.goto(x - 10, y + 15)
    t.pendown()
    t.goto(x + 10, y + 15)
    
def draw_meditating_stickman(x, y, color):
    """Draws a stickman in a cross-legged meditation pose."""
    t.pencolor(color)
    t.pensize(5)
    
    # Crossed Legs
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x - 30, y + 30)
    t.goto(x, y)
    t.goto(x + 30, y + 30)
    
    # Torso and Head
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x, y + 60) # Torso
    t.dot(30) # Head
    
    # Arms resting on knees
    t.goto(x - 30, y + 30)
    t.penup()
    t.goto(x, y + 50) # Shoulder
    t.pendown()
    t.goto(x + 30, y + 30)

# --- Main Program ---
if __name__ == "__main__":
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Story of Stickman: Episode 2 - The Calm")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()

    # Define positions
    GROUND_Y = -150
    STICKMAN_X = 0
    
    # Draw the ground
    t.pencolor("white")
    t.penup()
    t.goto(-400, GROUND_Y)
    t.pendown()
    t.goto(400, GROUND_Y)
    
    # Draw the scene elements
    draw_meditating_stickman(STICKMAN_X, GROUND_Y, "red")
    draw_sword(STICKMAN_X - 70, GROUND_Y)
    draw_sword(STICKMAN_X + 70, GROUND_Y)
    
    # Draw the episode title
    t.pencolor("gray")
    t.penup()
    t.goto(0, 200)
    t.write("Episode 2: The Calm", align="center", font=("Arial", 30, "normal"))

    # Update the screen to show everything at once
    screen.update()

    time.sleep(5) # Pause to view the scene
    
    turtle.done()