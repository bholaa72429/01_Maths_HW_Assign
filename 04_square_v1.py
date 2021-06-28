# Function Goes Here

# calculates the area and peri for the square
def square_area_peri(side):
   valid = False
   error = "Whoops! Please enter an integer "
   int_error = "ohh! Please enter an number more than zero"
   while not valid:
       try:
           side = float(input(side))
           # check if its more than 0 and then calculate
           if side > 0:
               area = side*side
               peri = 4 * side

               return area, peri
           else:
               print(int_error)
               side = ""


       except ValueError:
           print(error)

# main routine
area_sqr = ""
keep_going = ""
while keep_going == "":

   # ask for the sides
   area_sqr, peri_sqr = square_area_peri("Please enter side of the Square. ")

   # print calculations
   print("Calculating...")
   print("Area of Square", area_sqr)
   print("Perimeter of Square", peri_sqr)


   # more or end
   print()
   keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("Thank you")

