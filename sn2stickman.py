import turtle
import time
import math

def draw_virus_and_rotate_smoothly():
    """
    Draws the virus, then makes the completed shape rotate smoothly on a
    central axis, like a 3D object.
    """
    try:
        # --- Setup the Screen and Turtle ---
        screen = turtle.Screen()
        screen.bgcolor("black")
        screen.title("Smooth Virus Rotation")
        t = turtle.Turtle()
        t.color("lime")
        t.pensize(1)
        t.hideturtle()

        # ==========================================================
        # PHASE 1: Draw the virus visibly for the first time
        # ==========================================================
        t.speed(10)
        
        v = 200
        while v > 0:
            t.left(v)
            t.forward(v * 2)
            t.backward(v * 2) # Draw a centered version
            v -= 1
        
        time.sleep(1)

        # =================================================================
        # PHASE 2: Calculate and store the "blueprint" of the virus once
        # =================================================================
        t.clear() # Clear the initial drawing
        points = [] # This list will store the endpoints of each spike
        v = 200
        while v > 0:
            t.left(v)
            t.forward(v * 2)
            points.append(t.pos()) # Save the coordinate of the spike's tip
            t.backward(v * 2) # Return to center
            v -= 1

        # ===============================================================
        # PHASE 3: Animate the rotation using the stored blueprint
        # ===============================================================
        screen.tracer(0) # Turn off automatic updates for max speed
        rotation_angle = 0
        
        while True:
            t.clear() # Clear the last frame
            
            # Convert degrees to radians for the math functions
            rad_angle = math.radians(rotation_angle)
            cos_angle = math.cos(rad_angle)
            sin_angle = math.sin(rad_angle)

            # --- Redraw the entire virus from the blueprint ---
            for x, y in points:
                # Apply the 2D rotation formula to each point
                new_x = x * cos_angle - y * sin_angle
                new_y = x * sin_angle + y * cos_angle
                
                # Draw a line from the center to the new rotated point
                t.penup()
                t.goto(0, 0)
                t.pendown()
                t.goto(new_x, new_y)
            # --------------------------------------------------
            
            screen.update() # Show the newly drawn frame
            rotation_angle += 1 # Increment angle for the next frame (1 degree is smooth)
            time.sleep(0.01) # Small delay to control frame rate

    except turtle.Terminator:
        print("Drawing terminated by user.")

# --- Run the function ---
if __name__ == "__main__":
    draw_virus_and_rotate_smoothly()