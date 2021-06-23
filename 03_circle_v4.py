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
              area = 3.14*radius*radius
              peri = 2 * 3.14 * radius

              return area, peri

          # if not more than zero show error
          else:
              print()
              print(int_error)
              radius=""

      # If integer is not entered, show error
      except ValueError:

          print(error)
# main routine
area = ""
keep_going = ""
while keep_going == "":

   rad_dia = yes_no("Do you have Radius of the Circle ?  ")

   area , peri = circle_area_peri(rad_dia)
   print("Area of Circle", area)
   print("Perimeter of Circle", peri)

   # Asking about the radius of the circle


   # Ask for more or quit
   keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("---- Thank you ----")

