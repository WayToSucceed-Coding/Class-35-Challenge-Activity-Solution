import turtle

screen = turtle.Screen()
screen.title("Turtle Basics")

pen = turtle.Turtle()
#pen.color("green")

try:
    color=input("Enter the color pen: ")
    pen.color(color)
    shape=input("Do you want to draw a polygon or a star?Enter 'polygon' or 'star': ").strip().lower()
    if shape not in ['polygon', 'star']:
        raise ValueError("Invalid shape type. Please enter 'polygon' or 'star'.")
    if shape == 'polygon':
        sides = int(input("Enter the number of sides for the polygon: "))
        if sides < 0:
            raise ValueError("Number of sides cannot be negative.")
        angle = 360 / sides
        loop=sides
    else:
        points= int(input("Enter the number of points for the star: "))
        angle= 180-(180/5)  
        loop=points
    
except Exception as e:
    print("Something went wrong.")
    print("Details:\n", e)
else:
    for i in range(loop):
        pen.forward(100)
        pen.right(angle)           

screen.mainloop()




