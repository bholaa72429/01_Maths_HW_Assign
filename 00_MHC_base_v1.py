# import statement


# ********** Function Area **********
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


# checks that user has entered yes / no to a question
def string_checker(shape_q):
    valid_shape = [
        ["circle"],
        ["rectangle" ],
        ["square" ],
        ["triangle"]
    ]


    # initialise variables
    shape_accept = ""
    shape = ""
    # ask user for desired shape and put it in lowercase
    wanted_shape = input(shape_q).lower()

    for var_list in valid_shape:

        # if the snack is in one of the lists, return the full
        if wanted_shape in var_list:

            # Get full name of shape and put it
            # in title case so it looks nice when outputted
            shape = var_list[0].title()
            shape_accept = "yes"
            break
        # if the chosen shape is not valid, set shape_accept to no
        else:
            shape_accept = "no"

    # if the shape is not OK - ask question again.
    if shape_accept == "yes":
        return shape
    else:
        return("Invalid Shape Choice")


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
              area = 3.14*radius*radius
              peri = 2 * 3.14 * radius

              return area, peri

          # if not more than zero show error
          else:
              print()
              print(int_error)
              radius = ""

      # If integer is not entered, show error
      except ValueError:

          print(error)





# ********** Main Routine **********


a = ""
keep_going = ""
while keep_going == "":
    while a =="":
        shape  = string_checker("Input the Shape: ").lower()
        print(shape)
        if shape == "circle":
             rad_dia = yes_no("Do you have Radius of the Circle ?  ")
             area_cir , peri_cir = circle_area_peri(rad_dia)
             print("Area of Circle", area_cir)
             print("Perimeter of Circle", peri_cir)
        elif shape == "square":
            print(" step 2")
        elif shape == "rectangle":
            print(" step 3")
        elif shape == "triangle":
            print(" step 4 ")
        else:
            print("END Program")
            break
    keep_going=input("Press<enter> to play or any key to quit")
print("Thank you")

# Set up dictionaries / lists needed to hold data


# Ask the user if they have used the program before & show instruction if required


# Loop to get 'how many shapes' input


# Start of Shape Calculation Loop

# End of Shape Calculation Loop


# --- Calculate the Area & Perimeter


# Ask for rounding of answer

# ********** Printing Area **********

# The summary of shapes and their calculations
