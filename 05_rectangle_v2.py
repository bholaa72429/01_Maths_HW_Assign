# checking valid number input
def num_check():
    valid = False
    error = "Whoops! Please enter an integer "
    int_error = "ohh! Please enter an number more than zero"
    while not valid:

        try:
            response = float(input(side))

            # if response is less or = to 0
            side = float(input(side))
            # check if its more than 0 and then calculate
            if side > 0:
                continue
            else:
                print(int_error)

        except ValueError:
            print(error)

# Function for Rectangle
def rectangle_ap(side_one,side_two):
   valid = False

   while not valid:
       try:
           # get the two input of the side
           side_one = float(input(side_one))
           side_two = float(input(side_two))

           # check if its more than 0 and then calculate
               num_check()
               area_rec = side_one*side_two
               peri = 2*(side_one+side_two)

               return area_rec, peri


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

