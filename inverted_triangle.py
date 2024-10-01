# Inverted triangle

# Define the function to generate the triangle
def inverted_triangle(height_value):
    for height_value in range(height_n, 0, -1):
        print("*" * height_value)

# User input or the height of the triangle
try:
    height_n = int(input("Enter the height of the triangle: "))
    inverted_triangle(height_n)
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()
except:
    print("Something went wrong. Exiting the program.")
    exit()
