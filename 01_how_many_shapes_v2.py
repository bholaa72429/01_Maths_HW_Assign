# Integer checking function below
def intcheck(question,low=1,high=10):
    valid = False
    error = "Whoops! Please enter an integer "
    while not valid:
        try:
            response = int(input(question))

            if low <= response <= high:
                return response
            else:
                print("Oh! Please enter a number between 1 and 10. ")
                print()

        except ValueError:
            print(error)

rounds = intcheck("How many shapes would you like to calculate the area and perimeter of? ", 1, 10)

