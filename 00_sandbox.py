# adding to a string....

# get input

# Trial # 1
# given_data = ""
# for item in range(0, 3):
#     side = int(input("Length? "))
#     given_data += "side length: " + str(side)
#
# print("given data: ", given_data)

units = "cm"
side = input("side length: ")
base = input("base: ")

given_data = "side length: {} {} | base: {} {}".format(side, units, base, units)

print(given_data)