import os,sys
import numpy as np

def main(argv):

    f = lambda x : 1.0*np.sin(1*0.7*x) - 2.0*np.cos(1*0.7*x) + 1.0*np.sin(2*0.7*x) + 2.0*np.cos(2*0.7*x) \
        - 3.0*np.sin(3.0*0.7*x) + 4.0*np.cos(3.0*0.7*x) + np.random.normal(scale=2.0,size = len(x))

    # Generate f dataset
    x = np.arange(0,10.01,0.05)
    y = f(x)

    write_data('data.txt',x,y)

    return

def write_data(file_name,x,y):
    with open(file_name,'w') as f:
        f.write("{:<20s} {:<20s}\n".format("t-data","y-data"))        
        for i in range(len(x)):
            f.write("{:< 20.6f} {:< 20.6f}\n".format(x[i],y[i])) 


if __name__ == "__main__":
    main(sys.argv[1:])
