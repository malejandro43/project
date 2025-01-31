
start = 29 # ESCRIBE TU CÓDIGO AQUÍ
check = 'Error - While no ejecutado.'

while start < 30 and start > 28:
    start +=1
    check = '¡Listo! While ejecutado.'
start-=1
print(check)

annual_income = 150000 # ingreso anual de Jack
target_income = 1000000 # ingreso objetivo

total_income_sum = 0 # ingresos totales que se actualizarán para cada año
years_to_million = 0 # cantidad de años que también se actualizará

while total_income_sum < target_income:
    total_income_sum += 150000# escribe tu código aquí
    years_to_million +=1 # escribe tu código aquí
print(years_to_million)

for i in range(10):
    print(i)
    
    
age = 25
is_student = True

condition_1 = age >= 18
condition_2 = age >= 18 and is_student

print("Condición 1:", condition_1)
print("Condición final:", condition_2)

print('hola'.islower()) 
print('777'.isdigit()) 
print('el string contiene espacios, así como signos de puntuación'.isalpha())


age = 15

print(age <=12, "Eres niño.")

# Comprueba si la edad se encuentra entre 13 y 19
print(age>=13 and age <=19, "Eres adolescente.")

# Comprueba si la edad es 20 o más
print(age>=20, "Eres adulto.")

review_comment = "GreatProduct123"  # Puedes cambiar este valor para poner a prueba diferentes escenarios

# Review_comment contiene solo caracteres alfabéticos
print("El comentario solo contiene letras.",  review_comment.isalpha())

# Review_comment contiene solo dígitos
print("El comentario solo contiene números.", review_comment.isdigit())

# Review_comment contiene caracteres no alfabéticos y no tiene dígitos.
print("El comentario contiene caracteres no alfabéticos y no tiene dígitos.", not ( review_comment.isalpha() or review_comment.isdigit() ))


clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"]
]

elite_clients = [] # añade elite clients aquí
for variable in clients:
    if(variable[3]>200000):
        elite_clients.append(variable)
# escribe tu código aquí

print(elite_clients)




clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# listas vacías para agregar clientes
neo = []
plus = []
for variable in clients:
    if(variable[2]<41):
        neo.append(variable)
    else:
        plus.append(variable)

# escribe tu código aquí

print(neo)


countries = ['France', 'Italy', 'New Zealand', 'Italy', 'France', 'USA']
for variable in countries:
    if variable=='France':
        print("Le film est sorti en France.")
    elif variable=='Italy':
        print("Le film est sorti en Italia.")
    elif variable=='New Zealand':
        print("Country not defined.")
    else:
         print('The movie was released in the USA.')


ratings = [91, 35, 65, 89, 78, 93]
for variable in ratings:
    if variable >=0 and variable <=59:
        print("2")
    elif variable >= 60 and variable <=72:
        print("3")
    elif variable >=73 and variable <=84:
        print("4")
    else :
        print("5")


clients = [
    [32456, "Jack Wilson", 32, 150000, "Healthcare"],
    [34591, "Nina Brown", 45, 250000, "Telecom"],
    [37512, "Alex Smith", 39, 210000, "IT"],
    [39591, "Brian Perez", 29, 340000, "Transportation"],
    [45123, "Sarah Lee", 28, 120000, "Marketing"],
    [47635, "David Kim", 36, 180000, "Finance"],
    [49571, "Samantha Chen", 42, 220000, "Retail"],
    [50391, "Juan Rodriguez", 31, 160000, "Architecture"],
    [34556, "Lucas Hernandez", 37, 75000, "Education"],
    [64291, "Jessica Li", 25, 125000, "IT"],
    [74512, "Emma Davis", 47, 197000, "Finance"],
    [83191, "Sophia Perez", 34, 225000, "Transportation"],
    [91023, "Liam Kim", 29, 98000, "Retail"],
    [96435, "Ava Chen", 31, 175000, "Marketing"],
    [100571, "Noah Rodriguez", 28, 85000, "Architecture"],
    [101321, "Olivia Wilson", 44, 310000, "Telecom"],
    [104556, "William Brown", 38, 289000, "Finance"],
    [105491, "Emily Smith", 29, 193000, "Healthcare"],
    [107512, "Michael Perez", 53, 415000, "Transportation"]
]

# listas vacías para agregar clientes
standard = []
plus = []
elite = []
executive = []

for variable in clients:
    if variable[3]<100000:
        standard.append(variable)
    elif variable[3]>=100000 and variable[3]<=200000:
        plus.append(variable)
    elif variable[3]>=200000 and variable[3]<=300000:
        elite.append(variable)
    else:
        executive.append(variable)
# escribe tu código aquí


print(executive)