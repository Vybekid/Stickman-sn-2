import turtle 
import time 

def draw_virus():
    try:
        screen = turtle.Screen() 
        screen.bgcolor("black")
        screen.title("Virus Animation")

        t = turtle.Turtle()
        t.color("lime")
        t.pensize(1)

        t.speed(10)

        t.sleep(3)

        v = 200
        while v > 0:
            t.left(v)
            t.forward(v * 2)
            v = v - 1

        t.hideturtle()
        screen.mainloop()

    except turtle.Terminator:
        print("Drawing terminated by user.")

if __name__ == "__main__": 
    draw_virus()
    