# Lista anidada de pedidos: [precio, cantidad, descuento]
orders = [
    [199.99, 2, 0.10],  # 10% de descuento
    [349.99, 1, 0.05],  # 5% de descuento
    [129.99, 3, 0.00],  # Sin descuento
    [499.99, 1, 0.20],  # 20% de descuento
    [249.99, 4, 0.15],  # 15% de descuento
]
# Inicializa las variables
total_revenue = 0
highest_order_value = 0
descuento=0.0
prueba=[]

# Recorre los pedidos
for variable in orders:
    descuento=variable[0]*variable[1]-variable[0]*variable[1]*variable[2]
    total_revenue +=descuento
    prueba=variable[0]*variable[1]-variable[0]*variable[1]*variable[2]
    
   #highest_order_value=max()
### AQUÍ VA TU CÓDIGO ###
highest_order_value = prueba
print("Ingresos totales después de descuentos y tasas:", total_revenue) # Salida: Ingresos totales después de descuentos y tasas: 2332.4005
print("Valor de pedido único más alto:", highest_order_value)  # Salida: Valor de pedido único más alto: 849.966

    