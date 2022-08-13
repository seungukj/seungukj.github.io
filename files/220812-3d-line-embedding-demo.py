# initialization
import matplotlib.pyplot as plt

# options
while(True):
    option = input("""Choose option:

1. Show V(trop(min(w3, w1, v(b)))) and V(trop(min(w2, w1, v(a)))).
2. Show the intersection of two.

>> """)
    if(not((option == '1') or (option == '2'))): print("bad input")
    else: break

ax = plt.axes(projection='3d')
if(option == '1'):
    DATA = [[[],[],[]],[[],[],[]]]
    
    # DATA[0] = trop(min(w3, w1, v(b)))
    # DATA[1] = trop(min(w2, w1, v(a)))
    # Set v(b) = 0, v(a) = 5
    
    def data_append(dataid, w1, w2, w3):
        DATA[dataid][0].append(w1)
        DATA[dataid][1].append(w2)
        DATA[dataid][2].append(w3)
        return
    
    # DATA[0]
    for k in range(-15,16): # w2 values
        data_append(0, 0, k, 0) # v(b) = 0
        for i in range(1,16):
            data_append(0, i, k, 0)
            data_append(0, 0, k, i)
            data_append(0,-i, k,-i)
    
    # DATA[1]
    for k in range(-15,16): # w3 values
        data_append(1, 5, 5, k) # v(a) = 5
        for i in range(6,16):
            data_append(1, i, 5, k)
            data_append(1, 5, i, k)
        for i in range(-15,5):
            data_append(1, i, i, k)
    
    # plot the data; load the tropicalization picture
    ax.scatter3D(*DATA[0], marker='*')
    ax.scatter3D(*DATA[1], marker='*')
    
    # show
    plt.show()
else:
    # intersection; trop(line)
    DATA = [[],[],[]]
    def data_append(w1, w2, w3):
        DATA[0].append(w1)
        DATA[1].append(w2)
        DATA[2].append(w3)
        return
    
    for i in range(-15,0):
        data_append(i,i,i)
    for i in range(0,16):
        data_append(0,0,i)
    for i in range(1,6):
        data_append(i,i,0)
    for i in range(6,16):
        data_append(i,5,0)
        data_append(5,i,0)

    # plot the data
    ax.scatter3D(*DATA)

    # show
    plt.show()
