movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

usa_movies_filtered = [] # lista vacía para almacenar el resultado
for variable in movies_info:
    if variable[1]=='USA' and variable[2]>1990:
        usa_movies_filtered.append(variable)


# escribe tu código aquí
for x in usa_movies_filtered:
    x.pop(1)

# muestra el resultado
print(movies_info )



usa_movies_filtered = []  # Lista vacía para almacenar el resultado
for variable in movies_info:
    if variable[1] == 'USA' and variable[2] > 1990:
        usa_movies_filtered.append([variable[0], variable[2], variable[3], variable[4], variable[5]])  # Excluir el país

# Mostrar el resultado
print(usa_movies_filtered)


movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

# crear una lista vacía llamada movies_filtered
movies_filtered=[]
# escribe tu código aquí

# no modifiques el código de abajo ya que imprime el resultado final
for movie in movies_info:
    if movie[2]==1994 or movie[5]<8.5:
       movies_filtered+=movie
       #print(movie) 
print(movies_filtered)  



movies_info = [
    ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
    ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730],
    ['The Dark Knight', 'USA', 2008, 'fantasy, action, thriller', 152, 8.499],
    ["Schindler's List", 'USA', 1993, 'drama', 195, 8.818],
    ['The Lord of the Rings: The Return of the King', 'New Zealand', 2003, 'fantasy, adventure, drama', 201, 8.625],
    ['Pulp Fiction', 'USA', 1994, 'thriller, comedy, crime', 154, 8.619],
    ['The Good, the Bad and the Ugly', 'Italy', 1966, 'western', 178, 8.521],
    ['Fight Club', 'USA', 1999, 'thriller, drama, crime', 139, 8.644],
    ['Harakiri', 'Japan', 1962, 'drama, action, history', 133, 8.106],
    ['Good Will Hunting', 'USA', 1997, 'drama, romance', 126, 8.077]
]

# Crear una lista vacía llamada movies_filtered
movies_filtered = []

# Escribir el código para filtrar
for movie in movies_info:
    if movie[2] == 1994 or movie[5] < 8.5:
        movies_filtered.append(movie)

# Imprimir cada sublista en una nueva línea
for movie in movies_filtered:
    print(movie)
    
    
    
    
financial_info = {
    'American Express': 93.23,
    'Boeing': 178.44,
    'Coca-Cola': 45.15,
    'Walt Disney': 119.34,
    'Nike': 97.99,
    'JPMorgan':96.27,
    'Walmart': 130.68 
}

nike_price =financial_info.get('Nike') # escribe tu código aquí
print(nike_price)



products = {
    'Product_A': {'price': 10, 'quantity': 2, 'discount': 0.1},
    'Product_B': {'price': 20, 'quantity': 1, 'discount': 0.05},
    'Product_C': {'price': 15, 'quantity': 5, 'discount': 0.2},
}

ingreso_totalA=products['Product_A']['price']*products['Product_A']['quantity']-(products['Product_A']['price']*products['Product_A']['quantity'])*.1

ingreso_totalB=products['Product_B']['price']*products['Product_B']['quantity']-(products['Product_B']['price']*products['Product_B']['quantity'])*.05
ingreso_totalC=products['Product_C']['price']*products['Product_C']['quantity']-(products['Product_C']['price']*products['Product_C']['quantity'])*.2
total=ingreso_totalA+ingreso_totalB+ingreso_totalC

valor_mas_alto = max(products.values())

print(total, valor_mas_alto)