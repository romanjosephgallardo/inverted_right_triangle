# Inverted triangle

# Define the function to generate the triangle
def inverted_triangle(height_value):
    for height_value in range(height_n, 0, -1):
        print("*" * height_value)

# User input or the height of the triangle
height_n = int(input("Enter the height of the triangle: "))
inverted_triangle(height_n)
