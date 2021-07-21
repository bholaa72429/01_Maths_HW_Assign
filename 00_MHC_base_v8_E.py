# import statement
import pandas
import operator

# ********** Function Area **********

# checks units and yes/no response if invalid than gives error
def checker(question,list_choice,error):
   valid = False
   while not valid:

       # ask question and put response in lowercase
       # answer = answer of the user
       answer = input(question).lower()
       # check if input any space
       response = answer.replace(" ","")

       for var_item in list_choice:
           if response == var_item:
               return response
           elif response == var_item[0]:
               return var_item
       print(error)

# checks the input and comparing the value
def num_check(question,error,int_error,value,place):
    valid = False

    while not valid:

        try:
            # checks if it's an integer input or else changes to a float
            if place == "integer" :
                number = int(input(question))
            else:
                number = float(input(question))

            #comparing number >= value-0 for decimal place and 1 for Number check
            if operator.__ge__(number,value):
                return number
            else:
                print(int_error)
        except ValueError:
            print(error)

# provides instruction to the user
def instructions():

    print("****** Welcome to Area & Perimeter Calculator ******")
    to_check = ["yes", "no"]

    first_time = checker("\nHave you used this calculator before? ",to_check,"Please Enter YES or NO")

    if first_time == "yes":
        return ""

    print()
    print("***** Instructions ******")
    print()
    print("This program will ask you for...")
    print("- Choose from following shapes - Square, Rectangle, Triangle, Circle")
    print("- Pick the number of decimal place you want the area and perimeter output")
    print("- Pick unit for the dimensions of the shape (Valid unit are mm / cm / m / inch)")
    print("- And the dimension of the shape!!")
    print()
    print("At the end you will be provided with the summary of the shape with dimension entered and Area & Perimeter.")
    print()
    print("The data will also be written to a text file which has the AP_Calc.csv "
          " name .")
    print("Note: You can quit by pressing any letter at the end of shape calculation OR 'xxx' at shape input to end program ")

# checks valid shape option and gives error for invalid
def get_shape():
    # list of  valid shape inputs
    # , and possible abbreviations etc>
    valid_shape = [
        ["circle", "c","ci", "cir"],
        ["rectangle", "r","re", "rec", "tangle"],
        ["square", "s","sq", "squ", "squa"],
        ["triangle", "t","tr", "tri"]]
    # holds shape order for a single user.
    wanted_shape = ""
    while wanted_shape !="xxx":
        # ask user for desired shape and put it in lowercase
        print()
        print("OPTION TO PICK FROM: Circle, Rectangle, Square, Triangle")
        wanted_shape = input("Enter Shape: ").lower()

        # remove white space around shapes
        wanted_shape = wanted_shape.strip()
        if wanted_shape == "xxx":
            return wanted_shape
        # check if shape is valid
        is_valid = "yes"
        for var_list in valid_shape:
            # if the shape is in one of the lists, return the full
            if wanted_shape in var_list:

                # Get full name of shape abd put it in title case so it looks nice when outputted
                wanted_shape = var_list[0].title()
                is_valid = "yes"
                break
            # if the chosen option is not valid, set is_valid to no
            else:
                is_valid = "no"

        # if the shape is not OK - ask question again.
        if is_valid == "yes":
            shape_choice = wanted_shape
        else:
            shape_choice = "invalid choice"

        if shape_choice == "invalid choice":
            print(" Please enter a valid Shape Option ")

        # check that shape is not the exit code before adding
        if shape_choice != "xxx" and shape_choice != "invalid choice":
            return shape_choice

# calculates area and perimeter for square and rectangle
def squ_rec_ap(side_one,side_two):

    # calculating for  square
    if side_one == side_two:
        # calculate area and perimeter of square
        area = side_one*side_two
        peri = 4*side_one
        # adding dimensions of the shape to the list
        given_data = "|Side: {} |".format(side_one)
        dimensions.append(given_data)
        return area, peri
    # else calculating rectangle
    else:
        side_one = num_check(side_one,"Whoops! Please enter an integer ",
                             "ohh! Please enter an number more than zero",
                             1,"float")

        side_two = num_check(side_two,"Whoops! Please enter an integer ",
                             "ohh! Please enter an number more than zero",
                             1,"float")
        # calculate area and perimeter of rectangle
        area = side_one*side_two
        peri = 2*(side_one+side_two)
        # adding dimensions of the shape to the list
        given_data = "|Length: {}| Width: {} |".format(side_one, side_two)
        dimensions.append(given_data)
        return area, peri

# calculates area and perimeter for circle
def circle_area_peri(ans):

      enterd = ans
      if enterd == "yes":
          # get users input (radius)
          radius = num_check("Enter Radius of the Circle","Whoops! Please enter an integer ","ohh! Please enter an number more than zero",1,"float")

       # if user has the diameter
      else:
          diameter =num_check("Enter Diameter of the Circle","Whoops! Please enter an integer ","ohh! Please enter an number more than zero",1,"float")
          # work out the radius
          radius = diameter / 2


      #calculate the area and peri of circle
      area = 3.14*radius*radius
      peri = 2 * 3.14 * radius
      # adding dimensions of the shape to the list
      given_data = "|Radius: {} |".format(radius)
      dimensions.append(given_data)
      return area, peri

# calculates area and perimeter for triangle
def triangle_ap(choice):
    valid = False

    while not valid:


            enterd = choice
            if enterd == "yes":
                 # get users input of three side of the triangle
                side_1 = num_check("Enter Side One:","Whoops! Please enter an integer ",
                                   "ohh! Please enter an number more than zero",1,"float")

                side_2 = num_check("Enter Side Two:","Whoops! Please enter an integer ",
                                   "ohh! Please enter an number more than zero",1,"float")
                base = num_check("Enter Base:","Whoops! Please enter an integer ",
                                 "ohh! Please enter an number more than zero",1,"float")

                # calculating perimeter
                peri = side_1+side_2+base
                # heron's law
                # using peri(p)to calculate area
                p = peri/2

                # checking if the triangle is valid
                area_squared = (p*(p-side_1)*(p-side_2)*(p-base))
                if area_squared <= 0:
                    print("Oops!! This is not possible. *Try Again*")
                    print()
                    continue

                else:

                    area = (p*(p-side_1)*(p-side_2)*(p-base))**0.5
                    # adding dimensions of the shape to the list
                    given_data = "|Side: {} |Side: {} |Base: {} |".format(side_1, side_2,base)
                    dimensions.append(given_data)
                    return area, peri

           # if user has the height and base of triangle
            else:
                print("~NOTE: Perimeter Cannot be Calculated . Perimeter = 0~")
                height_1 = num_check("Enter Height: ","Whoops! Please enter an integer ",
                                     "ohh! Please enter an number more than zero",1,"float")
                base_1 =  num_check("Enter Base: ","Whoops! Please enter an integer ",
                                    "ohh! Please enter an number more than zero",1,"float")
                area= (base_1*height_1)/2
                peri = 0
                given_data = "|Height: {} |Base: {} |".format(height_1,base_1)
                dimensions.append(given_data)
                return area, peri

# ********** -Main Routine- **********

# Ask the user if they have used the program before & show instruction if required
instructions()

# Loop to get '  shapes' input
# Set up dictionaries / lists needed to hold data
all_shapes = []
dimensions =[]
all_area = []
all_peri = []
area_peri_dict = {
    "   Shape  ": all_shapes,
    "   Given Dimensions  ": dimensions,
    "   Area  ": all_area,
    "   Perimeter": all_peri
}
# list for the checker function
to_check = ["yes", "no"]
to_check1 = ["m", "cm", "meter","centimeter","mm","inches"]
# decimal place input
print()
round_place = int(num_check("Enter the number of Decimal Place = ",
                         "Whoops! Please enter an integer",
                         "Opps! Please enter an number more than or equal to zero",
                         0,"integer"))
# unit input
unit_1 = checker("Please Enter the UNIT of the measurement = ",
                 to_check1,"Please Enter a Valid unit like mm / cm / m / inch")

insert_shape = ""
while insert_shape != "xxx":
# Set up dictionaries / lists needed to hold data

    # Start of Shape Calculation Loop
    # checking if insert shape by user is verified
    # --- and calculate the Area & Perimeter according to that
    insert_shape = get_shape()

    # if user input is rectangle
    if insert_shape == "Rectangle":
        # asking for the the sides
        area_1, peri_1 = squ_rec_ap("Please Enter Length of the rectangle = ",
                                      "Please enter width of the rectangle")

   # if circle
    elif insert_shape == "Circle":
        # Asking about the radius of the circle
        rad_dia = checker("Do you have Radius of the Circle ?  ",to_check,"Please Answer (yes / no). ")
        area_1, peri_1 = circle_area_peri(rad_dia)


    # if square
    elif insert_shape == "Square":
        # numcheck added to check the side of the square 
        sq_side = num_check("Enter Side of square = ","Whoops! Please enter an integer ",
                            "ohh! Please enter an number more than zero",1,"float")
        # side of the square given to rectangle same for length and width
        area_1, peri_1 = squ_rec_ap(sq_side,sq_side)


    # if triangle
    elif insert_shape == "Triangle":

        choice = checker("Do you have 3 sides measurement of triangle ?  ",to_check,"Please Answer (yes / no). ")
        area_1, peri_1 = triangle_ap(choice)

    # if input is xxx - end the program
    elif insert_shape == "xxx":
        break


    # print calculations
    if round_place == 0:
        area = int(area_1)
        peri = int(peri_1)
    else:
        area = round(area_1, round_place)
        peri = round(peri_1, round_place)

    print("Calculating...")
    print("Area of {} is {} square {} " .format(insert_shape, area, unit_1))
    print("Perimeter of {} is {} {}".format(insert_shape, peri, unit_1))
    area_unit = "{} square {}".format(area,unit_1)
    peri_unit = "{} {}".format(peri,unit_1)

# adding the items to the lists
    all_shapes.append(insert_shape)
    all_area.append(area_unit)
    all_peri.append(peri_unit)


    insert_shape = input("Press <enter> to calculate more or XXX to quit").lower()

# ********** Printing Area **********
# The summary of shapes and their calculations
# prints details
print()
print("**** Calculation Summary ****")
print()

# Set up columns to be printed...
calc_data_frame = pandas.DataFrame(area_peri_dict)
print(calc_data_frame)
#write dataframe to csv file
calc_data_frame.to_csv("Area_Peri_Calc.csv")

# end of Shape Calculation Loop
# farewell user at end of game.
print()
print("***-Thank You For Using The Calculator-***")
print("***-Note: for full details, please see the csv file called 'Area_Peri_Calc.csv -***")
print("*** You can also open this file in exel for better presentation  ***")

