## A3 - Repaso Python
***EJ1 - Prepara un ejemplo donde expliques cómo hacer en Python 3 lo siguiente:***
- Clonar una lista.
```
lista_original = [1, 2, 3, 4, 5]
lista_copia = lista_original.copy()

print(lista_original)  # Output: [1, 2, 3, 4, 5]
print(lista_copia)     # Output: [1, 2, 3, 4, 5]
```

- ¿Cuál es la diferencia en Python entre “shallow copy” y “deep copy”?

Shallow Copy, es una copia superficial, por lo que crea una nueva estructura de datos, pero apuntan a la misma ubicacion en memoria que la original, por la que si se modifica una, se modifica la otra tambien.
```
lista_original = [1, [2, 3], 4]
lista_copia = lista_original.copy()

lista_copia[1][0] = 10

print(lista_original)  # Output: [1, [10, 3], 4]
print(lista_copia)     # Output: [1, [10, 3], 4]
```
Por otro lado Deep Copy es una copia profunda la cual crea una nueva estructura de datos y hace una copia recursiva de los elementos, de esta forma apuntan a una nueva direccion en memoria, por lo que los cambios en la copia no afectan a la original o viceversa.
```
import copy

lista_original = [1, [2, 3], 4]
lista_copia = copy.deepcopy(lista_original)

lista_copia[1][0] = 10

print(lista_original)  # Output: [1, [2, 3], 4]
print(lista_copia)     # Output: [1, [10, 3], 4]
```

- Añadir un elemento a una lista.

Añadir un elemento al final de la lista
```
lista = ["manzana", "platano", "fresa"]
lista.append("naranja")
print(lista)           # Output: ["manzana", "platano", "fresa", "naranja"]
```
Insertar elemento en una posicion especifica
```
lista = ["manzana", "platano", "fresa"]
lista.insert(1, "naranja")
print(lista)           # Output: ["manzana", "naranja", "platano", "fresa"]
```

- Quitar un elemento de una lista.

Quitar un elemento especifico de la lista
```
lista = ["manzana", "platano", "fresa"]
lista.remove("platano")
print(lista)           # Output: ["manzana", "fresa"]
```
En caso de existir mas de un valor igual, se eliminara la primera coincidencia
```
lista = ["manzana", "platano", "fresa", "platano", "kiwi"]
lista.remove("platano")
print(lista)           # Output: ["manzana", "fresa", "platano", "kiwi"]
```
Eliminar el elemento en un index especifico
```
lista = ["manzana", "platano", "fresa"]
lista.pop(1)
print(lista)           # Output: ["manzana", "fresa"]
```
Si no especificas el index, se elimina el ultimo elemento de la lista
```
lista = ["manzana", "platano", "fresa"]
lista.pop()
print(lista)           # Output: ["manzana", "platano"]
```
Otra forma de borrar un elemento de un index especifico es haciendo uso de del
```
lista = ["manzana", "platano", "fresa"]
del lista[0]
print(lista)           # Output: ['platano', 'fresa']
```

- Crear una nueva lista con los 4 últimos elementos de una lista.
```
lista = [10, 20, 30, 40, 50, 60, 70, 80]

# Obtener los 4 últimos elementos y crear una nueva lista
ultimos_cuatro = lista[-4:]

print(ultimos_cuatro)  # Output: [50, 60, 70, 80]
```

- Convertir las palabras de una cadena (separadas por espacios) en una lista.
```
cadena_palabras = "Hola mundo esto es una cadena de ejemplo"
lista_de_palabras = cadena_palabras.split()

print(lista_de_palabras)    # Output: ['Hola', 'mundo', 'esto', 'es', 'una', 'cadena', 'de', 'ejemplo']
```

- Comentarios de una línea.
Para hacer comentarios de una linea podemos usar #
```
# Esto es un ejemplo de comentario
nombre = "Jose"
print(nombre)
```

- Comentarios multilínea.
Para comentarios multilinea usamos """ al inicio y al final del comentario
```
"""
Esto es un
comentario que
tiene varias lineas
"""
```

***EJ2 - En Python 3 los tipos simples pasan por valor y los compuestos por referencia. Crea un ejemplo con 3 funciones que:***
- Reciban 2 números y devuelvan la suma.
```
def suma(num1, num2):
    return num1 + num2

print(suma(4,6))    # Output: 10
```

- Reciban una lista y modifiquen esa misma lista (referencia) duplicando los valores de todos los elementos. No debe devolver nada.
```
lista = [1,2,3,4,5]

def duplicar_valores(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2

duplicar_valores(lista)
print(lista)    # Output: [2, 4, 6, 8, 10]
```

- Reciban una lista y devuelvan una copia de esa misma lista (referencia) duplicando los valores de todos los elementos. La lista original no debe modificarse.
```
import copy

lista = [1,2,3,4,5]

def duplicar_valores(lista):
    lista_modifica = copy.deepcopy(lista)
    for i in range(len(lista_modifica)):
        lista_modifica[i] = lista_modifica[i] * 2
    return lista_modifica

lista_modifica = duplicar_valores(lista)
print(lista)            # Output: [1, 2, 3, 4, 5]
print(lista_modifica)   # Output: [2, 4, 6, 8, 10]
```

***EJ3 - A partir de un contexto donde queremos almacenar un usuario y su contraseña, haz un ejemplo que explique cómo se haría:***
- Usando una lista.
```
# Importamos la libreria hashlib para el hash de la contraseña
import hashlib

# Creamos la lista donde se almacenaran los usuarios
users = []

# Hasehamos la contraseña a sha512
def hash_password(password):
  password_bytes = password.encode('utf-8')

  sha512 = hashlib.sha512()

  sha512.update(password_bytes)

  hashed_password = sha512.hexdigest()

  return hashed_password

# Comprueba los datos del usuario para iniciar sesion
def login_user():
  username = input("Introduce el nombre de usuario: ")
  while not check_user_exists(username):
    username = input("El nombre de usuario no existe, introduce un nombre valida: ")

  password = input("Introduce la contrasaña del usuario: ")
  while not check_password(username, hash_password(password)):
    password = input("La contraseña no es correcta, vuelvelo a intentar: ")

  print("Has iniciado sesion correctamente con el usuario: " + username + "\n")
  main_menu()

# Registra un nuevo usuario, comprobando que ya no exista
def register_user():
  username = input("Introduce el nombre de usuario: ")
  while check_user_exists(username):
    username = input("Este nombre de usuario ya existe!\nNuevo nombre de usuario: ")

  password = input("Introduce la contraseña para el usuario: ")
  users.append([username, hash_password(password)])
  print("El usuario " + username + " se ha registrado correctamente\n")
  main_menu()

# Comprueba si el usuario existe ya en la lista
def check_user_exists(username):
  for i in range(len(users)):
    if users[i][0] == username:
      return True
  return False

# Comprueba que la clave corresponda al usuario y sea correcta
def check_password(username, password):
  for i in range(len(users)):
    if users[i][0] == username and users[i][1] == password:
      return True
  return False

# Muestra el menu inicial
def main_menu():
  opcion = "0"
  while not (opcion == "1" or opcion == "2" or opcion == "3"):
    opcion = input("¿Que deseas hacer? \n1 - Iniciar sesion \n2 - Registrar un nuevo usuario\n3 - Salir\n- ")
  if opcion == "1":
    login_user()
    return
  if opcion == "3":
    print("Adios!")
    return
  register_user()

# Crea datos falsos para probar el programa
def fake_users():
  users.append(["Jose", hash_password("Prueba1")])
  users.append(["Pedro", hash_password("Prueba2")])
  users.append(["Miguel", hash_password("Prueba3")])
  users.append(["Antonio", hash_password("Prueba4")])
  users.append(["Roberto", hash_password("Prueba5")])

fake_users()
main_menu()
```
[![Miniatura del video](https://i.imgur.com/ejemplo.png)](https://www.youtube.com/watch?v=Kp4Mvapo5kc&pp=ygUGcHl0aG9u)

- Usando un diccionario.
- Al llenarse, las contraseñas deben pasarse a un formato Hash (por ejemplo, SHA-512).
- El ejemplo debe llenar la lista con 5 usuarios/contraseña y hacer dos consultas.