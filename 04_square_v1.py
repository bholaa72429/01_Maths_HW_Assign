# Function Goes Here

# calculates the area and peri for the square
def square_area_peri(side):
   valid = False
   error = "Whoops! Please enter an integer "
   while not valid:
       try:
           side = int(input(side))
           # check if its more than 0 and then calculate
           if side > 0 :
               area = side*side
               peri = 4 * side

               return area, peri
           else:
               print(error)
               print()

       except ValueError:
           print(error)

# main routine
area = ""
keep_going = ""
while keep_going == "":

   area_peri = square_area_peri("Please enter side of the Square")
   area, peri = square_area_peri(area_peri)
   print("Area of Square", area)
   print("Perimeter of Square", peri)




   keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("Thank you")


