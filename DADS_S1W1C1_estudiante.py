
# # Sprint 1 - Week 1 - Version 1
# 
# Coding Session
# 
# # Ejercicio 1
# 
# ## E1.1
# 
# John tiene 25 años y su hermano 20. Asigna sus edades a las variables
# `john_age` y `brother_age`, y verifica los tipos de variables que son
# cada una de ellas.
john_age=25
brother_age=20
print(type(john_age))
# 
# ## E1.2
# 
# Calcula su diferencia de edad en una nueva variable (`diff_ages`), y
# luego muestra la siguiente frase “John tiene `john_age` años. Su hermano
# tiene `brother_age` y la diferencia de edad entre ellos es `diff_ages`”

diff_ages=john_age-brother_age
print(diff_ages)
# ## E2.1
# 
# Escribe y rellena las siguientes variables:
# 
# `name` -\> John
# 
# `john_bitcoins` -\> 2.45
# 
# `btc_to_usd` -\> 71000
# 
# `has_driving_license` -\> True
name='John'
john_bitcoins=2.45
btc_to_usd=71000
has_driving_license=True
print(name, john_bitcoins, has_driving_license)
print(type(has_driving_license))
# 
# Muestra todas las variables. A continuación, aplica la función type a
# cada una y comprueba el resultado. Después, calcula e imprime la
# cantidad de BTC que John tiene en dólares estadounidenses, utilizando el
# tipo de conversión indicado.
# 
# # Ejercicio 3
# 
# ## E3.1
# 
# John compró más de 1.3 bitcoins. Ejecuta el siguiente código y observa
# el error.


john_bitcoins = '2.45'
john_bitcoins = float(john_bitcoins )
john_bitcoins = john_bitcoins + 1.3
john_bitcoins =int(john_bitcoins )
print(john_bitcoins )


# ## E3.2
# 
# Ahora agrega una línea entre las dos líneas de código existentes para
# convertir la variable a float, e imprimir la variable y su tipo. ¿Qué
# pasó?
# 
# ## E3.3
# 
# Ahora convierte los bitcoins de John a int e imprime la variable y su
# tipo. ¿Qué pasó? ¿Ha perdido bitcoins?
# 
# # Ejercicio 4
# 
# John quiere enviar el 10% de su bitcoin a su amigo Max. Sin embargo,
# seleccionó una cartera que, por alguna razón, no es considerada válida,
# lo que hace que el programa genere un error.
# 
# ## E4.1
# 
# Ejecuta el código y observa el error. ¿Por qué recibimos este error?



     
# ## E4.2
# 
# Añade código para que el error quede más claro, mostrando el mensaje “Tu
# cartera no es válida. Por favor, inténtalo de nuevo.”, cuando falla.
# 
# Haz esto utilizando try except.
btc_wallet_2 = '3.75'
btc_to_send = btc_wallet_2 * 0.1

 try:
    btc_to_send = btc_wallet_2 * 0.1
except:
    print('Tu cartera no es válida. Inténtalo de nuevo.')
# 
# ## E4.3
# 
# Ahora corrige el código para que no produzca más errores. ¿A qué tipo de
# datos debemos convertir la cartera?
try:
    btc_to_send = float(btc_wallet_2) * 0.1
except:
    print('Tu cartera no es válida. Inténtalo de nuevo.')
    
# 
# ## E4.4
# 
# Utiliza la función apropiada para convertirla y luego muestra la
# cantidad de btc enviada a su amigo Max de la siguiente manera: “Has
# enviado `btc_to_send` bitcoins con éxito”.
btc_wallet_2 = '3.75'
btc_wallet_2=float(btc_wallet_2)
try:
    btc_to_send = float(btc_wallet_2) * 0.1
except:
    print('Tu cartera no es válida. Inténtalo de nuevo.')
    
# 
# # Ejercicio 5
# 
# ## E5.1
# 
# Crea una lista que contenga 4 elementos a ser comprados en una tienda de
# abarrotes “azucar”, “flores”, “muchos colores”, “X”. Llámala
# `compras_abarrotes`.
# 
# ## E5.2
# 
# Imprime el tercer elemento de la lista
# 
# ## E5.3
# 
# Imprime el tamaño de la lista
# 
# ## E5.4
# 
# Adiciona un producto más al final de la lista.
# 
# ## E5.5
# 
# Adiciona un producto más en la posicion 2 de la lista e imprime el
# resultado.
# 
# # Ejercicio 6
# 
# Sea una lista de productos de ferretería dada por Tornillos, Martillo,
# Pegamento. Llama a esa variable `compras_ferreteria`
# 
# ## E6.1
# 
# Crea esta nueva lista
# 
# ## E6.2
# 
# Adiciona esta lista `compras_abarrotes` y guarda el resultado en
# `compras_ferreteria_mas_abarrotes`
# 
# ## E6.3
# 
# Ordena la lista de compras en orden reverso e imprime el resultado
# final.
# 
# # Ejercicio 7
# 
# Sea la lista `python` definida a continuación
# 
# ## E7.1
# 
# Establezca 3 formas diferentes de obtener solamente los caracteres “py”
# filtrando la lista
# 
# Sea ahora la lista `numeros` dada por
# 
# ## E7.2
# 
# Obtenga solamente los elementos que se encuentran en una posición par


