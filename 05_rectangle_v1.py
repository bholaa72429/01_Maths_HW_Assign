# Function for Rectangle
def rectangle_ap(side_one,side_two):
   valid = False
   error = "Whoops! Please enter an integer "
   while not valid:
       try:
           # get the two input of the side
           side_one = float(input(side_one))
           side_two = float(input(side_two))
           # check if its more than 0 and then calculate
           if side_one > 0 and side_two > 0 :
               area_rec = side_one*side_two
               peri = 2*(side_one+side_two)

               return area_rec, peri
           else:
               print(error)



       except ValueError:
           print(error)

# main routine
area_rec = ""
keep_going = ""
while keep_going == "":

    area_rec, peri_rec = rectangle_ap("Please Enter Length of the rectangle ",
                                      "Please enter width of the rectangle")
    print("Calculating...")
    print("Area of Rectangle", area_rec)
    print("Perimeter of Rectangle", peri_rec)

    keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("Thank you")

