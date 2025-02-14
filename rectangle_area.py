def calculate_area(length, width): 
    return length * width 
def calculate_perimeter(length, width):
    return 2 * (length + width)
length = int(input("enter the length: "))
width = int(input("enter the width: "))
area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)
print(f"The area of the rectangle is: {area}") # From Maya's branch
print(f"The perimeter of the rectangle is: {perimeter}") # From Maya's branch