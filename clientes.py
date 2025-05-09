
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

incomes_per_field = {} # aquí colocarás los ingresos para cada campo
nombre_campo=""
ingresos=0

for client in clients:
    ingresos=client[3]
    nombre_campo=client[4]# primero, extrae el nombre del campo
	# segundo, extrae los ingresos
    if  nombre_campo not in incomes_per_field:
        incomes_per_field[nombre_campo] = []# comprueba si el campo extraído NO está en el diccionario incomes_per_field
		# añade un nuevo campo como clave y establece una lista como valor 
  
    incomes_per_field[nombre_campo].append(ingresos)# si el campo extraído está en el diccionario incomes_per_field
		# añade el nuevo ingreso a la lista de ingresos para un campo en particular
		

# no modifiques el código de abajo, ya que imprime el resultado
print(incomes_per_field)


items = {
    'Pizza margarita': 3,
        'Zumo de naranja': 2,
        'Patatas fritas medianas': 5
}

item = items.get('Pizza margherita')
print(item)


books = {
        'George Orwell': '1984',
    'Leo Tolstoy': 'Guerra y paz',
    'Ralph Ellison': 'El hombre invisible',
    'Antoine de Saint-Exupéry': 'El principito'
}

for author, title in books:
    print(author, title)




books = {
        'George Orwell': '1984',
    'Leo Tolstoy': 'Guerra y paz',
    'Ralph Ellison': 'El hombre invisible',
    'Antoine de Saint-Exupéry': 'El principito'
}

for author in books:
    print(author)
    

books = {
        'George Orwell': '1984',
    'Leo Tolstoy': 'Guerra y paz',
    'Ralph Ellison': 'El hombre invisible',
    'Antoine de Saint-Exupéry': 'El principito'
}

for author, title in books.items():
    print(author, title)
    
books = [
    {
        'author': 'George Orwell',
        'book': '1984',
        'page_count': 328
    },
    {
        'author': 'Leo Tolstoy',
        'book': 'Guerra y paz',
        'page_count': 1225
    },
    {
        'author': 'Ralph Ellison',
        'book': 'El hombre invisible',
        'page_count': 624
    },
    {
        'author': 'Antoine de Saint-Exupéry',
        'book': 'El principito',
        'page_count': 96
    }
]
total_page_count = 0

for book in books:
    total_page_count += book['page_count']
    
print(total_page_count)




# Diccionario para almacenar los libros
librero = {}

# Función para agregar libros al inventario
def add_book(title, autor, available=True):
    if title in librero:
        print(f"El libro '{title}' ya está en el inventario.")
    else:
        librero[title] = {'autor': autor, 'available': available}
        print(f"El libro '{title}' de {autor} se ha agregado al inventario.")

# Función para comprobar la disponibilidad de un libro
def check_availability(title):
    if title in librero:
        estado = "disponible" if librero[title]['available'] else "prestado"
        print(f"El libro '{title}' está {estado}.")
    else:
        print(f"El libro '{title}' no está en el inventario.")

# Función para prestar un libro
def lend_book(title):
    if title in librero:
        if librero[title]['available']:
            librero[title]['available'] = False
            print(f"Has prestado el libro '{title}'.")
        else:
            print(f"El libro '{title}' ya está prestado.")
    else:
        print(f"El libro '{title}' no está en el inventario.")

# Función para listar los libros según su estado
def list_books(status="all"):
    if status not in ["all", "available", "lent"]:
        print("Estado inválido. Usa 'all', 'available' o 'lent'.")
        return
    
    print("\nListado de libros:")
    for title, details in librero.items():
        if status == "all" or \
           (status == "available" and details['available']) or \
           (status == "lent" and not details['available']):
            estado = "disponible" if details['available'] else "prestado"
            print(f"- {title} (Autor: {details['autor']}, Estado: {estado})")

# Usar las funciones

# Agregar libros al inventario
add_book("1984", "George Orwell", available=True)
add_book("To Kill a Mockingbird", "Harper Lee", available=True)
add_book("The Great Gatsby", "F. Scott Fitzgerald", available=True)

# Comprobar la disponibilidad de un libro
check_availability("1984")
check_availability("Moby Dick")

# Prestar un libro
lend_book("1984")
lend_book("The Great Gatsby")

# Listar todos los libros
print("\nTodos los libros:")
list_books("all")

print("\nLibros disponibles:")
list_books("available")

print("\nLibros prestados:")
list_books("lent")