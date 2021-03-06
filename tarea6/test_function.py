import numpy as np
import matplotlib.pyplot as plt
from GC import GC
from Function import Function


def run(point_type, dim, lmbd, function):

    # Define function to smooth/denoise
    x = y = np.linspace(-1, 1, dim)
    x , y = np.meshgrid(x, y)
    g = x**2+y**2+0.1*np.random.randn(*x.shape)
    g = (g-g.min())/(g.max()-g.min())
    f = Function(g, lmbd)

    # Initial point
    if point_type == "const":
        x0 = np.ones(dim*dim)
    elif point_type == "rand":
        x0 = np.random.rand(dim*dim)
    else:
        print("\n Error, invalid type of point")
        quit()

    # Estimate minimum point through optimization method chosen
    alg = GC()

    xs, fs, gs = alg.iterate(x0, f)

    # Print point x found
    #print("\nf(x) =  ", f.eval(xs[-1]))

    # Plot f(x) through iterations
    plt.plot(np.array(range(len(fs))), fs)
    plt.legend(['f(x)'], loc = 'best')
    plt.xlabel("iteration")
    plt.show()

    # Plot ||gradient(x)|| through iterations
    plt.plot(np.array(range(len(gs))), gs)
    plt.legend(['grad(x)'], loc = 'best')
    plt.xlabel("iteration")
    plt.show()

    plt.imshow(g)
    plt.title("True matrix (g)")
    plt.show()

    plt.imshow(xs[-1].reshape((dim,dim)))
    plt.title("Solution found (x*)")
    plt.show()
