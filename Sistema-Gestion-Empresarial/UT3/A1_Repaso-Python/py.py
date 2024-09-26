# Importamos la libreria hashlib para el hash de la contraseña
import hashlib

# Creamos un diccionario donde se almacenaran los usuarios
users = {}

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
  key_name = "user" + str(len(users) + 1)
  username = input("Introduce el nombre de usuario: ")
  while check_user_exists(username):
    username = input("Este nombre de usuario ya existe!\nNuevo nombre de usuario: ")

  password = input("Introduce la contraseña para el usuario: ")

  users[key_name] = {
    "username" : username,
    "password" : hash_password(password)
  }
  print("El usuario " + username + " se ha registrado correctamente\n")
  main_menu()

# Comprueba si el usuario existe
def check_user_exists(username):
  for key in users:
    if users[key]["username"] == username:
      return True
  return False

# Comprueba que la clave corresponda al usuario y sea correcta
def check_password(username, password):
  for key in users:
    if users[key]["username"] == username and users[key]["password"] == password:
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
  users["user1"] = {"username" : "Jose", "password" : hash_password("Prueba1")}
  users["user2"] = {"username" : "Pedro", "password" : hash_password("Prueba2")}
  users["user3"] = {"username" : "Miguel", "password" : hash_password("Prueba3")}
  users["user4"] = {"username" : "Antonio", "password" : hash_password("Prueba4")}
  users["user5"] = {"username" : "Roberto", "password" : hash_password("Prueba5")}

fake_users()
main_menu()