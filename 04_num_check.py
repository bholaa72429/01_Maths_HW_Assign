# Function Goes Here

# checks that input is a float or an integer which is more zero.
# Has custom error messages for int/float
def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            # if response is less or = to 0
            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

# MAIN ROUTINE
get_circle = num_check("Please enter Radius of the Circle. ",
                    "Please enter an integer (whole number) which is more than 0\n",
                    float)


print("Radius: {}".format(get_circle))