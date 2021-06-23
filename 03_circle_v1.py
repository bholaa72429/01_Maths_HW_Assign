# area_peri = area and perimeter
# function calculates the area and perimeter of a circle
def circle_area_peri(radius):
    valid = False
    error = "Whoops! Please enter an integer "
    int_error = "Ohh! Please enter an number more than zero "

    while not valid:

       try:
           # get users input (radius)
           radius = int(input(radius))

           # check if its more than 0 nad then calculate
           if radius > 0:
               area = 3.14*radius*radius
               peri = 2 * 3.14 * radius

               return area, peri
           # if not more than zero show error
           else:
               print(int_error)
               radius = ""
       # If integer is not entered, show error
       except ValueError:
           print(error)

area = ""
keep_going = ""
while keep_going == "":

    # Asking about the radius of the circle
   circle_ap = circle_area_peri("Please enter Radius of the Circle. ")
   print("Area and Perimeter of Circle respectively",circle_ap)

    # Ask for more or quit
   keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("---- Thank you ----")

