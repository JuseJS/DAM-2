import random

### Listado de Juegos ###
games = {
    "1"   :   "Piedra, Papel o Tijera",
    "2"   :   "Traducir Palabras",
    "3"   :   "Adivina el número"
}


### Listado de Palabras ###
words = {
    "random"    :   "aleatorio",
    "curious"   :   "curioso",
    "elephant"  :   "elefante",
    "beautiful" :   "hermoso",
    "mountain"  :   "montaña",
    "question"  :   "pregunta",
    "ocean"     :   "océano",
    "happy"     :   "feliz",
    "dream"     :   "sueño",
    "color"     :   "color",
    "window"    :   "ventana",
    "listen"    :   "escuchar",
    "travel"    :   "viajar",
    "book"      :   "libro",
    "garden"    :   "jardín",
    "smile"     :   "sonrisa",
    "star"      :   "estrella",
    "friend"    :   "amigo",
    "night"     :   "noche",
    "dance"     :   "bailar"
}


### Mensajes de Victoria y Derrota globales ###
def showWinMsg():
    print("================")
    print("¡Has Ganado \U0001F601!")
    print("================")
def showLoseMsg():
    print("================")
    print("¡Has Perdido \U0001F643!")
    print("================")


### Piedra Papel o Tijeras ###
def game1():
    options = ["piedra", "papel", "tijeras"]
    robotOption = random.choice(options)
    print(robotOption)

    print("\n==========¿Qué eliges?========")
    print("Piedra, Papel o Tijeras")
    playerOption = input("Tu opción: ").lower()

    while playerOption not in options:
        playerOption = input("Introduce una respuesta correcta: ")

    if playerOption == "piedra" and robotOption == "tijeras":
        showWinMsg()
        return
    if playerOption == "tijeras" and robotOption == "papel":
        showWinMsg()
        return
    if playerOption == "papel" and robotOption == "piedra":
        showWinMsg()
        return
    if playerOption == robotOption:
        print("======================================")
        print("Has Empatado, más suerte a la proxima!")
        print("======================================")
        return
    showLoseMsg()


### Traduce la palabra del ingles ###
def game2():
    points = 0
    for i in range(5):
        gameWord = random.choice(list(words.keys()))
        playerWord = input("Traduce la palabra " + gameWord + " al español: ")
        if playerWord.lower() == words.get(gameWord):
            print("Correcto +1 Punto!")
            points += 1
        else:
            print("No has acertado, más suerte a la proxima")
        del words[gameWord]
    showWinMsg
    print("Puntos: " + str(points) + "/5")
        


### Adivina el Número ##
def game3():
    gameNum = random.randint(1,200)
    trys = 0
    print("Intenta adivinar el número entre 1 y 200")
    while trys < 3:
        try:
            playerNum = int(input("¿Qué número crees que es?: "))
            if playerNum < 1 or playerNum > 200:
                raise Exception("número incorrecto")
            trys += 1
        except:
            print("Debes introducir un número entre 1 y 200")
        if playerNum < gameNum:
            print("Tu número es más pequeño que es de la máquina")
        if playerNum > gameNum:
            print("Tu número es más grande que es de la máquina")
        if playerNum == gameNum:
            trys = 3
            showWinMsg()
    

### Validar Juego Seleccionado ###
def validateSelectedGame(selectedGame):
    while selectedGame not in games:
        selectedGame = input("El input introducido no corresponde al número de ningun juego\nIntroduce un número correcto: ")
    if selectedGame == "1":
        game1()
    if selectedGame == "2":
        game2()
    if selectedGame == "3":
        game3()    


### Menu Inicial ###
print("\n==========Listado de Juegos==========")
for k, v in games.items():
    print(k, "-" , v)
print("=====================================")
selectedGame = input("Introduce el número del juego al que quieras jugar: ")
validateSelectedGame(selectedGame)