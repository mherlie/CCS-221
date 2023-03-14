import numpy as np
import matplotlib.pyplot as plt

_arr_2d = np.array([[1, 0, 1]
                   , [0, 0, 0]
                   , [1, 0, 1]])

def change(x, y, color):
   
    
    fig = plt.figure()
    for i in range(len(_arr_2d)):
        for j in range(len(_arr_2d)):
            _arr_2d[x][y] = color

    img = plt.imshow(_arr_2d, cmap='plasma', interpolation='none')
    img.set_clim([0, 100])
    plt.colorbar()
    
    return fig

def main():
    change(2, 1, 85)
    
if __name__=="__main__":
    main()
