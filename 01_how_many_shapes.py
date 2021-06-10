# ask how many number of shapes would like to calculate

shape_no = int(input("How many Shapes? "))
shape_no_entered = 0

while shape_no_entered < shape_no:
    print("Shapes Wanted {}".format(shape_no_entered+1))
    shape_no_entered += 1

print("You have gotten to the end of the game")