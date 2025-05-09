from scipy.optimize import linprog

# Coeficientes de la función objetivo (maximizar 8x + 10y)
c = [-8, -10]  # Negativos porque linprog minimiza por defecto

# Coeficientes de las restricciones
A = [
    [2, 3],    # Restricción de tela: 2x + 3y <= 600
    [2, 1],    # Restricción de horas: 2x + y <= 500
    [0, 4]     # Restricción de esquineros: 4y <= 600
]

# Lados derechos de las restricciones
b = [600, 500, 600]

# Restricciones de no negatividad
x_bounds = (0, None)  # x >= 0
y_bounds = (0, None)  # y >= 0

# Resolver el problema con linprog
result = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds], method="highs")

# Variables óptimas y valor máximo de la función objetivo
if result.success:
    optimal_x, optimal_y = result.x
    optimal_profit = -result.fun
    print(f"Número de manteles redondos (x): {optimal_x}")
    print(f"Número de manteles rectangulares (y): {optimal_y}")
    print(f"Ganancia máxima: {optimal_profit}")
else:
    print("No se pudo encontrar una solución óptima.")