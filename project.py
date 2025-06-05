import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

try:
    num_shapes = int(input("Enter the number of shapes to draw: "))
    if num_shapes < 1:
        raise ValueError("Number of shapes must be at least 1.")

    size = int(input("Enter the length of each side: "))
    if size < 1:
        raise ValueError("Side length must be at least 1.")

    color = input("Enter the pen color: ").strip()
    if not color:
        raise ValueError("Color cannot be empty.")

    pen.color(color)

    sides=int(input("Enter the number of sides for each polygon: "))
    if sides < 3:
        raise ValueError("Number of sides must be at least 3.")

except Exception as e:
    print("Invalid input. Please try again.")
    print("Details:", e)

else:
    angle_polygon = 360 / sides
    angle_between_shapes = 360 / num_shapes

    for i in range(num_shapes):
        for j in range(sides):
            pen.forward(size)
            pen.right(angle_polygon)
        pen.right(angle_between_shapes)

    screen.mainloop()
