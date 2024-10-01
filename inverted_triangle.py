'''
Generate an inverted right triangle of height n.

Sample output
Enter the height of the triangle: 6
******
*****
****
***
**
*
'''

#pseudocode
# Get the height of the triangle
height_n = int(input("Enter the height of the triangle: "))

# Generate the triangle
for height_value in range(height_n, 0, -1):
    print("*" * height_value)