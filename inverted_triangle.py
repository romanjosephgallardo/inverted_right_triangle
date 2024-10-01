# Inverted triangle

# User input or the height of the triangle
height_n = int(input("Enter the height of the triangle: "))

# Generate and print the triangle
for height_value in range(height_n, 0, -1):
    print("*" * height_value)