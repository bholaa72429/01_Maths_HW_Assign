def triangle_ap(side1,side2,side3):
    valid = False
    error = "Whoops! Please enter an integer "
    while not valid:
       try:
           s1 = int(input(side1))
           s2 = int(input(side2))
           s3 = int(input(side3))
           if s1 > 0 and s2 > 0 and s3>0:

               peri = s1+s2+s3
               #semi-perimeter
               p=peri/2
               area =(p*(p-s1)*(p-s2)*(p-s3))**0.5

               return area, peri
           else:
               print(error)
               print()

       except ValueError:
           print(error)

a =""
keep_going = ""
while keep_going == "":

   ap = triangle_ap("Please Enter first side of triangle","Please Enter second side of triangle","Please Enter third side of triangle")
   print ("Area and Perimeter of triangle respectively",ap)



   keep_going = input("Press <enter> to calculate more or any key to quit")

# farewell user at end of game.
print("Thank you")
