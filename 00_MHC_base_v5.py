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
            side = ""
            print(error)
#Function to check the string
def string_check(choice, options):
    is_valid = "yes"
    chosen = ""
    for var_list in options:
        # if the shape is in one of the lists, return the full
        if choice in var_list:

            # Get full name of shape abd put it in title case so it looks nice when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break
        # if the chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if the snack is not OK - ask question again.
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"
# Function get shape
def get_shape():
    # llist of  valid shape inputs  <full name, letter code (a -e)
    # , and possible abbreviations etc>
    valid_shape = [
        ["circle", "c","ci", "cir", "a"],
        ["rectangle", "r","re", "rec", "tangle", "b"],
        ["square", "s","sq", "squ", "squa", "c"],
        ["triangle", "t","tr", "tri","d"],]
    # holds shape order for a single user.
    wanted_shape = ""
    while wanted_shape !="xxx":
        # ask user for desired shape and put it in lowercase
        wanted_shape = input("Enter Shape: ").lower()

        # remove white space around shapes
        wanted_shape = wanted_shape.strip()

        # check if shape is valid
        shape_choice = string_check(wanted_shape,valid_shape)
        if shape_choice == "invalid choice":
            print(" Please enter a valid Shape Option ")

        # check that shape is not the exit code before adding
        if shape_choice != "xxx" and shape_choice != "invalid choice":
            return shape_choice

# Function for Rectangle
def rectangle_ap(side_one,side_two):

    # get the two input of the side
    side_one = num_check(side_one)
    side_two = num_check(side_two)
    # calculate area and perimeter of rectangle
    area = side_one*side_two
    peri = 2*(side_one+side_two)
    return area, peri

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
              # print("Calculating ...")

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

def square_ap(side_one):

    # get the two input of the side
    side_one = num_check(side_one)

    # calculate area and perimeter of rectangle
    area = side_one*side_one
    peri = 4*side_one
    return area, peri

def triangle_ap(side1,side2,side3):

    # inputs of the three sides
    side_1 = num_check(side1)
    side_2 = num_check(side2)
    side_3 = num_check(side3)

    # calculating perimeter
    peri = side_1+side_2+side_3
    # using peri(p) to calculate area
    p = peri/2
    area =(p*(p-side_1)*(p-side_2)*(p-side_3))**0.5

    return area, peri

def shape_calcu():
  insert_shape = get_shape()
  print(insert_shape)
    # decimal place option
  round_place = int(num_check("Enter the rounding Place value no"))
  # --- Calculate the Area & Perimeter
  if insert_shape == "Rectangle":
        # asking for the the sides
        area_rec1, peri_rec1 = rectangle_ap("Please Enter Length of the rectangle ",
                                            "Please enter width of the rectangle")
        # print calculations

        area_rec = round(area_rec1, round_place)
        peri_rec = round(peri_rec1, round_place)
        print("Calculating...")
        print("Area of Rectangle", area_rec )
        print("Perimeter of Rectangle", peri_rec)

    # if circle
  elif insert_shape == "Circle":
        # Asking about the radius of the circle
        rad_dia = yes_no("Do you have Radius of the Circle ?  ")

        area_cir, peri_cir = circle_area_peri(rad_dia)
        print("Calculating...")
        print("Area of Circle", area_cir)
        print("Perimeter of Circle", peri_cir)

    # if square
  elif insert_shape == "Square":
        area_sq, peri_sq = square_ap("Please Enter side of the square ")
        # print calculations
        print("Calculating...")
        print("Area of Square", area_sq)
        print("Perimeter of Square", peri_sq)

    # if triangle
  else:
        area_tri, peri_tri = triangle_ap("Please Enter first side of triangle",
                                         "Please Enter second side of triangle",
                                         "Please Enter third side of triangle")
        print("Calculating...")
        print("Area of Square", area_tri)
        print("Perimeter of Square", peri_tri)



# End of Shape Calculation Loop
# farewell user at end of game.




# ********** -Main Routine- **********
# Loop to get '  shapes' input

keep_going = ""
while keep_going == "":
  shape_calcu()
    # Start of Shape Calculation Loop
    # checking if insert shape by user is verified
    # --- and calculate the Area & Perimeter according to that
    # insert_shape = get_shape()
    # print(insert_shape)
    # # decimal place option
    # round_place = int(num_check("Enter the rounding Place value no"))




    # # --- Calculate the Area & Perimeter
    # if insert_shape == "Rectangle":
    #     # asking for the the sides
    #     area_rec1, peri_rec1 = rectangle_ap("Please Enter Length of the rectangle ",
    #                                         "Please enter width of the rectangle")
    #     # print calculations

    #     area_rec = round(area_rec1, round_place)
    #     peri_rec = round(peri_rec1, round_place)
    #     print("Calculating...")
    #     print("Area of Rectangle", area_rec )
    #     print("Perimeter of Rectangle", peri_rec)

    # # if circle
    # elif insert_shape == "Circle":
    #     # Asking about the radius of the circle
    #     rad_dia = yes_no("Do you have Radius of the Circle ?  ")

    #     area_cir, peri_cir = circle_area_peri(rad_dia)
    #     print("Calculating...")
    #     print("Area of Circle", area_cir)
    #     print("Perimeter of Circle", peri_cir)

    # # if square
    # elif insert_shape == "Square":
    #     area_sq, peri_sq = square_ap("Please Enter side of the square ")
    #     # print calculations
    #     print("Calculating...")
    #     print("Area of Square", area_sq)
    #     print("Perimeter of Square", peri_sq)

    # # if triangle
    # else:
    #     area_tri, peri_tri = triangle_ap("Please Enter first side of triangle",
    #                                      "Please Enter second side of triangle",
    #                                      "Please Enter third side of triangle")
    #     print("Calculating...")
    #     print("Area of Square", area_tri)
    #     print("Perimeter of Square", peri_tri)

  keep_going = input("Press <enter> to calculate more or any key to quit")

# End of Shape Calculation Loop
# farewell user at end of game.
print("Thank you")


# Set up dictionaries / lists needed to hold data


# Ask the user if they have used the program before & show instruction if required







# Ask for rounding of answer and Unit for answer

# ********** Printing Area **********

# The summary of shapes and their calculations
