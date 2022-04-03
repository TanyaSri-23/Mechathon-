from math import *
import pandas as pd
forces = []
"""This is a command line program of structural analysis"""

def force_analysis(F):
    H = []
    V = []
    for force in F:
        V.append(round(force[0]*sin(force[2]),2))
        H.append(round(force[0]*cos(force[2]),2))
    return (round(sum(H),2), round(sum(V),2))

def torque_analysis(mag, pos):
    pass


nf = int(input("Enter number of forces: "))

for i in range(0,nf):
    force=[]
    F = int(input(f"Enter the magnitude of F{i+1}: "))
    force.append(F)
    position = tuple(input("Enter the cartesian coordinates of point of action: (x,y)").split(","))
    force.append(position)
    orientation = round((float(input("Enter the angle with horizontal(counter clockwise): "))*pi) / 180, 2)
    force.append(orientation)
    forces.append(force)


for i in forces:
    data = pd.DataFrame([i[0],i[1],i[2]], ["magnitude", "coordinates", "orientation"])

print(data)
print(force_analysis(forces))

