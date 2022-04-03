from math import *
import pandas as pd
forces = []
"""This is a command line program of structural analysis"""

def force_analysis(F):
    """this function performs force analysis by static equilibrium condition"""
    H = []
    V = []
    for force in F:
        V.append(round(force[0]*sin(force[2]),2))
        H.append(round(force[0]*cos(force[2]),2))
    return (round(sum(H),2), round(sum(V),2))

# def torque_analysis(F):
#     """this function performs moment analysis by static equilibrium condition"""
#     V = []
#     for force in F:
#         fsin = V.append(round(force[0]*sin(force[2]),2))
#         distance = force[1][0]
#     M = round(fsin * distance, 2)

#     return M


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


Fh = force_analysis(forces)[0]
Fv = force_analysis(forces)[1]

balancing_force = round(sqrt(Fh**2 + Fv**2),2)
direction = round((atan(Fv/Fh) * (180/pi)),2)

print(f"The balancing force will be {balancing_force} at {direction} degree counter clockwise.")
