# the goal is to merge the square and rectangle function into one function

 # checking valid number input
def num_check(side):
    valid = False
    error = "Whoops! Please enter an integer "
    int_error = "ohh! Please enter an number more than zero"
    while not valid:

        try:
            # if response is less or = to 0
            side = float(input(side))
            # check if its more than 0 and then calculate
            if side > 0:
                return side
            else:
                side = ""
                print(int_error)
        except ValueError:
            print(error)

# Function for Rectangle
def square_ap(side_one):

    # get the two input of the side
    side_one = num_check(side_one)

    # calculate area and perimeter of rectangle
    area = side_one*side_one
    peri = 4*side_one
    return area, peri

# Main Routine
keep_going = ""
while keep_going == "":
    # asking for the the side of square
    area_sq, peri_sq = square_ap("Please Enter side of the square ")
    # print calculations
    print("Calculating...")
    print("Area of Square", area_sq)
    print("Perimeter of Square", peri_sq)
    keep_going = input("Press <enter> to calculate more or any key to quit")
# farewell user at end of game.
print("Thank you")

def rectangle_ap(side_one,side_two):

    # get the two input of the side
    side_one = num_check(side_one)
    side_two = num_check(side_two)
    # calculate area and perimeter of rectangle
    area = side_one*side_two
    peri = 2*(side_one+side_two)
    return area, peri


# main routine
area_rec = ""
keep_going = ""
while keep_going == "":

    # asking for the the sides
    area_rec, peri_rec = rectangle_ap("Please Enter Length of the rectangle ",
                                      "Please enter width of the rectangle")
    # print calculations
    print("Calculating...")
    print("Area of Rectangle", area_rec)
    print("Perimeter of Rectangle", peri_rec)

    keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("Thank you")

