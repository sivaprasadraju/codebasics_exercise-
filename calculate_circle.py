import numpy as np
import math
def circle_calc(circ_rad):
    diameter = 2*circ_rad
    circumference = 2 * math.pi * circ_rad
    area = math.pi * circ_rad**2
    return area, circumference, diameter

def main():
    print("Please provide the raidus of the circle: ")
    radius = float(input())
    area, circumference, diameter = circle_calc(radius)

    print("area of circle: ", round(area,2))
    print("circumference of circle: ", round(circumference,2))
    print("diameter of circle: ", round(diameter,2))






if __name__ == '__main__':
    main()