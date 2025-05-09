message = "yo tengo"  
edad=40
message2="años"
print(message, edad, message2)  
edad=39
test=2
resultado=edad/test
print("hoy tengo",type(resultado))
print('Let\'s learn about strings!')
shopping_list = """Mi lista de compras:
2 cartones de leche, 
cereal, 
huevos, 
pan"""
print(shopping_list)
print(len(shopping_list))
sonnet = "Que la ruda mano del invierno no deshaga,\nEn ti el verano, antes tú debes ser destilado:\nEndulza algún pomo, en algún lugar atesórate\nCon el tesoro de la belleza antes que ella a sí se mate.\nNo es usura prohibida hacer pagar,\nA quien feliz paga por lo que debe;\nEso sería para ti engendrar otro tú,\nO diez veces más feliz, sea un diez por uno;\nDiez veces más feliz serás de lo que eres,\nSi diez de ti diez veces te figuran:\nPues, ¿qué podría hacer la muerte si partes,\nDejándote vivo, con descendencia?\nNo seas egoísta, tu belleza es mucha para conquista\nDe la muerte, que a los gusanos tus herederos haría."

print(sonnet)
#print() # imprime una línea en blanco
print(len(sonnet))
phrase = 'Olivia loves her little yellow duckling' 
longitud=len(phrase)-1
print(phrase[longitud])# muestra aquí el último carácter usando la función len() y la indexación positiva
longitud_negativa=-1* len(phrase)
print(phrase[longitud_negativa])
string = 'En cierto modo, programar es como pintar. Comienzas con un lienzo en blanco y algunas materias primas básicas. Usas una combinación de ciencia, arte y artesanía para determinar qué hacer con ellos' 
x=string[3]
print(x)
print(string[-4])
city = 'Rio de Janeiro, Brasil'

print(city[4:1000])
print(city[-15:500])
print(city[4:0])
name = 'Victoria'
age = 23
height = 157

message = f"{name} tiene {age} años y mide {height} cm"
print(message)
name = 'Victoria'
age = 23

name_surname = 'Joseph Kobe Steeler'
months = 5

message =f"Estimado {name_surname}, ha gastado mas de 10,000 en el mes {months}. Su devolucion de impuestos se inicia el mes que viene. {months+1}" # escribe tu código aquí
print(message)

message = f"El próximo año, {name} tendrá {age + 1} años"
print(message)
name = 'Victoria'
age = 23
height = 157

message = "{n} tiene {a} años y mide {h} cm".format(h=height, n=name, a=age)
print(message)
name = 'Clint Eastwood'
print(name[6:9])

# Una lista vacía
my_list = []

# Una lista de enteros
numbers = [1, 2, 3, 4, 5]

# Una lista de strings
fruits = ['manzana', 'manzana', 'banana', 'cereza']

# Una lista de tipos de datos mezclados
mixed = [1, 'apple', 3.14, True]
print(len(fruits), type(fruits))
string=fruits[-1]
print(string)
print('Contenido de la variable my_list:',my_list)
print('Contenido de la variable numbers:',numbers)
print('Contenido de la variable fruits:',fruits)
print('Contenido de la variable mixed:',mixed)
my_list = [1, 2, 3]
my_list.insert(1, [1.2, 1.5])  # Inserta 1.2 y 1.5 en el índice 1
print(my_list) 

clients = []
client_info = [32456, 'Jack Wilson', 32, 150000, 'Healthcare']
clients.insert(0,[client_info])
# escribe tu código aquí

print(clients)

shawshank_movie = ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111]
shawshank_movie.append("Frank Darabont") # escribe tu código aquí
print(shawshank_movie)
titanic_movie = ['Titanic', 'USA', 1997, 'James Camron', 'drama', 194]
titanic_movie.remove('James Camron')
# elimina el nombre del director de la lista
print(titanic_movie)

godfather_movie = ['The Godfather', 'USA', 1972]
# añade los nombres del director y del compositor al final de la lista
sgodfather_movie2=['Francis Ford Coppola','Nino Rota']
godfather_movie.extend(sgodfather_movie2)#tu código)
print(godfather_movie)

shawshank_movie = ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111]
shawshank_movie.append("Frank Darabont") # escribe tu código aquí
print(shawshank_movie)

titanic_movie = ['Titanic', 'USA', 1997, 'James Camron', 'drama', 194]
titanic_movie.pop(3)
# elimina el nombre del director de la lista
print(titanic_movie)

titanic_movie = ['Titanic', 'USA', 1997, 'drama', 194]
titanic_movie.insert(3, 'James Cameron')
# añade el nombre del director antes del género de la película:
print(titanic_movie)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]
print(years)

years.sort()
print(years)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]

years.sort(reverse=True)
print(years)

years = [1994, 1972, 2008, 1993, 2003, 1994, 1966, 1999, 1962, 1997]

years_sorted = sorted(years)# devuelve la lista ordenada a otra lista

print(years_sorted)

movies_duration = [142, 175, 152, 195, 201, 154, 178, 139]

movies_duration_sorted = sorted(movies_duration, reverse=True)
print(movies_duration_sorted)

movies_info = [
            ['The Shawshank Redemption', 'USA', 1994, 'drama', 142, 9.111],
            ['The Godfather', 'USA', 1972, 'drama, crime', 175, 8.730]
]#almacenes como matrices

print(movies_info[0]) # recuperamos la primera fila
print(movies_info[-1]) # recuperamos la última fila
print(movies_info)


example = [10,20,30,['a','b','c'],50]
print(example[3][1]) # coordenadas


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
print(movies_info[9][1])
print(movies_info[5][2])
print(movies_info[1][-1])
# muestra aquí el país de producción de *Good Will Hunting*
# muestra aquí el año de estreno de Pulp Fiction
# muestra aquí la valoración de The Godfather

phrase = 'dividir o no dividir'
words = phrase.split() # divide el string
print(words)


text = 'Esta es una oración. Esta es otra oración.'
sentences = text.split('.') # Delimitador específico para dividir cambia el . por ,
print(sentences)

words = ['Mi', 'película', 'favorita', 'es', 'The', 'Graduate.']
phrase = ' '.join(words) # forma un string a partir de los elementos, separados por espacios
print(phrase)# cambia las , por el espacio

movie_info = ['Fight Club', 1999, ['thriller', 'drama', 'crime'], 139, 8.644]
print(movie_info.__len__)

name_surname = 'Joseph_Kobe_Steeler '
name_surname = name_surname.split('_')
name_surname=' '.join(name_surname)
print(name_surname)

name_surname = 'Joseph Kobe Steeler'
name_split = name_surname.split() # escribe tu código aquí

print(name_split)

citizen_CA = [-465, 156, -567, -6051, 8607]

total_amount =citizen_CA[0]+citizen_CA[1]+citizen_CA[2]+citizen_CA[3]+citizen_CA[4] 
print(total_amount)

citizen_CA = [-465, 156, -567, -6051, 8607]

total_amount =citizen_CA[0]+citizen_CA[1]+citizen_CA[2]+citizen_CA[3]+citizen_CA[4] # escribe tu código aquí
citizen_CA.sort()
max_tax_due = citizen_CA[0] # escribe tu código aquí
max_rebate = citizen_CA[4]# escribe tu código aquí

print(total_amount)
print(max_tax_due)
print(max_rebate)

client_info = [32456, 'Jack Wilson', 32, 150000, 'Healthcare']# escribe tu código aquí
print(client_info)


clients = []
client_info = [32456, 'Jack Wilson', 32, 150000, 'Healthcare']
clients.append[1, client_info]
# escribe tu código aquí

print(clients)

clients = [
    [32456, 'Jack Wilson', 32, 150000, 'Healthcare'],
    [34591, 'Nina Brown', 45, 250000, 'Telecom']
]

client_income =clients[1][3] # escribe tu código aquí
print(client_income)




clients = [
    [32456, 'Jack Wilson', 32, 150000, 'Healthcare'],
    [34591, 'Nina Brown', 45, 250000, 'Telecom'],
    [37512, 'Alex Smith', 39, 210000, 'IT'],
    [39591, 'Brian Perez', 29, 340000, 'Transportatiion']
]

clients.pop(3)# escribe tu código aquí

print(clients)

ages = [32, 45, 39, 29, 25, 32]

ages.sort(reverse=True)
# escribe tu código aquí

print(ages)

names = 'Jack Wilson,Nina Brown,Alex Smith,Brian Perez,David Martinez,John Kim'

names_split =names.split(' ') # escribe tu código aquí
#names_split=' '.join(names_split)
print(names_split)



name_surname = 'Joseph_Kobe_Steeler '
name_surname = name_surname.split('_')
name_surname=' '.join(name_surname)
print(name_surname)

name_surname = 'Joseph_Kobe_Steeler '
name_surname = name_surname.strip()
name_surname = name_surname.replace('_', ' ')

print(name_surname)

name_surname = 'Joseph Kobe Steeler'
name_split = name_surname.split()

print(name_split)


film_genres = ['scifi','drama','thriller','comedy','action']
for value in film_genres:
    print(value)
    
payers = [56, 65, 64, 63]
total=3
total += total+1
print(total)
for element in payers:
    print (payers)
    
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

for row in movies_info:
    runtime = row[4] # extrae la duración aquí
    runtime /=60 # convierte la duración extraída a horas
    print(runtime)   
    
    
orders = [
    [199.99, 2, 0.10],  # 10% de descuento
    [349.99, 1, 0.05],  # 5% de descuento
    [129.99, 3, 0.00],  # Sin descuento
    [499.99, 1, 0.20],  # 20% de descuento
    [249.99, 4, 0.15],  # 15% de descuento
]

# Inicializa las variables
total_revenue = 0
highest_order_value = max(orders[0])
descuento=0
descuento=orders[0][0]-orders[0][0]*orders[0][2]
print(descuento)
print(highest_order_value)



# Lista anidada de pedidos: [precio, cantidad, descuento]
