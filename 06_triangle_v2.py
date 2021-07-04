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
            print(error)


def triangle_ap(side1,side2,side3):

    s1 = num_check(side1)
    s2 = num_check(side2)
    s3 = num_check(side3)


    peri = s1+s2+s3
    #semi-perimeter
    p=peri/2
    area =(p*(p-s1)*(p-s2)*(p-s3))**0.5

    return area, peri

a =""
keep_going = ""
while keep_going == "":

   ap = triangle_ap("Please Enter first side of triangle","Please Enter second side of triangle","Please Enter third side of triangle")
   print ("Area and Perimeter of triangle respectively",ap)



   keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("Thank you")
