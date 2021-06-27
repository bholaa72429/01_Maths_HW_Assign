# valid shape holds list all shape
# Each item in valid shape is a list with
# valid options for each shape <full name, letter code (a -e)
# , and possible abbreviations etc>

valid_shape = [
    ["Circle", "c","ci", "cir", "a"],
    ["Rectangle", "r","re", "rec", "tangle", "b"],
    ["Square", "s","sq", "squ", "squa", "c"],
    ["Triangle", "t","tr", "tri","d"]
]

# initialise variables
shape_accept = ""
shape = ""

# loop five times to make testing quicker

for item in range(0, 5):

    # ask user for desired shape and put it in lowercase
    wanted_shape = input("Shape: ").lower()

    for var_list in valid_shape:

        # if the snack is in one of the lists, return the full
        if wanted_shape in var_list:

            # Get full name of shape and put it
            # in title case so it looks nice when outputted
            shape = var_list[0].title()
            shape_accept = "yes"
            break
        # if the chosen shape is not valid, set snack_accept to no
        else:
            shape_accept = "no"

    # if the shape is not OK - ask question again.
    if shape_accept == "yes":
        print("Shape Choice: ", shape)
    else:
        print("Invalid Shape Choice")