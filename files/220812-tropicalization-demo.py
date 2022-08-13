# initialization
import matplotlib.pyplot as plt
ax = plt.axes(projection='3d')
xdata, ydata, zdata = [], [], []

# plane region x,y>=0, z=0
for i in range(0,16):
    for j in range(0,16):
        xdata.append(i); ydata.append(j); zdata.append(0);

# plane region y>=0, z>0, x=0
for i in range(0,16):
    for j in range(1,16):
        xdata.append(0); ydata.append(i); zdata.append(j);

# plane region x,z>0, y=0
for i in range(1,16):
    for j in range(1,16):
        xdata.append(j); ydata.append(0); zdata.append(i);

# plane region x=y<0, z>=x
for i in range(1,16):
    for j in range(-i,16):
        xdata.append(-i); ydata.append(-i); zdata.append(j);

# plane region y=z<0, x>=y, and x=z<0, y>=z
for i in range(1,16):
    for j in range(-i+1,16):
        xdata.append(j); ydata.append(-i); zdata.append(-i);
        xdata.append(-i); ydata.append(j); zdata.append(-i);

# plot the data; load the tropicalization picture
ax.scatter3D(xdata,ydata,zdata)

# show
plt.show()
