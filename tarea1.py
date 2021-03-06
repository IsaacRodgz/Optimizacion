import numpy as np
import matplotlib.pyplot as plt

def f1(x1, x2):

    return x1**2 - x2**2

def f2(x1, x2):

    return 2*x1*x2

def main():

    # Intervalo donde se hara la gráfica

    x = np.linspace(-9, 9, 400)
    y = np.linspace(-5, 5, 400)
    x, y = np.meshgrid(x, y)

    # Creacion de la grafica

    ax = plt.subplot(111)

    # Se dibujan los ejes x, y

    ax.axhline(0, alpha=.1)
    ax.axvline(0, alpha=.1)

    # Se ajustan los limites de los ejes

    ax.set_xlim([-9, 9])
    ax.set_ylim([-5, 5])

    # Se grafica funcion f1(x1, x2) = x1**2 - x2**2

    ax.contour(x, y, f2(x, y), [16], colors='b', alpha = 0.7)

    # Se grafica funcion f2(x1, x2) = 2*x1*x2

    ax.contour(x, y, f1(x, y), [12], colors='g', alpha = 0.7)

    # Se grafican puntos de interseccion entre las curvas de nivel

    ax.plot(np.array([-4, 4]), np.array([-2, 2]), '.', color = 'r')

    # Se grafican las leyendas, titulo y nombre de los ejes

    ax.legend(['${x_1}^2 - {x_2}^2 = 16$', '$2x_1x_2 = 12$', 'Intersection points'])
    
    ax.set_xlabel('$x_1$')
    
    ax.set_ylabel('$x_2$')
    
    ax.set_title('Level sets')

    # Se muestra la grafica

    plt.show()

if __name__ == '__main__':
    main()
