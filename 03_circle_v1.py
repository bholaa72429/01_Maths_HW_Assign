# areperi = area and perimeter
def circle_areperi(side):

   valid = False

   error = "Whoops! Please enter an integer "
   while not valid:
       try:
           # get users input (radius)
           side = int(input(side))

            # check if its more than 0 nad then calculate
           if side > 0 :
               area = 3.14*side*side
               peri = 2 * 3.14 * side

               return area, peri
           # if not more than zero show error
           else:
               print("Please enter an number more than zero")
               print()

       except ValueError:
           print(error)

area =""
keep_going = ""
while keep_going == "":

   ap = circle_areperi("Please enter Radius of the Circle. ")
   print("Area and Perimeter of Circle respectively",ap)


    # ask for more or quit
   keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("Thank you")

