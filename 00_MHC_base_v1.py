# import statement


# ********** Function Area **********
# checks that user has entered yes / no to a question
def yes_no(question):

   to_check = ["yes", "no"]

   valid = False
   while not valid:

       # ask question and put response in lowercase
       # answer = answer of the user
       answer = input(question).lower()
       # check if input any space
       response = answer.replace(" ","")

       for var_item in to_check:
           if response == var_item:
               return response
           elif response == var_item[0]:
               return var_item
       print("Please Answer (yes / no). ")

# area_peri = area and perimeter
def circle_area_peri(ans):
   valid = False
   error = "Whoops! Please enter an integer. "
   int_error = "oops! Please enter an number more than zero. "

   while not valid:

       try:
           enterd = ans
           if enterd == "yes":
               # get users input (radius)
               radius = float(input("Please Enter Radius. "))

               # if user has the diameter
           else:
               diameter = float(input("Please Enter Diameter. "))
               # work out teh radius
               radius = diameter / 2
               print("Calculating ...")

           # check if its more than 0 nad then calculate
           if radius > 0:
               area = 3.14 * radius * radius
               peri = 2 * 3.14 * radius

               return area, peri

           # if not more than zero show error
           else:
               print()
               print(int_error)
               # radius=""

       # If integer is not entered, show error
       except ValueError:

           print(error)

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
               area = side * side
               peri = 4 * side

               return area, peri
           else:
               print(int_error)
               side = ""


       except ValueError:
           print(error)

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
                return response

        except ValueError:
            print(error)



# ********** Main Routine **********
#
area_sqr = ""
area_cir = ""
keep_going = ""
while keep_going == "":

   area_sqr, peri_sqr = square_area_peri("Please enter side of the Square. ")
   print("Calculating...")
   print("Area of Square", area_sqr)
   print("Perimeter of Square", peri_sqr)
# Set up dictionaries / lists needed to hold data


# Ask the user if they have used the program before & show instruction if required


# Loop to get 'how many shapes' input


# Start of Shape Calculation Loop








# End of Shape Calculation Loop


# --- Calculate the Area & Perimeter


# Ask for rounding of answer

# ********** Printing Area **********

# The summary of shapes and their calculations
