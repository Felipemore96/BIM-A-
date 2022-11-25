# BIM A+3: Parametric Modelling in BIM
# Felipe Moreira
# Programming Assignement #3
# Topic 2: Fundamentals of programming, Python program to calculate geometrical characteristics for any polygon

print("The Python program calculates different geometrical characteristics for a polygon")
print()

# Print message to obtain the amount of plygon poings
n = int(input("Enter number of polygon points: "))

# Create empty lists for coordinates of the points
xs = []
ys = []

# Print message to obtain coordinates for all points
print("Enter polygon points:")
for i in range(0,n):
    x = float(input(f"xs[{i+1}]: "))
    y = float(input(f"ys[{i+1}]: "))
    xs.append(x)
    ys.append(y)
print()

# Print table of points
print(f"{'X':>10} {'Y':>10}")
print("-" * 26)  
for i in range(n):
    print(i+1, ":", f"{xs[i]:>7} {ys[i]:>10}")

# Create lists to use in calculations
a1 = []
sx1 = []
sy1 = []
ix1 = []
iy1 = []
ixy1 = []

# Create loops for requested formulas and put all results in the lists created
for i in range(0,n):
    a2 = (xs[i]+xs[i-1])*(ys[i]-ys[i-1])
    sx2 = (xs[i]-xs[i-1])*((ys[i]**2+ys[i-1]*ys[i]+ys[i-1]**2))
    sy2 = (ys[i]-ys[i-1])*((xs[i]**2+xs[i-1]*xs[i]+xs[i-1]**2))
    ix2 = (xs[i]-xs[i-1])*((ys[i]**3+(ys[i-1]*ys[i]**2)+(ys[i]*ys[i-1]**2)+ys[i-1]**3))
    iy2 = (ys[i]-ys[i-1])*((xs[i]**3+(xs[i-1]*xs[i]**2)+(xs[i]*xs[i-1]**2)+xs[i-1]**3))
    ixy2 = (ys[i]-ys[i-1])*(ys[i]*(3*xs[i]**2+2*xs[i-1]*xs[i]+xs[i-1]**2)+ys[i-1]*(3*xs[i-1]**2+2*xs[i-1]*xs[i]+xs[i]**2))
    a1.append(a2)
    sx1.append(sx2)
    sy1.append(sy2)
    ix1.append(ix2)
    iy1.append(iy2)
    ixy1.append(ixy2)

# Define all requested geometrical characteristics   
A = (1/2)*(sum(a1))
Sx = (-1/6)*sum(sx1)
Sy = (1/6)*sum(sy1)
Ix = (-1/12)*sum(ix1)
Iy = (1/12)*sum(iy1)
Ixy = (-1/24)*sum(ixy1)
xT = Sy/A
yT = Sx/A
IxT = Ix-yT**2*A
IyT = Iy-xT**2*A
IxyT = Ixy+xT*yT*A

#Print all final results of geometrical characteristics
print()
print("Geometric characteristics:")
print()
print(f"A    =  {A:.2f}")
print(f"Sx   =  {Sx:.2f}")
print(f"Sy   =  {Sy:.2f}")
print(f"Ix   =  {Ix:.2f}")
print(f"Iy   =  {Iy:.2f}")
print(f"Ixy  =  {Ixy:.2f}")
print(f"xT   =  {xT:.2f}")
print(f"yT   =  {yT:.2f}")
print(f"IxT  =  {IxT:.2f}")
print(f"IyT  =  {IyT:.2f}")
print(f"IxyT =  {IxyT:.2f}")
print()

print("End.")