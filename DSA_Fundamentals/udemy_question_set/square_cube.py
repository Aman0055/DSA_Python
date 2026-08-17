# WAP to get a number from 1 to 10 and get their square and cube and then add their value
# Wap a prgram to get number from 10 to 1 with the difference of 4 and get their square and cube

# WAP to get a number from 1 to 10 and get their square and cube and then add their value
# WAP a program to get number from 10 to 1 with the difference of 4 and get their square and cube

def square_cube_ascending():
    print("Squares and Cubes from 1 to 10:")
    for i in range(1, 11):
        square = i ** 2
        cube = i ** 3
        total = square + cube
        print(f"Number: {i}, Square: {square}, Cube: {cube}, Total: {total}")


def square_cube_descending():
    print("\nSquares and Cubes from 10 to 1 (step -4):")
    for i in range(10, 0, -4):
        square = i ** 2
        cube = i ** 3
        total = square + cube
        print(f"Number: {i}, Square: {square}, Cube: {cube}, Total: {total}")

def generate_numbers():
    print("\nGenerating numbers from 1 to 100 with def of 4:")
    for i in range(1, 101 , 4):
        print(f"Numbers generated :{i}")

def main():
    square_cube_ascending()
    square_cube_descending()
    generate_numbers()


main()
                      
        