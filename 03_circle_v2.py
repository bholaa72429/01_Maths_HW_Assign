
# areperi = area and perimeter
# checks that input is an integer/ float which is more than zero
# has a custom error mess
def circle_areperi(radius, error):

   valid = False

   error = "Whoops! Please enter an integer "
   while not valid:
       try:
           # get users input (radius)
           radius = float(input(radius))

            # check if its more than 0 nad then calculate
           if radius > 0 :
               area = 3.14*radius*radius
               peri = 2 * 3.14 * radius

               return area, peri

       # If integer is not entered, show error
       except ValueError:
           print(error)

area = ""
keep_going = ""
while keep_going == "":

   circle_ap = circle_areperi("Please enter Radius of the Circle.",
                              "Ohh! Please enter an number more than zero")
   print("Area and Perimeter of Circle respectively",circle_ap)


   # ask for more or quit
   keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("---- Thank You ----")

