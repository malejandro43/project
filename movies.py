movies = [
    ["The Shawshank Redemption", 1994, "Frank Darabont"],
    ["The Godfather", 1972, "Francis Ford Coppola"],
    ["The Dark Knight", 2008, "Christopher Nolan"],
    ["12 Angry Men", 1957, "Sidney Lumet"],
    ["Schindler's List", 1993, "Steven Spielberg"],
    ["The Lord of the Rings: The Return of the King", 2003, "Peter Jackson"]
]

movie_to_change = "The Lord of the Rings: The Return of the King"
new_movie = "The Lord of the Rings: The Fellowship of the Ring"
new_year = 2001

for movie in movies:
    if movie[0]==movie_to_change: # establece una condición aquí
        movie[0]=new_movie
        movie[1]=new_year# sustituye el nombre de la película si la condición devuelve True
        # sustituye el año de estreno si la condición devuelve True

# no modifiques el código de abajo, ya que imprime el resultado
for movie in movies:
    print(movie)




employees = [['Alice', 75000, 'Desarrollador', 'Júnior'],
						 ['Bob', 68000, 'Diseñador', 'Semi sénior'],
						 ['Charlie', 78000, 'Desarrollador', 'Júnior'],
						 ['David', 85000, 'Gerente', 'Sénior'],
						 ['Eve', 80000, 'Desarrollador', 'Semi sénior']]
							
# Define el nombre que actualizarás, el incremento de salario y el umbral especificado de salario para el cambio de antigüedad
name_to_update = "Alice"
salary_increase = 10000
salary_threshold = 80000
new_seniority = "Sénior"

## TU CÓDIGO ##
for variable in employees:
    if variable[0]=="Alice":
        variable[1]+=10000
for variable in employees:
    if variable[1]>80000:
        variable[3]=new_seniority

print(employees)



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

movies_filtered = [] # lista vacía para almacenar el resultado

for variable in movies_info:
     if variable[1]=='USA':
         movies_filtered.append(variable)

# escribe tu código aquí
# muestra el resultado
for movie in movies_filtered: 
    print(movie)
    
    



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