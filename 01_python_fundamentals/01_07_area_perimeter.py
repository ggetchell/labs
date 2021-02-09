'''

Write the necessary code to display the area and perimeter of a rectangle that has a width of 2.4 and a height of 6.4.

'''

width = float(input("Enter the width: "))
height = float(input("Enter the height: "))
area = width * height
perimeter = 2 * (width + height)
print("Area : {0:.2f}".format(area))
print("Perimeter : {:.2f}".format (perimeter))

