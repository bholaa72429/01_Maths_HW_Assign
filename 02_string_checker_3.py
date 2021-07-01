
# Function goes here
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
        ["triangle", "t","tr", "tri","d"],
]

    # holds shape order for a single user.
    shape_input = []

    wanted_shape = ""


    shape_row = []

    # ask user for desired snack and put it in lowercase
    wanted_shape = input("Enter Shape: ").lower()

    if  wanted_shape == "end":
        return shape_input

    # remove white space around shapes
    wanted_shape = wanted_shape.strip()

    # check if shape is valid
    shape_choice = string_check(wanted_shape, valid_shape)

    if shape_choice == "invalid choice":
        print(" Please enter a valid Shape Option ")

    # add shape to list...
    shape_row.append(shape_choice)

    # check that shape is not the exit code before adding
    if shape_choice != "end" and shape_choice != "invalid choice":
        shape_input.append(shape_row)

# Main Routine
# valid options for yes / no question
insert_shape = get_shape()
# Show shape order
print()
if len(insert_shape) == 0:
    print("Shape input: None")
print("Shape:")
    #print(item)
print(insert_shape)

