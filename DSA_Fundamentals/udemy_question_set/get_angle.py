# Wap to get a angle from the user and finds its sin and cos value in radian ::

import math 

def solution():
    angle = float(input("Enter the angle in degrees:"))
    angle_in_radians = math.radians(angle)
    sin_value = math.sin(angle_in_radians)
    cos_value = math.cos(angle_in_radians)
    print(f"Sin value of {angle} degree is : {sin_value}")
    print(f"Cos value of {angle} degree is : {cos_value}")


    print("After onwards , reverse the program and get angle radian to angle")
    rev_sin_value = math.degrees(sin_value)
    rev_cos_value = math.degrees(cos_value)
    print(f"Reversed Sin value is : {rev_sin_value}")
    print(f"Reversed Cos value is : {rev_cos_value}")

solution()