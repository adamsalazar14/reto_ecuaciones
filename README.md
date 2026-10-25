# Solución de Ecuación Diferencial: Método de Euler vs Analítica

Este repositorio contiene un script en Python que resuelve una ecuación diferencial separable utilizando dos enfoques: el método analítico (separación de variables) y el método numérico de Euler.

## El Problema

Se ha seleccionado la siguiente ecuación diferencial ordinaria (EDO) de primer orden con valor inicial:

$$ \frac{dy}{dt} = y, \quad y(0) = 1 $$

El objetivo es encontrar la solución en el intervalo $t \in [0, 1]$ utilizando un paso de integración $h = 0.2$.

### 1. Solución Analítica (Separación de Variables)
Podemos reescribir y separar las variables de la ecuación:

$$ \frac{dy}{y} = dt $$

Integrando ambos lados:

$$ \int \frac{1}{y} dy = \int dt $$
$$ \ln|y| = t + C $$
$$ y = e^{t+C} = K e^t $$

Aplicando la condición inicial $y(0) = 1$:
$$ 1 = K e^0 \implies K = 1 $$

Por lo tanto, la solución exacta es:
$$ y(t) = e^t $$

### 2. Método Numérico de Euler
El método de Euler aproxima la solución utilizando la fórmula iterativa:

$$ y_{n+1} = y_n + h \cdot f(t_n, y_n) $$

Sabiendo que $f(t, y) = y$ y el tamaño de paso es $h = 0.2$, las primeras iteraciones son:
- **Iteración 0:** $t_0 = 0$, $y_0 = 1$
- **Iteración 1:** $y_1 = 1 + 0.2(1) = 1.2$ (para $t_1 = 0.2$)
- **Iteración 2:** $y_2 = 1.2 + 0.2(1.2) = 1.44$ (para $t_2 = 0.4$)
- Y así sucesivamente hasta llegar a $t = 1.0$.

## Requisitos

Para ejecutar el código necesitarás instalar `numpy` y `matplotlib`. Puedes hacerlo ejecutando:

```bash
pip install -r requirements.txt