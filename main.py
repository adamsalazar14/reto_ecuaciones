import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    """Ecuación diferencial dy/dt = f(t, y) = y"""
    return y

def solucion_exacta(t):
    """Solución analítica y(t) = e^t"""
    return np.exp(t)

def main():
    # Parámetros iniciales
    t0 = 0.0
    tf = 1.0
    h = 0.2
    y0 = 1.0

    # Crear el vector de tiempo
    t = np.arange(t0, tf + h, h)
    n = len(t)

    # Arreglos para almacenar los resultados
    y_euler = np.zeros(n)
    y_euler[0] = y0

    # Arreglo de la solución exacta
    y_exact = solucion_exacta(t)

    # Aplicar el método de Euler
    for i in range(n - 1):
        y_euler[i + 1] = y_euler[i] + h * f(t[i], y_euler[i])

    # Imprimir la tabla de resultados
    print(f"{'t':<5} | {'Euler':<10} | {'Exacta':<10} | {'Error Absoluto':<15}")
    print("-" * 50)
    for i in range(n):
        error = abs(y_exact[i] - y_euler[i])
        print(f"{t[i]:.1f}   | {y_euler[i]:<10.5f} | {y_exact[i]:<10.5f} | {error:<15.5f}")

    # Visualización (Gráfica)
    plt.figure(figsize=(8, 5))
    plt.plot(t, y_exact, label='Solución Exacta $y = e^t$', color='blue', linewidth=2)
    plt.plot(t, y_euler, label='Método de Euler', color='red', marker='o', linestyle='dashed')
    
    plt.title('Comparación: Método de Euler vs Solución Exacta')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()