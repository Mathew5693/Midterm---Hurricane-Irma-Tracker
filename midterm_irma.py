import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(1025, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-110, 0, 0, 50)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="atlantic-hurricane-tracking-map.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    # for some reason I have to move it 15 less than than 1025 width
    canvas.create_image(-1010, -600, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("hurricane.gif")
    t.shape("hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # opens / reads file into a list and strips unnecessary information
    # all that is needed is longitude, latitude, and windspeed
    with open('irma.csv', 'r') as oFile:
        lines = [line.strip() for line in oFile.readlines()]
        lines = lines[1:]
        lines = [line.split(',') for line in lines]
        lines = [line[2:5] for line in lines]

    # Sets up turtle a first coordinate
    t.penup()

    start = lines[0]
    yStart = start[0]
    xStart = start[1]

    # cast xstart and ystart to float
    xStart = float(xStart)
    yStart = float(yStart)

    # hides turtle til it reaches starting point
    t.hideturtle()

    # used casted x and y start as setx/sety coords
    t.setx(xStart)
    t.sety(yStart)

    # elif statements to change turtle color and line size based on wind speed (catagory 1-5)
    # for loop incremented based on number of total elements in the oFile list
    # that breaks down into a smaller list of 3 elements so that long lat and wind speed can be used
    # to update turtle and hurricane categories
    elements = len(lines)
    for i in range(elements):

        # separate list to smaller list containing the 3 elements needed to update hurricane
        update = lines[i]

        # get x and y from list
        y = update[0]
        x = update[1]
        cat = update[2]
        cat = int(cat)
        # cast list x and y as floats
        x = float(x)
        y = float(y)

        # if-else to compare wind speeds to determine category
        # colors hurricane based off category 1-5 & changes pen thickness
        if cat < 74:

            t.width(1)
            t.pencolor("black")

        elif cat >= 74 and cat <= 95:

            t.width(3)
            t.pencolor("blue")
            t.write("1", font=("Arial", 20))

        elif cat >= 96 and cat <= 110:

            t.width(5)
            t.pencolor("green")
            t.write("2", font=("Arial", 20))

        elif cat >= 110 and cat <= 129:

            t.width(7)
            t.pencolor("yellow")
            t.write("3", font=("Arial", 20))

        elif cat >= 130 and cat <= 156:

            t.width(8)
            t.pencolor("orange")
            t.write("4", font=("Arial", 20))

        elif cat >= 158:

            t.width(11)
            t.pencolor("red")
            t.write("5", font=("Arial", 20))

        i += 3
        # turtle is shown and starts the path incremented by the loop
        t.showturtle()
        t.pendown()
        t.goto(x, y)

    wn.exitonclick()

if __name__ == "__main__":
    irma()
