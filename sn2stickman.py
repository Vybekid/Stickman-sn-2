import turtle
import time

def draw_virus_slower():
    """
    This code draws the virus animation at a slower, non-instant speed.
    """
    try:
        # --- Setup the Screen ---
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Virus Animation - Slower Speed")
        
        # --- Setup the Turtle (our pen) ---
        t = turtle.Turtle()
        t.color("lime")
        t.pensize(1)
        
        # --- NEW: Set speed to 'fast' (10) instead of 'instant' (0) ---
        t.speed(10) 
        
        # Add the 3-second delay
        time.sleep(3)

        # --- The Drawing Logic ---
        v = 200
        while v > 0:
            t.left(v)
            t.forward(v * 2)
            v = v - 1

        t.hideturtle()
        screen.mainloop()

    except turtle.Terminator:
        print("Drawing terminated by user.")

# --- Run the function ---
if __name__ == "__main__":
    draw_virus_slower()