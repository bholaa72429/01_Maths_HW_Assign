# import statement
import pandas

# ********** Function Area **********
def unit_choice(question):

   to_check = ["m", "cm", "meter","centimeter","mm","inches"]
   valid = False
   while not valid:
       # ask question and put response in lowercase
       answer1 = input(question).lower()
       response = answer1.replace(" ","")
       for var_item in to_check:
           if response == var_item:
               return response
           elif response == var_item[0]:
               return var_item
       print("Please Enter a Valid unit like mm / cm / m / inch")
def dec_pl(deci_place_value):
    valid = False
    error = "Whoops! Please enter an integer "
    int_error = "Opps! Please enter an number more than or equal to zero"
    while not valid:

        try:
            # if response is less than 0
            deci_place_value = float(input(deci_place_value))
            # check if its more than 0
            if deci_place_value >= 0:
                return deci_place_value
            else:
                deci_place_value = ""
                print(int_error)
        except ValueError:
            deci_place_value = ""
            print(error)

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
    rec_side_1.append(side_one)
    rec_side_2.append(side_two)
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
              rad.append(radius)
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
    sq_side.append(side_one)
    return area, peri

def triangle_ap(side1,side2,base1):

    # inputs of the three sides

    valid = False
    error = "Invalid Input: Make Sure sum of two sides of triangle > Base of the triangle"
    print()

    while not valid:

        try:
            side_1 = num_check(side1)
            side_2 = num_check(side2)
            base = num_check(base1)

            # calculating perimeter
            peri = side_1+side_2+base
            # heron's law
            # using peri(p)to calculate area
            p = peri/2

            area_squared = (p*(p-side_1)*(p-side_2)*(p-base))
            if area_squared < 0:
                print("Oops that is not possible")
                print()
                continue

            else:

                area = (p*(p-side_1)*(p-side_2)*(p-base))**0.5
                tri_base.append(base)
                tri_side_1.append(side_1)
                tri_side_2.append(side_2)

                return area, peri

        except TypeError:
            side_1 = ""
            side_2 = ""
            base = ""
            print(error)



# ********** -Main Routine- **********

# Ask the user if they have used the program before & show instruction if required

# Loop to get '  shapes' input
# Set up dictionaries / lists needed to hold data

all_shapes = []
all_area = []
all_peri = []
rad=[]
sq_side=[]
rec_side_1=[]
rec_side_2=[]
tri_side_1=[]
tri_side_2=[]
tri_base=[]
area_peri_dict = {
    "Shapes": all_shapes,
    "Area": all_area,
    "Perimeter": all_peri

}
#dictionary for triangle's parameters
tri_dict = {"Triangle Side 1":tri_side_1,
                            "Triangle Side 2": tri_side_2,
                            "Triangle Base" : tri_base

                }
#dictionary for rectangle's parameters
rec_dict={
    "Rectangle Length":rec_side_1,
    "Rectangle Width": rec_side_2
}
#dictionary for square's parameters
sq_dict={
     "Square side": sq_side
}
#dictionary for circle's parameters
cir_dict={
    "Radius":rad
}
# decimal place option
round_place = int(dec_pl("Enter the number of Decimal Place "))
unit_1 = unit_choice("Please Enter the UNIT of the measurement")


keep_going = ""
while keep_going == "":
# Set up dictionaries / lists needed to hold data

    # Start of Shape Calculation Loop
    # checking if insert shape by user is verified
    # --- and calculate the Area & Perimeter according to that
    insert_shape = get_shape()
    print(insert_shape)


    # --- Calculate the Area & Perimeter
    if insert_shape == "Rectangle":
        # asking for the the sides
        area_1, peri_1 = rectangle_ap("Please Enter Length of the rectangle ",
                                      "Please enter width of the rectangle")

   # if circle
    elif insert_shape == "Circle":
        # Asking about the radius of the circle
        rad_dia = yes_no("Do you have Radius of the Circle ?  ")
        area_1, peri_1 = circle_area_peri(rad_dia)


    # if square
    elif insert_shape == "Square":
        area_1, peri_1 = square_ap("Please Enter side of the square ")



    # if triangle
    else:
        area_1, peri_1 = triangle_ap("Please Enter first side of triangle",
                                     "Please Enter second side of triangle",
                                     "Please Enter the base of triangle")
    # print calculations
    area = round(area_1, round_place)
    peri = round(peri_1, round_place)
    print("Calculating...")
    print("Area of {} is {} sq {} " .format(insert_shape, area, unit_1))
    print("Perimeter of {} is {} {}".format(insert_shape, peri, unit_1))

    # adding the items to the lists
    all_shapes.append(insert_shape)
    all_area.append(area)
    all_peri.append(peri)
    print(all_shapes,all_area,all_peri) # trial purpose to see what is adding into list
    keep_going = input("Press <enter> to calculate more or any key to quit")

# print details
cal_data_frame = pandas.DataFrame(area_peri_dict)
print(cal_data_frame)
tri_dict_frame = pandas.DataFrame(tri_dict)
print(tri_dict_frame)
sq_dict_frame = pandas.DataFrame(sq_dict)
print(sq_dict_frame)
rec_dict_frame = pandas.DataFrame(rec_dict)
print(rec_dict_frame)
cir_dict_frame = pandas.DataFrame(cir_dict)
print(cir_dict_frame)


# End of Shape Calculation Loop
# farewell user at end of game.
print("Thank you")



# ********** Printing Area **********

# The summary of shapes and their calculations
