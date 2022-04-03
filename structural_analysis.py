from math import *
import pandas as pd
forces = []
angle = []
coordinates = []
"""This is a command line program of structural analysis"""

def force_analysis(mag, orientation):
    H = 0
    V = 0
    print(mag, orientation)
    for F, a in mag, orientation:
        V += F*sin(a)
        H += F*cos(a)
        print(V,H)
    
    return (round(H,2), round(V,2))

def torque_analysis(mag, pos):
    pass


nf = int(input("Enter number of forces: "))

for i in range(0,nf):
    F = int(input(f"Enter the magnitude of F{i+1}: "))
    forces.append(F)
    position = tuple(input("Enter the cartesian coordinates of point of action: (x,y)").split(","))
    coordinates.append(position)
    orientation = (float(input("Enter the angle with horizontal(counter clockwise): ")) * (pi/180))
    angle.append(orientation)


data = pd.DataFrame([forces,angle,coordinates], ["magnitude", "angle", "coordinates"])
print(data)
print(force_analysis(forces, angle))

