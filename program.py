import turtle

def draw_text(text, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("blue")
    turtle.write(text, align="center", font=("Arial", 24, "bold"))

def main():
    # Set up the screen
    turtle.bgcolor("black")
    turtle.title("Happy New Year")

    # Draw the text
    draw_text("Happy New Year!", 0, 0)

    # Hide the turtle and finish
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()